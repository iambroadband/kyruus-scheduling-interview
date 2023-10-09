from datetime import time
from typing import Optional

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse

from app.database.db import DB
from app.models import AddDoctorRequest
from app.models.error import NotFoundException
from app.services.availability_service import AvailabilityService
from app.services.doctor_service import DoctorService
from app.settings import Settings

FORCE_INIT_DB = False


def create_app() -> FastAPI:
    doctor_service: DoctorService
    availability_service: AvailabilityService
    db: Optional[DB] = None
    if Settings.in_database:
        db = DB()
        db.init_if_needed(force=FORCE_INIT_DB)
        doctor_service = DoctorService(db=db)
        availability_service = AvailabilityService(db=db)

    app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

    @app.get("/doctors")
    def list_doctors():
        return doctor_service.list_doctors()

    @app.get("/doctors/{id}")
    async def get_doctor(id: int):
        return doctor_service.get_doctor(id)

    @app.post("/doctors")
    def add_doctor(request: AddDoctorRequest):
        id = doctor_service.add_doctor(
            first_name=request.first_name, last_name=request.last_name
        )

        return {"id": id}

    @app.get("/doctors/{doctor_id}/locations")
    def get_doctor_locations(doctor_id: int):
        return doctor_service.list_doctor_locations(doctor_id=doctor_id)

    @app.get("/doctors/{doctor_id}/schedules")
    def get_doctor_schedules(doctor_id: int):
        return doctor_service.list_doctor_schedules(doctor_id=doctor_id)

    @app.get("/availability/{doctor_id}/appointments")
    def get_doctor_appointments(doctor_id: int):
        return availability_service.list_doctor_appointments(doctor_id=doctor_id)

    @app.get("/availability/{doctor_id}")
    def get_doctor_availability(doctor_id: int):
        return availability_service.list_doctor_availability(doctor_id=doctor_id)

    @app.get("/availability/{doctor_id}/book")
    def add_doctor_appointment(doctor_id: int, location_id: int, start_time: time):
        return availability_service.book_doctor_appointment(doctor_id=doctor_id, location_id=location_id, start_time=start_time)

    @app.delete("/availability/{appointment_id}/cancel")
    def delete_doctor_appointment(appointment_id: int):
        return availability_service.cancel_doctor_appointment(
            appointment_id=appointment_id
        )

    @app.exception_handler(NotFoundException)
    async def not_found(request: Request, exc: NotFoundException):
        return Response(status_code=404)

    @app.on_event("shutdown")
    def shutdown():
        if db:
            db.close_db()

    @app.get("/", include_in_schema=False)
    def root():
        return RedirectResponse("/docs")

    return app


app = create_app()
