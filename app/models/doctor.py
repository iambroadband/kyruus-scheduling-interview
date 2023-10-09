from __future__ import annotations

from datetime import time

from pydantic import BaseModel, Field


class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str


class Location(BaseModel):
    id: int
    address: str


class DoctorLocation(BaseModel):
    """
    This indicates that a doctor works at a location. Locations can have
    multiple doctors, and doctors can have multiple locations
    """

    id: int
    doctor_id: int
    location_id: int


class DoctorSchedule(BaseModel):
    """
    This indicates that a doctor is available during the given schedule.
    """

    id: int
    doctor_id: int
    day_of_week: int
    start_time: time
    end_time: time


class DoctorAppointment(BaseModel):
    """
    This indicates that a doctor has an appointment for the given times at the
    given location.
    """

    id: int
    doctor_id: int
    location_id: int
    day_of_week: int
    start_time: time
    end_time: time
