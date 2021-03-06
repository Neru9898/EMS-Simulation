from datetime import datetime, timedelta, timezone
from time import sleep
import threading
from simulation_modules.murb_module.power_from_time_model import power_from_time

my_date = datetime.now(timezone.utc)

counter = 0
power = 0

dict_time_jump = {
    "pastDay": (4*24)-1,
    "pastWeek": (4*24*7)-1,
    "pastMonth": (4*24*30)-1,
    "pastYear": (4*24*365)-1
}

dict_time_delta = {
    "pastDay": 1,
    "pastWeek": 1*7,
    "pastMonth": 1*30,
    "pastYear": 1*365
}


def murb_simulation_init(sio):

    def realTimeData(parameters):
        global timer
        timer = threading.Timer(900.0, realTimeData)
        timer.start()
        TimeStamp = datetime.now(timezone.utc).isoformat()
        Power = power_from_time(datetime.now(timezone.utc), parameters)
        sio.emit('New Murb Power', {
            'TimeStamp': TimeStamp,
            'Power': Power
        })

    @sio.on('Generate Murb Power')
    def generate_murb_power(interval, parameters):
        global counter
        global power
        interval_datetime = datetime.now(timezone.utc)-timedelta(0, 900)

        realTimeData(parameters)
        while counter < (dict_time_jump[interval]):
            counter = counter + 1
            interval_datetime = interval_datetime - timedelta(0, 900)
            TimeStamp = interval_datetime.isoformat()
            Power = power_from_time(interval_datetime, parameters)

            sio.emit('Old Murb Power', {
                'TimeStamp': TimeStamp,
                'Power': Power
            })

            # Sleep every 100th iteration to prevent server from getting overloaded
            if ((counter % 100) == 1):
                sleep(3)

        counter = 0

    @sio.on('Status Check')
    def status_check():
        if 'timer' in globals():
            real_time_data_status = timer.is_alive()
        else:
            real_time_data_status = False

        return {
            'real_time_data_status': real_time_data_status,
            'data_generate_config': dict_time_jump
        }

    @sio.on('Pre - Generate Murb Power')
    def pre_send_past_day():
        print("Received")

    @sio.on('Stop Murb Power')
    def stop_murb_data():
        global timer
        if 'timer' in globals():
            timer.cancel()
