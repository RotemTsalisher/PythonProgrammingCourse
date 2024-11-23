number_of_seconds = int(input("enter number of seconds: "))

# seconds in minute = 60 {120 seconds / 60 = 2 minutes}
# minute in an hour = 60 {120 minute / 60 = 2 hours}
# seconds / 3600 = hours
# take only the whole part: seconds // 3600 = whole part of the hours

hours = (number_of_seconds // 3600) % 24
minutes = (number_of_seconds // 60) % 60
seconds = number_of_seconds % 60

print(f"clock view: {hours:02d}:{minutes:02d}:{seconds:02d}")
# 7200 + 48