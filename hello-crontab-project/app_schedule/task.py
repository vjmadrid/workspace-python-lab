from datetime import datetime
import schedule
import time

def main():
    #print(f"Running script at {datetime.now()}")
    #print(f"Hello Crontab :: {datetime.now().strftime('%H:%M:%S')}")
    print("Hello Crontab 'Schedule' :: " + str(datetime.now()))

def job():
    main()

schedule.every().hour.at("00:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)