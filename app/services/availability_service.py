from abc import ABC, abstractmethod
from datetime import time
from typing import List

from app.database.db import DB
from app.models import (Doctor, DoctorAppointment, DoctorLocation,
                        DoctorSchedule, Location)
from app.models.error import SchedulingConflictException


class AvailabilityService:
    """
    This is left up to you to implement, generally following the patterns in the repo.

    That said, *don't* feel obliged to make an abstract base class/interface for your chosen approach - you
    can simply write the service using either the database or in-memory approach from the beginning.
    We used that pattern for the doctor_service to have examples for both modes.
    """

    # * Ability to book an appointment with a doctor (a tuple of (doctor, location, time))
    # * Ability to cancel an appointment with a doctor

    def __init__(self, db: DB):
        self.db = db

    def list_doctor_appointments(self, doctor_id: int) -> List[DoctorAppointment]:
        dict_result = self.db.execute(
            "SELECT da.id, da.doctor_id, da.location_id, da.doctor_schedule_id "
            "FROM doctor_appointments da "
            "WHERE da.doctor_id = ?",
            [doctor_id],
        )

        return [DoctorAppointment(**res) for res in dict_result]

    def list_doctor_availability(self, doctor_id: int) -> List[DoctorSchedule]:
        dict_result = self.db.execute(
            "SELECT id, doctor_id, day_of_week, start_time, end_time "
            "FROM doctor_schedules "
            "WHERE doctor_id = ? AND id NOT IN "
            "(SELECT doctor_schedule_id FROM doctor_appointments WHERE doctor_id = ?) ",
            # NOTE: I am certain there is a syntactically correct way to do this, but I don't know it
            [doctor_id, doctor_id],
        )

        return [DoctorSchedule(**res) for res in dict_result]

    def book_doctor_appointment(
        self, doctor_id: int, location_id: int, start_time: time
    ) -> int:
        doctor_availability = self.list_doctor_availability(doctor_id=doctor_id)

        # TODO:
        # NOTE: book appointments as hour only (assumption for this take home)
        # get the doctor's availability
        # create a new DoctorAppointment and insert it to the database if the time slot is available
        # else, return an error?
        pass

    def cancel_doctor_appointment(self, appointment_id: int) -> DoctorAppointment:
        cancelled_appointment = self.db.execute(
            "DELETE FROM doctor_appointments " "WHERE id=(?) RETURNING *;",
            [appointment_id],
        )

        if cancelled_appointment is not None:
            return cancelled_appointment
