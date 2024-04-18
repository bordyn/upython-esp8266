from machine import RTC

# show datetime at current date
rtc_clock = machine.RTC()
print (rtc_clock.datetime())

def rtc_datetime_to_bkk_time(dt,gmt=7):
    year,month,day,week,hrs,minute,seconds,ms = dt
    if hrs + gmt >= 24:
        hrs = hrs + gmt - 24
        day = day + 1
    else:
        hrs = hrs + gmt
    return (year,month,day,week,hrs,minute,seconds,ms)

# convert this to Bangkok time
print (rtc_datetime_to_bkk_time(rtc_clock.datetime()))

# routine to add more minute to datetime
def rtc_next_minutes(dt,add_min):
    assert (add_min > 60,"limit this to 60 mins only")
    year,month,day,week,hrs,minute,seconds,ms = dt
    if minute + add_min >= 60:
        minute = minute + add_min - 60
        hrs = hrs + 1
    else:
        minute = minute + add_min
    return (year,month,day,week,hrs,minute,seconds,ms)

# convert this to next minutes
bkk_time = rtc_datetime_to_bkk_time(rtc_clock.datetime())
print ("next 15 mins is ",rtc_next_minutes(bkk_time,15))

