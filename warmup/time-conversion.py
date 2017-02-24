
time = input().strip()
hours = int(time[:2])

if "PM" in time:
    if hours == 12:
        pass
    else:
        hours += 12
elif "AM" in time:
    if hours == 12:
        hours -= 12


if hours < 10:
    hours = "0"+str(hours)
result = str(hours)+time[2:len(time)-2]
print(result)
