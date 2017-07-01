def minutes_to_hours(minutes):
# this function converts minutes to hours
    hours = minutes / 60
    return hours

def minutes_to_seconds(seconds):
# this function converts seconds to hours
    hours = seconds / 3600
    return hours

a = minutes_to_hours(30) + 1

b = minutes_to_seconds(600)

print(a)

print(b)
