import os
import csv
import string
import random

def pause():
    pause = raw_input("Press any key to continue. . .")
    
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

Status = True    

#Pack Default"
Actor = "Xic0"
Robot = "Lolita"
msgIdle = ["...", "Nothing to say, eh?", "Yeah! Me too...", "?!?", "What?", "Meh!", "Bah!", "Why don't you speak to me?", "Type !help already!!!", "OMG!", "Do you know Miranda?", "As if..."]

#Pack Borg#
#Actor = "Drone"
#Robot = "The Colective"
#msgIdle = ["Resistence is futile!", "You're being assimilated!", "Join the colective", "You're 1of9... and I'm 1 of a kind!", "This is Unimatrix 001, do you like it, neo?"]

#Pack StarWars#
#Actor = "Young Skywalker"
#Robot = "Yoda"
#msgIdle = ["Use the force!", "Tired of this nonsense you will...", "What? I'm a Jedi. Not a fucking mind reader...", "ready you're not this program to use", "Hmmm?", "Darth Vader says Yoda stinks!!!", "bip, blip. bip. bip. blip. blip... Yes! R2D2 is telling you to fuck off!"]

#Pack StarGate#
#Actor = "SGC Trainee"
#Robot = "Morgan LeFay"
#msgIdle = ["Indeed!", "Kree!", "Indeed you are...", "It's Supreme Commander for you...", "I'm just a hologram... (sou mesmo falsa!)", "Hey, guess what? Daniel died again!", "Quick, dial the gate!"]


### Start ###
banner()
print Robot + ": Please type !help if you need assistance.\n"

while (Status == True):
    query = raw_input(Actor + ": ")
    if (len(query) == 0):
        print Robot + ": " + random.choice(msgIdle) + "\n"
    elif (query == "!help"):
        print "Help!"
    elif (query == "!clear"):
        if (os.name == "nt"):
            os.system("cls")
        else:
            os.system("clear")
        banner()
    elif (query == "!dig"):
        print "[Beta Feature] DiG Service\n"
        qDig = raw_input("DiG: ")
        cmdDig = "dig " + qDig + " ANY IN | more"
        if (os.name == "nt"):
            os.system(cmdDig)
        else:
            os.system(cmdDig)
    elif (query == "!uptime"):
        print "\n"
        if (os.name == "nt"):
            os.system('SYSTEMINFO | FIND /I "Up Time"')
        else:
            os.system("uptime")
        print "\n"
    elif (query == "!vaca"):
        print Robot + ": Moo!!! :)\n"
    elif (query == "!slap"):
        print "\n[ACTiON] " + Actor + " Bitchslaps " + Robot +" in the face!"
        print "\n[ACTiON] " + Robot + " slaps " + Actor + " around with a large trout!.\n"
    elif (query == "!quit"):
        print Robot + ": Bye!!"
        Status = False
    elif (query == "!call"):
        print Robot + ": Call who?"
        qCall = raw_input(Actor + ": ")
        print Robot + ": Who's " + qCall + "?"
    else:
        print dbSearch(query)
