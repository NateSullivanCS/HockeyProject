import os
import sys
import cmd
import csv
from fpdf import *
from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

playerTotalArray = []

# Removes extra players from files that aren't in the first one.
def checkIfInOriginal(filePlayer, USETOTALPLAYERARRAY):
    booleanCheckForMatch = False
    for obj in USETOTALPLAYERARRAY:
        if filePlayer.name == obj.name:
            booleanCheckForMatch = True
        else:
            doNothing
    return booleanCheckForMatch

def getIndivIntensityAverage(USEPLAYERTOTALARRAY, index):
    if (index >= len(USEPLAYERTOTALARRAY)):
        return 0
    else:
        playerAtIndexIntensityAvg = USEPLAYERTOTALARRAY[index].playerLoad / 7 # or fileIndex
        return playerAtIndexIntensityAvg

def teamIntensityAverage(USEPLAYERTOTALARRAY): 
    numPlayers = 0
    totalNumerator = 0
    individualIntensity = 0
    for obj in USEPLAYERTOTALARRAY:
        individualIntensity = float(obj.playerLoad) / 7 
        totalNumerator = totalNumerator + float(individualIntensity)
        numPlayers = numPlayers + 1
    teamIntensityAverage = totalNumerator / numPlayers
    return teamIntensityAverage

def getIndivLoadAverage(USEPLAYERTOTALARRAY, index):
    if (index >= len(USEPLAYERTOTALARRAY)):
        return 0
    else:
        print(float(USEPLAYERTOTALARRAY[index].playerLoadMin))
        playerAtIndexLoadAvg = USEPLAYERTOTALARRAY[index].playerLoadMin / 7
        print(float(playerAtIndexLoadAvg))
        return playerAtIndexLoadAvg

def teamLoadAverage(USEPLAYERTOTALARRAY):
    numPlayers = 0
    totalNumerator = 0
    indivLoadAvg = 0
    for obj in USEPLAYERTOTALARRAY:
        indivLoadAvg = float(obj.playerLoadMin) / 7 
        totalNumerator = totalNumerator + float(indivLoadAvg)
        numPlayers = numPlayers + 1
    teamLoadAverage = totalNumerator / numPlayers
    return teamLoadAverage





## To Turn into Executable File (DO AT END: https://www.youtube.com/watch?v=bqNvkAfTvIc&t=38s)
####################### INITIALIZING GENERAL VARIABLES

def doNothing():
    doNothing = 0


#Prints output of where user is in PC (Absolute Pathname)
print("\n")
print("PRINTING SYSTEM ARGUMENTS:")
print(sys.argv)
print("SYSTEM ARGUMENTS PRINTED.\n")
global fileIndex
fileIndex = 0
playerLoad = 0
playerLoadMin = 0



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
    def playerStructArray(allPlayerData):
        playerStructureArray = playerStructureArray
    

class PlayerTotals:
        myPlArray = []
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




# Variables each have their own array indexing at the specific player
players = []

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

# Variable only used for playerTotalsArray
playerMonotony = []


files = []
global file
file = 'NULL'

####################### END OF INITIALIZATION

def generalMethod(): #Working if command = generalMethod
    print("testing general method")

def checkIfCSV(file):
    charsToMatch = ('c', 's', 'v')
    if (file.endswith(charsToMatch) == 0):
        print("MUST ENTER CSV FILE!")
        return 0



# BUTTON 1 -->
def uploadFile():
    charsToMatch = ('c', 's', 'v') #USED TO SEE IF FILE IS CSV
    filepath = filedialog.askopenfilename()
    file = filepath
    global fileIndex

    newFile, oldExtension = os.path.splitext(file) #New File is what we save the file
    ### CHECKS IF FILE IS CSV, IF NOT WE RETURN TO MAIN PROGRAM AND BREAK FROM FUNCTIOJN
    if ((checkIfCSV(file) == 0)):
        return # RETURN IN THIS CASE BREAKS FROM THE FUNCTION
    ### END CHECK CSV

    files.append(PracticeCSV()) #Adds new File Structure to file array.

    files[fileIndex].name = newFile
    print(files[fileIndex].name)

    
    #Variables for all those players that were just initialized.
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



    with open(file, 'r') as infile:
        rows = csv.reader(infile, delimiter=',')
        header = next(rows)
        allData = []

        for row in rows:
            allData.append(row)

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

    players = []
    playLength = len(playerNames)
    print(playLength)
    for i in range(playLength): #Initializing all players that the file will Store
        players.append(Player())

    i = 0;
    for obj in playerNames:
        print(obj)
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

    files[fileIndex].playerStructArray = players
    print("FILE UPLOAD SUCCESSFUL!")
    fileIndex = fileIndex + 1
    print(fileIndex)

