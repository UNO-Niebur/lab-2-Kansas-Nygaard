#FutureTime.py
#Name: Kansas Nygaard
#Date: 02/01/2026
#Assignment: Lab 2: FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  addHours = int(input("Enter additional hours: "))
  #Ask user for minutes
  addMinutes = int(input("Enter additional minutes: "))

  #Calculate the time after the user-supplied time has passed.
 
  #convert to minutes
  totalMinutes = currentHour * 60 + currentMinute
  addedMinutes = addHours * 60 + addMinutes
 
  #calculate future time
  futuretotalMinutes = (totalMinutes + addedMinutes) % (24*60)
 
  #convert back to HH:MM
  futureHour = futuretotalMinutes // 60
  futureMinute = futuretotalMinutes % 60
  



  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("The future time is: {:02d}:{:02d}" .format(futureHour, futureMinute))


if __name__ == '__main__':
  main()
