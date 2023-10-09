from abc import ABC, abstractmethod
from datetime import time
from typing import List

from app.database.db import DB
from app.models import (Doctor, DoctorAppointment, DoctorLocation,
                        DoctorSchedule, Location)
from app.models.error import NotFoundException


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
            "SELECT da.id, da.doctor_id, da.location_id, da.day_of_week, da.start_time, da.end_time "
            "FROM doctor_appointments da "
            "WHERE da.doctor_id = ?",
            [doctor_id],
        )

        return [DoctorAppointment(**res) for res in dict_result]

    def list_doctor_availability(self, doctor_id: int) -> List[DoctorSchedule]:
        # TODO:
        # get all the schedules for a doctor
        # get all the appointments for a doctor
        # filter out the time slots where there is overlap
        # return a list of the time slots that didn't have overlap
        pass

    def book_doctor_appointment(
        self, doctor_id: int, location_id: int, start_time: time
    ) -> int:
        # TODO:
        # NOTE: book appointments as hour only (assumption for this take home)
        # get the doctor's availability
        # create a new DoctorAppointment and insert it to the database if the time slot is available
        # else, return an error?
        pass

    def cancel_doctor_appointment(self, appointment_id: int) -> None:
        self.db.execute(
            "DELETE FROM doctor_appointments " "WHERE id=(?)",
            [appointment_id],
        )
