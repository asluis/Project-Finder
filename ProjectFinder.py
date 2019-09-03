#This program was made by Luis Alvarez

import re
import sys
import imapclient
import pyzmail
import smtplib


emailPassword = "REDACTED"
emailUsername = "asluisinfo@gmail.com"
workEmail = "REDACTED"


#Establishes a connection with the domain of the email
server = imapclient.IMAPClient("imap.gmail.com", ssl = True)

#Logs in to a specific acc that matches the connection we made above
server.login(emailUsername, emailPassword)


#Specifies the specific folder within the email we want to access
selectInfo = server.select_folder("INBOX")

#Shows us how many messages are in the inbox
print("%d messages in inbox" % selectInfo[b'EXISTS'])


#Gives us a list of unique IDs for each email received from a specific sender
UIDs = server.search(["FROM", workEmail])
print(UIDs)
#Returns a list of unique IDs from a specific sender


myUID = selectInfo[b'EXISTS']


#Returns a specific email (thru its UID) as gibberish unreadable by humans
rawMsg = server.fetch([myUID], ["BODY[]", "FLAGS"])
rawMsg



#Gives us a version of the unreadable gibberish of a specific email (thru UID)
pyzMsg = pyzmail.PyzMessage.factory(rawMsg[myUID][b'BODY[]'])
pyzMsg







#this returns a
#normal string, although it still has a lot of escape characters
message = pyzMsg.text_part.get_payload().decode("UTF-8")
print("Message = " + str(message))





#=======Processing/parsing text seection========






projectRegex = re.compile(r"""
(
(\#  \d{1,2}  \s  \(   \w{1,3}   \)   )
( ([^.])? (.+)? ){3,5}
)
""", re.VERBOSE)



rawProjectsList = projectRegex.findall(message) #Creates a multideimensional list
                                                                #that contains a list of projects
                                                                #and each project has its components split up
        #First group (item/element) contains entire project listing
print(str(rawProjectsList))
print(len(rawProjectsList)) #Prints number of projects available

cleanProjList = []
for i in range(0, len(rawProjectsList)):
    cleanProjList.append(rawProjectsList[i][0])

#The for loop above cleans up the list to ONLY contain complete project details,
    #not complete project details AND the same project details split up into different
    #items within the list
#Now each individual entry is a complete project and can be parsed for location
    #each entry is now something that can be sent as an email without any editing of
    #the entry
    #An entry will be sent as an email if it matches my list of work-able locations

print("========CLEAN===========")

print(str(cleanProjList))



#============================================================
#Creates a separate location list with a valid location
locationRegex = re.compile(r"""

(
\s?Los\sGatos\s?
|
\s?Campbell\s?
|
\s?Milpitas\s?
|
\s?Mountain\sView\s?
|
\s?Morgan\sHill\s?
|
\s?Gilroy\s?
|
\s?Sunnyvale\s?
|
\s?Menlo\sPark\s?
|
\s?Palo\sAlto\s?
|
\s?Stanford\s?
|
\s?Redwood\sCity\s?
|
\s?Scotts\sValley\s?
|
\s?Pleasanton\s?
|
\s?Newark\s?
|
\s?Union\sCity\s?
)


""", re.VERBOSE)



#Creates a list that shows which entries in the cleanProjList have valid locations
#0 = not a valid location, 1 = valid location
locationIndex = []
validProjList = []
for i in range(0, len(cleanProjList)):
    locMatch = locationRegex.search(str(cleanProjList[i]))
    if locMatch == None:
        locationIndex.append(0)
    else:
        locationIndex.append(1)


#Exits program if no project is in a suitable location
if len(cleanProjList) == 0:
    print("\nTHERE ARE NO SUITABLE PROJECTS.\nExiting program...")
    server.logout()
    sys.exit()

print("\n=====HERE ARE THE VALID LOCATIONS:=====\n")
print("Which project would you like? Enter a number from 1 to whatever\n\
the maximum number of projects there are. \nPLEASE NOTE:\n\
Do NOT enter the project number. Numbering starts at 1 from top to bottom.")

#Prints valid projects
for i in range(0, len(locationIndex)):
    if locationIndex[i] == 1:
        print("\n")
        print(str(cleanProjList[i]))
        validProjList.append(cleanProjList[i])



print("Which project would you like to go to? Enter 0 for none of the above")

answer = str(input())
stop = False;

while True:
    if answer.isdigit() == False:
        answer = str(input("Try again, enter a number:\n"))
        continue
    elif int(answer) > len(validProjList):
        answer = str(input("Try again, enter a number:\n"))
        continue;
    elif int(answer) == 0:
        stop = True
        break;
    else:
        break;

#This is done to match the index of the list
answer = int(answer) - 1
if stop == False:
    print("You chose number: " + str((answer + 1)) + " which is this project:\n")
    print(validProjList[answer])
else:
    print("You did not choose a project.")
    server.logout()
    sys.exit() #Exits if user says none
    

print("\n=============Response==============\n")



#==============Crafting a response section===================



response = "Hello,\n\nI am interested in the following job opportunity:\n" + validProjList[answer] + "\n\nThanks.\n\n" 
signature = "- Luis"
response+= signature
print(response)
    
response = response.encode("utf-8")

#===========Sending Message============

outServer = smtplib.SMTP("smtp.gmail.com", 587)
outServer.ehlo()
outServer.starttls()
outServer.login(emailUsername, emailPassword)


outServer.sendmail(emailUsername, workEmail,  response)











