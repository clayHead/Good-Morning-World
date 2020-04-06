from datetime import date

# Help from https://www.programiz.com/python-programming/datetime/current-datetime

goodMorning = "Good Morning World!"
date = 0

def formatDate():
    date = date.today()
    return date.strftime("%B %d, %Y")

def getString():
    return goodMorning + " Today is " + formatDate()
