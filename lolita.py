import os
import csv
import string

def banner():
    print "                             _         _"
    print "                          \_|_)       | | o"
    print "                            |     __  | |   _|_  __,"
    print "                           _|    /  \_|/  |  |  /  |"
    print "                          (/\___/\__/ |__/|_/|_/\_/|_/ v1.5 (DB@01-06-2010)"
    print ""

def dbSearch(squery):
    results = False
    dbReader = csv.reader(open("rge.csv"), delimiter=",")
    for row in dbReader:
        srow = str(row).upper()
        x = srow.find(squery.upper())
        if x != -1:
            results = True
            print srow
    if results == False:
        return Robot + ": '" + squery + "' not found!\n"
    else:
        return Robot + ": Done!\n"

def GetInHMS(seconds):
    hours = seconds / 3600
    seconds -= 3600*hours
    minutes = seconds / 60
    seconds -= 60*minutes
    if hours == 0:
        return "%02dm%02ds" % (minutes, seconds)
    return "%02dh%02dm%02ds" % (hours, minutes, seconds)


Actor = "Xic0"
Robot = "Lolita"
Status = True

### Start ###
banner()
print Robot + ": Please type !help if you need assistance.\n"

while (Status == True):
    query = raw_input(Actor + ":")
    if (query == ""):
        print Actor + ": "
    if (query == "!help"):
        print "Help!"
    elif (query == "!clear"):
        print "Clear!!"
        if (os.name == "nt"):
            os.system("cls")
        else:
            os.system("clear")
        banner()
    elif (query == "!uptime"):
        if (os.name == "nt"):
            os.system('SYSTEMINFO | FIND /I "Up Time"')
        else:
            os.system("uptime")
    elif (query == "!vaca"):
        print "Moo!!!\n"
    elif (query == "!quit"):
        print Robot + ": Bye!!"
        Status = False
    elif (query == "!hms"):
	print Robot + ": Quantos segundos?"
	Seconds = raw_input(Actor + ":")
	print Robot + ": " + GetInHMS(int(Seconds))
    else:
        print dbSearch(query)
