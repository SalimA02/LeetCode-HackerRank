def timeConversion(s):
    minutes = s[3:5]
    seconds = s[6:8]
    hours = s[0:2]
    ampm = s[8:]
    
    if ampm == "AM" and hours == "12":
        hours = "00"
    elif ampm == "PM" and hours != "12":
        hours = int(hours)
        hours += 12
        hours = str(hours)
    
    return f"{hours}:{minutes}:{seconds}"
