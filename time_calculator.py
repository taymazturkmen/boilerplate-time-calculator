import math
def add_time(start, duration):
    hour = int(start[0:start.find(":")])
    minute = int(start[start.find(":")+1:start.find(":")+3])
    mode = (start[len(start)-2:len(start)])

    hourDuration = int(duration[0:duration.find(":")])
    minuteDuration = int(duration[duration.find(":")+1:duration.find(":")+3])

    newMinute = minute+minuteDuration
    newHour = hour + hourDuration
    pastDays = 0
    if 12 < newHour < 24:
        if(newHour!= 12):
            newHour = newHour - 12
        if (mode == "AM"):
            mode = "PM"
        else:
            mode = "AM"
            pastDays = pastDays + 1 
            
    if(newHour > 24):
        pastDays = pastDays + math.floor(newHour / 24)
        newHour =  newHour % 24 
    if newMinute > 60 : 
        newMinute = newMinute - 60
        newHour = newHour + 1

    if 12 <= newHour < 24:
        if(newHour!= 12):
            newHour = newHour - 12 
        if (mode == "AM"):
            mode = "PM"
        else:
            mode = "AM"
            pastDays = pastDays + 1 


    newTime = str()
    print(start +" "+ str(pastDays))
    if(newMinute < 10):
        newTime = newTime + str(newHour)+":"+"0"+str(newMinute)+" "+mode
    else:
        newTime = str(newHour)+":"+str(newMinute)+" "+mode
    
    if(pastDays == 0):
        return(newTime)
    if(pastDays == 1):
        return(newTime+" (next day)")
    if(pastDays > 1 ):
        return(newTime+" ("+str(pastDays)+" days later)")

    #return new_time
    
