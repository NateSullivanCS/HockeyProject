import os
import sys
import cmd
import csv
from tkinter import *
from tkinter import filedialog
import warnings #Used to ignore deprication warnings, mostly in TK

warnings.filterwarnings("ignore", category=DeprecationWarning) # Not working


#Prints output of where user is in PC (Absolute Pathname)
print(sys.argv)

#TODO: Define player class that stores all variables 
    #Defines the player structure, arrays of variables stored in Hockey Catapult CSV.
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



#TODO: Prompt User to import a file 
    # Store other variables such as date, see if data in spreadsheets match 

#Method used by Tk to store file thats scanned by CSV scanner
def openFile():
    global file
    filepath = filedialog.askopenfilename()
    file = filepath

#See the global 'file' variable that user imports
def printFile():
    print(file)

# Used to get import from user
window = Tk()
Button = Button(text="Select File", command=openFile)
Button.pack()
window.mainloop()

# Used to test & see the file that the user imported, is it stored correctly?
print("\nShould be here: ")
print(printFile())



# Very primitive, find a different method to enter later.
#USE THIS: "/Users/natesullivan/Desktop/Hockey Catapult Project/Coding/catapultexportex.csv"
#file = input("Please select the path of the CSV file to input: ")
#print("You entered: " + file)


#TODO: Scan CSV File
    # Store allData in array.
    # For each player in first row, create a new unique player object

#Basically takes a string form of the absolute path of the file destination and scans that as a CSV.
with open(file, 'r') as infile:
    rows = csv.reader(infile, delimiter=',')
    header = next(rows)
    allData = []

    for row in rows:
        allData.append(row)


 #Initialize Blank Player Objects
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()
player7 = Player()
player8 = Player()
player9 = Player()
player10 = Player()
player11 = Player()
player12 = Player()
player13 = Player()
player14 = Player()
player15 = Player()
player16 = Player()
player17 = Player()
player18 = Player()
player19 = Player()
player20 = Player()
player21 = Player()
player22 = Player()
player23 = Player()
player24 = Player()
player25 = Player()
player26 = Player()
player27 = Player()
player28 = Player()
player29 = Player()
player30 = Player()
player31 = Player()
player32 = Player()

#There are going to be blank player objects, but this is fine for now
playerList = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16, player17, player18, player19, player19, player20, player21, player22, player23, player24, player25, player26, player27, player28, player29, player30, player31, player32]


for row in allData:
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

#TODO: Go through all data and store variables in the player object
i = 0;
for obj in playerNames:
    playerList[i].name = playerNames[i]
    playerList[i].playerLoad = playerLoads[i]
    playerList[i].playerLoadMin = playerLoadsMin[i]
    playerList[i].workingPl = workingPlayerLoads[i]
    playerList[i].workingPlMin = workingPlayerLoadsMin[i]
    playerList[i].expEffAvg = explosiveEfforts[i]
    playerList[i].expRatio = explosiveRatio[i]
    playerList[i].skatingLoad = skatingLoads[i]
    playerList[i].pBand1Fs = band1Force[i]
    playerList[i].pBand2Fs = band2Force[i]
    playerList[i].pBand3Fs = band3Force[i]
    playerList[i].skatingLoadMin = skatingLoadMin[i]
    i = i + 1





#Testing Outputs for player structures.
print(player13.name)
print(player13.skatingLoad)
print(player25.skatingLoad)
print(player25.name)


running = 1

#while (running):
   # print("Here are the options for the CSV interface")
    # Basically, we can do a very similar format to the Clue Game from CS230
    # If user types 'end'. Set running int to 0
    # If user types 'import'. prompt the user to imput another practice
    # If user types 'average', prompt user to see averages of all practices from the imputted data, (GO TO B TO GET MORE EQUATIONS THAT HE USES)
    # If user types 'export', export to: spreadsheets? pdf of averages for each player? lots of possibilities
    # If user types 
    




# POSSIBLE FUNCTIONALITIES

    #1) Find Averages of CSV 
      # - We can do this for multiple CSV files, finding the averages of the specific 
      # - Have user input dates, store that data somewhere in a concatanted string, and put that on top of a new CSV file.
    #2) Export a spreadsheet of data comparing the players by a variable.
      # - "Select varaibles and players you would like to compare or practices"
    #3) -

