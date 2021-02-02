import time

# named_tuple = time.localtime() # get struct_time
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
#
# print(time_string)
#
#
# # seconds passed since epoch
# #seconds = 1545925769.9618232
# local_time = time.ctime()
# local_time + 16
# print("Local time:", local_time)

from datetime import timedelta, datetime

today = print(datetime.today().strftime("%Y-%m-%d"))
# tomorrow = datetime.today() + timedelta(15)
# tomorrow=tomorrow.strftime("%Y-%m-%d")
# print(today,'\n',tomorrow)

#today = print(datetime.today())

