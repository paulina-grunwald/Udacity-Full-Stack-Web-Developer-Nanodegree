#Making The Program Wait

import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
#time.ctime() - gives current time
#time.sleep - suspends program for specified time
while(break_count<total_breaks):
	time.sleep(10)
	webbrowser.open("http://www.google.com")
	break_count = break_count+1