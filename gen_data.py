import datetime
import random

testCases = 300
startTime = datetime.datetime(2019, 1, 1)
endTime = datetime.datetime(2019, 1, 20)

soilHumidity = 29.76
soilTemperature = 27.3
pipeSurfaceTemperature = 27
gasPressure = 100221.98
ultrasoundDistance = 2.4
batteryCharge = 1800

pool = [1] * 75 + [2] * 10 + [3] * 8 + [4] * 8 + [5] * 8 + [6] * 8 + [7] * 4 + [8] * 4 + [9] * 3 + [10] * 2


def jitter(base, percentage):
    mult = (100 - random.randint(-percentage, percentage)) / 100
    return base * mult


(1, '2019-01-19 15:30:00', '6.00', '64.00', '3.00', '4.00', '5.00', '6.00');


def write_sensor_data(deviceID, time):
    data = "INSERT INTO sensorData (deviceID, time, soilHumidity, soilTemperature, " \
           "pipeSurfaceTemperature, gasPressure, ultrasoundDistance, batteryCharge) VALUES ("
    if (deviceID % 10) == 0:
        jper = 30
    else:
        jper = 12
    data += f"{deviceID},'{time}','{jitter(soilHumidity,jper)}','{jitter(soilTemperature,jper)}'," \
            f"'{jitter(pipeSurfaceTemperature,jper)}','{jitter(gasPressure,jper)}'," \
            f"'{jitter(ultrasoundDistance,jper)}','{jitter(batteryCharge,jper)}');\n"
    return data


def generate_sensor_scheme():
    with open("sensor_data.sql", "w+") as file:
        for i in range(1, testCases + 1):
            time = startTime
            while time < endTime:
                file.write(write_sensor_data(i, time))
                time += datetime.timedelta(minutes=30)


def random_date(start, end):
    delta = end - start
    int_delta = delta.total_seconds()
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def random_severity():
    return random.choice(pool)


def write_sensor_meta(deviceID, time):
    data = "INSERT INTO sensorMeta (deviceID, time, latitude, longitude, sensorInstallDate, pipeInstallDate, severityLevel, labels) VALUES "
    if (deviceID % 10) == 0:
        jper = 10
    else:
        jper = 4

    if deviceID < 100:
        latitude = 45.274098
        longitude = -73.863636
    elif deviceID < 200:
        latitude = 45.3358
        longitude = -73.8434
    elif deviceID < 300:
        latitude = 45.982
        longitude = -73.6386
    elif deviceID < 400:
        latitude = 45.256
        longitude = -73.9807
    elif deviceID < 500:
        latitude = 45.4929
        longitude = -73.629
    else:
        latitude = 45.4713
        longitude = -73.7032

    earlyTime = datetime.datetime(1960, 1, 1)
    medTime = datetime.datetime(2017, 1, 1)
    endingTime = datetime.datetime(2018, 1, 10)

    data += f"({deviceID},'{time}','{latitude + jitter(0.2,jper * 5)}','{longitude + jitter(0.2,jper * 5)}'," \
            f"'{random_date(medTime, endingTime)}','{random_date(earlyTime, endingTime)}'," \
            f"{random_severity()},'{jitter(batteryCharge,jper)}, \'\'');\n"
    return data


def main():
    with open("sensor_meta.sql", "w+") as file:
        sTime = datetime.datetime(2019, 1, 1)
        eTime = datetime.datetime(2019, 1, 20)
        for i in range(1, 601):
            file.write(write_sensor_meta(i, random_date(sTime, eTime)))


if __name__ == "__main__":
    main()
