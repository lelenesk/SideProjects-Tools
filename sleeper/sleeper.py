import os
import sys
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M")
print("Current time is ",current_time)
current_time = current_time.split(":")

shutdown_time = input("Shutdown time: ")
shutdown_time = shutdown_time.split(":")

current_time = now.strftime("%H:%M")
current_time = current_time.split(":")

seconds=((int(shutdown_time[0])-int(current_time[0]))*60*60)+(int(shutdown_time[0])-int(current_time[0])*60)

if (seconds < 0 ):
  seconds = 0
try:
  os.system(f'shutdown /s /t {seconds}')
  cancel = input(f"Kikapcsolás {seconds} mp múlva .\n C-vel megszakítás, Enter kilépés.")
except:
  input("Hiba", sys.exc_info()[0], "Enter")
if(cancel=="C"):
  os.system('shutdown /a')
  input("Visszavonva.")