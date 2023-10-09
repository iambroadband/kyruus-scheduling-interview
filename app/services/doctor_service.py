from typing import List

from app.database.db import DB
from app.models import (Doctor, DoctorAppointment, DoctorLocation,
                        DoctorSchedule, Location)
from app.models.error import NotFoundException


class DoctorService:
    def __init__(self, db: DB):
        self.db = db

    def list_doctors(self) -> List[Doctor]:
        dict_result = self.db.execute(
            "SELECT id, first_name, last_name " "FROM doctors"
        )

        return [Doctor(**res) for res in dict_result]

    def get_doctor(self, id: int) -> Doctor:
        dict_result = self.db.execute(
            "SELECT id, first_name, last_name " "FROM doctors " "WHERE id = ?", [id]
        )

        if not dict_result:
            raise NotFoundException()

        if len(dict_result) > 1:
            raise Exception("Found more than one doctor with that ID")

        return Doctor(**dict_result[0])

    def add_doctor(self, first_name: str, last_name: str) -> int:
        self.db.execute(
            "INSERT INTO doctors (first_name, last_name) " "VALUES (?, ?)",
            [first_name, last_name],
        )

        id = self.db.last_row_id

        assert id

        return id

    def list_doctor_locations(self, doctor_id: int) -> List[Location]:
        dict_result = self.db.execute(
            "SELECT l.id, l.address "
            "FROM doctor_locations dl "
            "INNER JOIN locations l ON dl.location_id = l.id "
            "WHERE dl.doctor_id = ?",
            [doctor_id],
        )

        return [Location(**res) for res in dict_result]

    def list_doctor_schedules(self, doctor_id: int) -> List[DoctorSchedule]:
        dict_result = self.db.execute(
            "SELECT ds.id, ds.doctor_id, ds.day_of_week, ds.start_time, ds.end_time "
            "FROM doctor_schedules ds "
            "WHERE ds.doctor_id = ?",
            [doctor_id],
        )

        return [DoctorSchedule(**res) for res in dict_result]
