
# import the time module 
import time 
import weather
  
# define the countdown func. 

def interval(t1): 

    
    while t1: 
        mins, secs = divmod(t1, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t1 -= 1
      

def dry_rock_countdown(t2, restart, climb, rain): 

    
    while t2: 
        mins, secs = divmod(t2, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t2 -= 1
        if t2 == 0:
            climb = True
            print(climb)
            print("You may go climb at Santstone MN*") 
        if t2 % 180 == 0:
            climb, rain = weather.check(climb, rain) 
            if rain is True:
                t2 = restart        
      


  
# input time in seconds 
#t = input("Enter the time in seconds: ") 

if __name__ == "__main__": 
    countdown(t)