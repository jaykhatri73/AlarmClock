import datetime
import time


def alarm(alarm_time):

    # capturing system's time and converting it into string
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("WAKE UP! \n WAKE UP! \n WAKE UP!")
            break

        # sleep time to avoid repeating the code again and again
        time.sleep(1)


print("Please note that the time is in 24-Hour format.")
alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

alarm(alarm_time)
