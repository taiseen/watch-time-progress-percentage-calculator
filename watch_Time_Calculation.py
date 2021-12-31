# 28 Dec 2021

# importing "math" for precision function
import math
  
def watch_Time_Calculation():
    totalHours = int(input('Enter Total Hours : '))
    totalMinuts = int(input('& Remaining Minuts : '))
    print('==============================')
    watchHours = int(input('Enter Your Watching Hours : '))
    watchMinutes = int(input('& Remaining Minutes are : '))

    totalTime = (totalHours * 60) + totalMinuts
    watchTime = (watchHours * 60) + watchMinutes
    remain_time = totalTime - watchTime

    remain_hours = remain_time / 60
    remain_minutes = remain_time % 60

    complete = (watchTime / totalTime) * 100
    remaining = 100 - complete

    #print("Total Time is : ${totalTime}Hour " + hours + " & minutes :" + minutes)

    print('\nTotal Completed :', math.trunc(complete), '%')
    print('Total Remaining :', math.trunc(remaining), '%')
    
    print('\nRemaining Time is :' , math.trunc(remain_hours),'h &' , remain_minutes,'m' );
    
    input("\nPress Enter to continue...")

# Function Calling
watch_Time_Calculation()

  
