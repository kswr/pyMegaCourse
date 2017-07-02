def minutes_to_hours(minutes=70, seconds):
# this function converts minutes and seconds to hours, it's default value for argument "minutes" is 70
    hours = minutes / 60 + seconds / 3600
    return hours

def seconds_to_hours(seconds):
# this function converts seconds to hours
    hours = seconds / 3600
    return hours

a = minutes_to_hours(30, 3000)

b = seconds_to_hours(600)

print(a)

print(b)
