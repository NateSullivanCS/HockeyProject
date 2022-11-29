import os
import sys
import cmd
import csv
from tkinter import *
from tkinter import filedialog
import warnings #Used to ignore deprication warnings, mostly in TK
#Google Spreadsheets



####################### INITIALIZING GENERAL VARIABLES

#Prints output of where user is in PC (Absolute Pathname)
print("\n")
print("PRINTING SYSTEM ARGUMENTS:")
print(sys.argv)
print("SYSTEM ARGUMENTS PRINTED.\n")

# Player Structure takes all variables from CSV export 2022-2023 Season
class Player:
        def __init__(self):
            self = self
        def name(playerName):
            playerName = playerName
        def playerLoad(playerLoad):
            playerLoad = playerLoad
        def playerLoadMin(playerLoadMin):
            playerLoadMin = playerLoadMin
        def workingPl(workingPl):
            workingPl = workingPl
        def workingPlMin(workingPlMin):
            workingPlMin = workingPlMin
        def expEffAvg(expEffAvg):
            expEffAvg = expEffAvg
        def expRatio(expRatio):
            expRatio = expRatio
        def skatingLoad(skatingLoad):
            skatingLoad = skatingLoad
        def pBand1Fs(pBand1Fs):
            pBand1Fs = pBand1Fs
        def pBand2Fs(pBand2Fs):
            pBand2Fs = pBand2Fs
        def pBand3Fs(pBand3Fs):
            pBand3Fs = pBand3Fs
        def skatingLoadMin(skatingLoadMin):
            skatingLoadMin = skatingLoadMin


class PracticeCSV:
    def __init__(self):
        self = self 
    def name(practiceName): # This will be initialized to to the CSV file name but split out the .CSV
        practiceName = practiceName
    def playerStruct(playerStruct):
        playerStruct = playerStruct
    





# Variables each have their own array indexing at the specific player

#TODO: Must do this for all array variables so that we can store multiple files.
playerNames = []
playerLoads = []
playerLoadsMin = []
workingPlayerLoads = []
workingPlayerLoadsMin =[]
explosiveEfforts = []
explosiveRatio = []
skatingLoads = []
band1Force = []
band2Force = []
band3Force = []
skatingLoadMin = []



players = []
for i in range(32):
   players.append(Player())
print(players[0].name)


global file
file = 'NULL'

####################### END OF INITIALIZATION

def generalMethod(): #Working if command = generalMethod
    print("testing general method")

def uploadFile():
    #If Array of Variables is not Null, reset all variables to null. 
    playerNames = []
    playerLoads = []
    playerLoadsMin = []
    workingPlayerLoads = []
    workingPlayerLoadsMin =[]
    explosiveEfforts = []
    explosiveRatio = []
    skatingLoads = []
    band1Force = []
    band2Force = []
    band3Force = []
    skatingLoadMin = []
    filepath = filedialog.askopenfilename()
    file = filepath
    print(file) # Correctly printing File name being read
    with open(file, 'r') as infile:
        rows = csv.reader(infile, delimiter=',')
        header = next(rows)
        allData = []

        for row in rows:
            allData.append(row)

    for row in allData: # THIS NEEDS TO BE CHANGED SO NEW FILE ISNT OVERWRITING EXISTING INFO
        playerNames.append(row[0])
        playerLoads.append(row[1])
        playerLoadsMin.append(row[2])
        workingPlayerLoads.append(row[3])
        workingPlayerLoadsMin.append(row[4])
        explosiveEfforts.append(row[5])
        explosiveRatio.append(row[6])
        skatingLoads.append(row[7])
        band1Force.append(row[8])
        band2Force.append(row[9])
        band3Force.append(row[10])
        skatingLoadMin.append(row[11])

    i = 0;
    for obj in playerNames:
        players[i].name = playerNames[i]
        players[i].playerLoad = playerLoads[i]
        players[i].playerLoadMin = playerLoadsMin[i]
        players[i].workingPl = workingPlayerLoads[i]
        players[i].workingPlMin = workingPlayerLoadsMin[i]
        players[i].expEffAvg = explosiveEfforts[i]
        players[i].expRatio = explosiveRatio[i]
        players[i].skatingLoad = skatingLoads[i]
        players[i].pBand1Fs = band1Force[i]
        players[i].pBand2Fs = band2Force[i]
        players[i].pBand3Fs = band3Force[i]
        players[i].skatingLoadMin = skatingLoadMin[i]
        i = i + 1
    print("FILE UPLOAD SUCCESSFUL!")






#Just get as much basic shit down as possible. 
root = Tk()
root.geometry('500x500')
root.title("Massachusetts Hockey Performance")





massHockeyLabel = Label(text='UMASS HOCKEY PERFORAMANCE *PROTOTYPE*', height = 50, width = 50, fg = 'red', font = 'Helvetica 18 bold').pack()


#Initialize Buttons
importbtn = Button(root, text = 'IMPORT FILE', bd = '20', command = uploadFile)
    #CONSTRAINTS:
        # 1) Only able to upload 1 file at a time.
        # We want each file upload to be stored in its own file structure. Where we can access data from that SPECIFIC csv file.
        #




practicebtn = Button(root, text = 'PRACTICES', bd = '20', command = root.destroy)
    # TODO: 
    


playersbtn = Button(root, text = 'PLAYERS', bd = '20', command = root.destroy)
    # TODO: 
    


exportbtn = Button(root, text = 'EXPORT DATA', bd = '20', command = root.destroy)
    # TODO: 
    


resetbtn = Button(root, text = 'RESET DATA', bd = '20', command = root.destroy)
    # TODO: 
    


exitbtn = Button(root, text = 'EXIT', bd = '20', command = root.destroy)
    # TODO: 
    




# Set the position of the buttons 
importbtn.place(x = 30, y = 200)
practicebtn.place(x = 200, y = 200)
playersbtn.place(x = 360, y = 200)
exportbtn.place(x = 30, y = 275)
resetbtn.place(x = 200, y = 275)
exitbtn.place(x = 360, y = 275)


#Ideas for implementation


#Problems
# 1) 




#End Ideas


print("-------> GUI Loop Still Running <-------")
root.mainloop() # This runs until mainloop is ended or "destroyed"

print("Passes Mainloop of TKINTER GUI") # Runs after end of mainloop
print(players[20].name)
print(players[20].skatingLoad)
print(players[3].skatingLoad)
print(players[3].name)




'''
ERROR WITH UPLOADING 2 FILES TO INTERFACE:
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/Tkinter.py", line 1547, in __call__
    return self.func(*args)
  File "/Users/natesullivan/Desktop/Hockey Catapult Project/Coding/Untitled-1.py", line 148, in uploadFile
    playerList[i].name = playerNames[i]
IndexError: list index out of range





''' 

