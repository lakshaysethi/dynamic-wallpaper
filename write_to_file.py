from datetime import *
from time import sleep

def getTime(obj):
	time = str(obj).split()[1].split('.')[0].split(":")
	return f'{time[0]}:{time[1]}'#:{time[2]}'

# while True:
#     content = ''
#     f = open("timenow.txt", "w")
#     #content += f'started at {getTime(started)} \n'
#     content += getTime(datetime.now())
#     #breaktime = 'break time 10 mins \n will be back at 18:30 ' 
#     #content+= breaktime
#     f.write(content)
#     f.close()
#     sleep(1)