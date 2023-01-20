

import datetime
from datetime import datetime

# cur_time = datetime.datetime.now()

# print(f"current time = {cur_time}   ")

print("setting time....")

# ret_status = datetime.time(hour=20, minute=30)
# print(f"return status = {ret_status}")

time_ = datetime.strptime("8:30:00","%H:%M:%S")

print(f"new time = {time_}  ")






