USE iot_proyecto;

CREATE VIEW ´View_HR_readings´ AS
SELECT users.name AS "Nombre", users.last_name AS "Apellido", 
        hr_readings.hr_reading AS "Rimto cardiaco", hr_readings.time AS "Fecha"
FROM iot_proyecto.users INNER JOIN iot_proyecto.hr_readings
ON iot_proyecto.users.id_user = iot_proyecto.hr_readings.id_user
ORDER BY hr_readings.time DESC;


CREATE VIEW ´View_SaO2_readings´ AS
SELECT users.name AS "Nombre", users.last_name AS "Apellido", 
        sao2_readings.sao2_reading AS "Nivel Oxígeno", sao2_readings.time AS "Fecha"
FROM iot_proyecto.users INNER JOIN iot_proyecto.sao2_readings
ON iot_proyecto.users.id_user = iot_proyecto.sao2_readings.id_user
ORDER BY sao2_readings.time DESC;