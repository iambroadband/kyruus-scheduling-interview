DELETE FROM doctor_locations;
DELETE FROM doctor_schedules;
DELETE FROM doctor_appointments;
DELETE FROM doctors;
DELETE FROM locations;

INSERT INTO doctors(id, first_name, last_name) VALUES (0, 'Jane', 'Wright');
INSERT INTO doctors(id, first_name, last_name) VALUES (1, 'Joseph', 'Lister');

INSERT INTO locations(id, address) VALUES (0, '1 Park St');
INSERT INTO locations(id, address) VALUES (1, '2 University Ave');

INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (0, 0, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (1, 1, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (2, 1, 1);

-- Jane's Schedule (only available on Monday)
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (0, 0, 0, '09:00', '10:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (1, 0, 0, '10:00', '11:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (2, 0, 0, '11:00', '12:00');
-- Unavailable around lunch time
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (3, 0, 0, '14:00', '15:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (4, 0, 0, '15:00', '16:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (5, 0, 0, '16:00', '17:00');

-- Joseph's Schedule (available every weekday from noon to 2pm)
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (6, 1, 0, '12:00', '13:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (7, 1, 0, '13:00', '14:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (8, 1, 1, '12:00', '13:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (9, 1, 1, '13:00', '14:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (10, 1, 2, '12:00', '13:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (11, 1, 2, '13:00', '14:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (12, 1, 3, '12:00', '13:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (13, 1, 3, '13:00', '14:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (14, 1, 4, '12:00', '13:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (15, 1, 4, '13:00', '14:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (16, 1, 5, '12:00', '13:00');
INSERT INTO doctor_schedules(id, doctor_id, day_of_week, start_time, end_time) VALUES (17, 1, 5, '13:00', '14:00');


-- Jane's Appointments
INSERT INTO doctor_appointments(id, doctor_id, location_id, doctor_schedule_id) VALUES (0, 0, 0, 0);
INSERT INTO doctor_appointments(id, doctor_id, location_id, doctor_schedule_id) VALUES (1, 0, 1, 1);

-- Joseph's Appointments
INSERT INTO doctor_appointments(id, doctor_id, location_id, doctor_schedule_id) VALUES (2, 1, 0, 6);
INSERT INTO doctor_appointments(id, doctor_id, location_id, doctor_schedule_id) VALUES (3, 1, 1, 9);
INSERT INTO doctor_appointments(id, doctor_id, location_id, doctor_schedule_id) VALUES (4, 1, 1, 10);
