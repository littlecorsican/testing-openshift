import schedule
import time
from datetime import datetime

def job():
    print("I'm working...")
    print(datetime.now())
    f = open("demofile2.txt", "a")
    f.write(f"bla bla \n")
    f.close()

schedule.every(10).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)