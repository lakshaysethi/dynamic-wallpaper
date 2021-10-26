from write_to_file import *
from  tgb.manictime import getLastfewHours

def getText():
    text = ""
    time = getTime(datetime.now())
    text += time +"\n"
   
#     '''TODO:
# shower 
# make fasting app'''
    return text
