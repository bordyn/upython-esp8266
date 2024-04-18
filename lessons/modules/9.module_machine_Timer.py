from machine import Timer,Pin
from time import sleep

# start testing timer
tim = Timer(0)

# write this routine to confirm that timer activation expired
timer_executed = False
def OneShotTimerActivation(t):
    global timer_executed
    print ("Timer shot executed")
    timer_executed = True

# start timer shot
tim.init(mode=Timer.ONE_SHOT,period=1000,callback=OneShotTimerActivation)
while not timer_executed:
    sleep(0.1)

# remove old configurations
tim.deinit()

# write this routine to keep on excuting this one
def PeriodicTimerActivation(t):
    print ("Timer Periodic executed")

# start timer periodic
tim.init(mode=Timer.PERIODIC,period=1000,callback=PeriodicTimerActivation)
sleep(10)
# stop
tim.deinit()
    