# BUTTON 2 -->
def average(): 
    print("Averaging Data... Generating Documentation...")

    numOfPlayersInFirstFile = 0
    for obj in files[0].playerStructArray:
        numOfPlayersInFirstFile = numOfPlayersInFirstFile + 1

    for i in range(numOfPlayersInFirstFile): #Initializing all players that the file will Store
        playerTotalArray.append(PlayerTotals())

    indexingPlayerTotalArray = 0
    for obj in playerTotalArray:
        playerTotalArray[indexingPlayerTotalArray].name = files[0].playerStructArray[indexingPlayerTotalArray].name
        playerTotalArray[indexingPlayerTotalArray].playerLoad = float(files[0].playerStructArray[indexingPlayerTotalArray].playerLoad)
        playerTotalArray[indexingPlayerTotalArray].playerLoadMin = float(files[0].playerStructArray[indexingPlayerTotalArray].playerLoadMin)
        playerTotalArray[indexingPlayerTotalArray].workingPl = float(files[0].playerStructArray[indexingPlayerTotalArray].workingPl)
        playerTotalArray[indexingPlayerTotalArray].workingPlMin = float(files[0].playerStructArray[indexingPlayerTotalArray].workingPlMin)
        playerTotalArray[indexingPlayerTotalArray].expEffAvg = float(files[0].playerStructArray[indexingPlayerTotalArray].expEffAvg)
        playerTotalArray[indexingPlayerTotalArray].expRatio = float(files[0].playerStructArray[indexingPlayerTotalArray].expRatio)
        playerTotalArray[indexingPlayerTotalArray].skatingLoad = float(files[0].playerStructArray[indexingPlayerTotalArray].skatingLoad)
        playerTotalArray[indexingPlayerTotalArray].pBand1Fs = float(files[0].playerStructArray[indexingPlayerTotalArray].pBand1Fs)
        playerTotalArray[indexingPlayerTotalArray].pBand2Fs = float(files[0].playerStructArray[indexingPlayerTotalArray].pBand2Fs)
        playerTotalArray[indexingPlayerTotalArray].pBand3Fs = float(files[0].playerStructArray[indexingPlayerTotalArray].pBand3Fs)
        playerTotalArray[indexingPlayerTotalArray].skatingLoadMin = float(files[0].playerStructArray[indexingPlayerTotalArray].skatingLoadMin)
        indexingPlayerTotalArray = indexingPlayerTotalArray + 1

    for obj in files[1:]:
        fileIt = obj
        for obj in fileIt.playerStructArray:
            booleanVal = True
            booleanVal = checkIfInOriginal(obj, playerTotalArray)
            if booleanVal is False:
                fileIt.playerStructArray.remove(obj)
    # Fixed to find playerTotals
    for obj in files[1:]:
        filesN = obj
        for obj in filesN.playerStructArray:
            playerObject = obj #PlayerObject is the object in the player array of current file being scanned
            for obj in playerTotalArray: #Obj in this case is the Player in PlayerTotalsArray
                playerTotalArrayObject = obj
                if (playerTotalArrayObject.name == playerObject.name):
                    obj.playerLoad = float(obj.playerLoad) + float(playerObject.playerLoad)
                    obj.playerLoadMin = float(obj.playerLoadMin) + float(playerObject.playerLoadMin)
                    # You must initialize all other variables.   
                else:
                    doNothing

