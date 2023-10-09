import timer
import weather

can_i_climb = True
raining = True
while True:
    can_i_climb, raining = weather.check(can_i_climb, raining)
    while raining == False:
        interval = 180
        timer.interval(interval)
        can_i_climb, raining = weather.check(can_i_climb, raining)
    else:
        two_days = 48*60*60
        timer.dry_rock_countdown(two_days, two_days, can_i_climb, raining)

