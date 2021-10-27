from write_to_file import *
from  tgb.manictime import getLastfewHours,get_manictime_last_x_days

def getText():
    text = ""
    time = getTime(datetime.now())
    text += time +"\n"
   
#     '''TODO:
# shower 
# make fasting app'''
    return text