# BUTTON 3 -->
def exportPDF():
    print("Analytics Report Created!")
    names = []
    position = []
    barsForIndivLoad = []
    barsForIndivIntense = []
    indexingBars = 0
    positionsNum = 0
    for obj in playerTotalArray:
        barsForIndivLoad.append(float(getIndivLoadAverage(playerTotalArray, indexingBars)))
        barsForIndivIntense.append(float(getIndivIntensityAverage(playerTotalArray, indexingBars)))
        names.append(obj.name)
        position.append(positionsNum)
        positionsNum = positionsNum + 1
        indexingBars = indexingBars + 1

    fg = plt.figure(figsize=(7,5))
    plt.bar(position, barsForIndivLoad, width = .9, color = "red")
    plt.xticks(position, names)
    plt.xticks(rotation = 90)
    plt.xticks(fontsize=5, fontweight='bold')
    fg.savefig("1stplot.png")

    fg2 = plt.figure(figsize=(7,5))
    plt.bar(position, barsForIndivIntense, width = .9, color = "red")
    plt.xticks(position, names)
    plt.xticks(rotation = 90)
    plt.xticks(fontsize=5, fontweight='bold')
    fg2.savefig("2ndplot.png")
    print((getIndivLoadAverage(playerTotalArray, 1)))
    # Create a new PDF document


    pdf = FPDF()
    pdf.add_page(orientation = 'P', format = 'A4')    # Set the font and font size for the page title
    pdf.set_font('Arial', 'B', 24)
    # Calculate the width of the page title
    title_width = pdf.get_string_width('UMASS HOCKEY ANALYSIS')
    # Calculate the x-coordinate of the page title
    # Print the page title
    pdf.cell(195, 5, 'UMASS HOCKEY ANALYSIS', 0, 1, 'C')


    # Set the font and font size for the subheading
    pdf.set_font('Arial', 'B', 16)
    # Print the subheading
    pdf.cell(0, 10, 'FROM PRACTICES:', ln=1)
    # Set the font and font size for the file names
    # Iterate through the 'files' array
    pdf.set_font('Arial', 'I', 12)
    for file in files:
        # Print the file name
        pdf.cell(0, 10, file.name, ln=2)
        # Save the PDF document
    
    #Page 2
    pdf.add_page(orientation = 'P', format = 'A4')   # Set the font and font size for the page title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(195, 10, "Weekly Player Load Average", 0, 1, 'C')
    pdf.image('1stplot.png',  w=175, h=175)
    
    #Page 3
    pdf.add_page(orientation = 'P', format = 'A4')   # Set the font and font size for the page title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(195, 10, "Weekly Intensity Average", 0, 1, 'C')
    pdf.image('2ndplot.png',  w=175, h=175)

    
    pdf.output('TestAnalysis.pdf')

# BUTTON 4 -->
def reset():
    myResetLabel = Label(text="RESETTING DATA ...", font=("Helvetica", 32, "bold"), fg="red", bg="black")
    myResetLabel.place(x = 270, y = 100)
    # Schedule the label to be removed after 3 seconds
    myResetLabel.after(1500, myResetLabel.destroy)
    playerTotalArray = []
    names = []
    position = []
    bars = []
    indexingBars = 0
    positionsNum = 0
    indexingPlayerTotalArray = 0
    numOfPlayersInFirstFile = 0
    players = []
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
    files = []
    global file
    file = 'NULL'

# BUTTON 5 --> 
def help():
    print("Heres how to use the Massachusettes Hockey Interface:")
    print("Blahblahblah")

# BUTTON 6 -->
def endProgram():
    root.destroy()
#Just get as much basic shit down as possible. 
root = Tk()
root.configure(bg="gray")
root.geometry('768x432')
root.title("Massachusetts Hockey Performance")

# Create a PhotoImage object
image = PhotoImage(file="1200px-UMass_Amherst_Athletics_logo.svg.PGM")
# Create a label with the image
label = Label(root, image=image, bg="gray")
# Set the image as the background of the label
label.image = image
# Add the label to the GUI
label.pack()


# Initialize Buttons
importbtn = Button(root, text='IMPORT FILE', bd='.5', command=uploadFile, font=("Helvetica", 12, "bold"), bg="white")
averagebtn = Button(root, text='AVERAGE', bd='.5', command=average, font=("Helvetica", 12, "bold"), bg="white")
exportbtn = Button(root, text='EXPORT', bd='.5', command=exportPDF, font=("Helvetica", 12, "bold"), bg="white")
resetbtn = Button(root, text='RESET DATA', bd='.5', command=reset, font=("Helvetica", 12, "bold"), bg="white")
helpbtn = Button(root, text='HELP', bd='.5', command=help, font=("Helvetica", 12, "bold"), bg="white")
exitbtn = Button(root, text='EXIT', bd='.5', command=endProgram, font=("Helvetica", 12, "bold"), bg="white")

# Set the position of the buttons 
importbtn.place(x=190, y=200)
averagebtn.place(x=340, y=200)
exportbtn.place(x=490, y=200)
resetbtn.place(x=190, y=275)
helpbtn.place(x=340, y=275)
exitbtn.place(x=490, y=275)

# Add a title label
#HockeyLabel = Label(root, text="UMASS HOCKEY PERFORMANCE", font=("Helvetica", 24, "bold"), fg="red", bg="gray")
#HockeyLabel.pack(pady=95)

print("-------> GUI Loop Still Running <-------")
root.mainloop() # This runs until mainloop is ended or "destroyed"


