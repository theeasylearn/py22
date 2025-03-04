from datetime import datetime 
def getDate(): #dd-mm-YYYY
    date = datetime.now() 
    dmy = date.strftime("%d-%m-%Y")   
    return dmy 
def getTime(): #hh:mm:ss
    date = datetime.now()
    time = date.strftime("%H:%M:%S")
    return time 
