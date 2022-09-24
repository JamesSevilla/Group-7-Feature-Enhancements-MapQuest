#Import Dependencies
from tkinter import *
import urllib.parse
import requests

#Initialize Import
root = Tk()
root.title("Map Quest")

#Main Function of the Program
def mapQuest():
    outputBox = Toplevel()
    #Api and key for URL Access
    main_api = "http://www.mapquestapi.com/directions/v2/route?"
    key = "ptA1mBi4uz4PZtAhPot62IBhPZEqFd6j"
    url = main_api + urllib.parse.urlencode({"key":key, "from":sourceCity.get(), "to":destinationCity.get()})
    #Print URL Used
    urlLabel = Label(outputBox, text=("URL ", (url)))
    urlLabel.grid(row=7,column=1)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        #Print if Successful route Call
        successLabel = Label(outputBox,text=("API Status: " + str(json_status) + " = A successful route call.\n"))
        successLabel.grid(row=8,column=1)
        #Divider
        equalLine = Label(outputBox,text="=============================================")
        equalLine.grid(row=9,column=1)
        #Print the Original Position
        dirFrom = Label(outputBox,text=("Directions from " + (sourceCity.get()) + " to " + (destinationCity.get())))
        dirFrom.grid(row=10,column=1)
        #Print the Trip Duration
        tripDuration = Label(outputBox, text=("Trip Duration: " + (json_data["route"]["formattedTime"])))
        tripDuration.grid(row=11,column=1)
        #Print the Kilometers
        kilometers = Label(outputBox, text=("Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))))
        kilometers.grid(row=12, column=1)
        #Print the Fuel Used
        fuelUsed=Label(outputBox,text=("Fuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))))
        fuelUsed.grid(row=13,column=1)
        #Divider
        equalLine1 = Label(outputBox,text="=============================================")
        equalLine1.grid(row=14,column=1)
        #Initialize i for looping
        i=15
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            i+=1
            #Print the direction steps
            direction = Label(outputBox,text=((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")))
            direction.grid(row=i,column=1)
        
    elif json_status == 402:
        #Divider
        astLine = Label(outputBox,text="**********************************************")
        astLine.grid(row=8,column=1)
        #Print Status COde
        statusCode = Label(outputBox,text=("Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations."))
        statusCode.grid(row=9,column=1)
        #Divider
        astLine1 = Label(outputBox,text="**********************************************")
        astLine1.grid(row=10,column=1)
    elif json_status == 611:
        #Divider
        astLine = Label(outputBox,text="**********************************************")
        astLine.grid(row=8,column=1)
        #Print Status COde
        statusCode = Label(outputBox,text=("Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations."))
        statusCode.grid(row=9,column=1)
        #Divider
        astLine1 = Label(outputBox,text="**********************************************")
        astLine1.grid(row=10,column=1)
    else:
        #Divider
        astLine = Label(outputBox,text="**********************************************")
        astLine.grid(row=8,column=1)
        #Print Status COde
        statusCode = Label(outputBox,text=("For Status Code: " + str(json_status) + "; Refer to:"))
        statusCode.grid(row=9,column=1)
        urlHelp = Label(outputBox,text="https://developer.mapquest.com/documentation/directions-api/status-codes")
        urlHelp.grid(row=10,column=1)
        #Divider
        astLine1 = Label(outputBox,text="**********************************************")
        astLine1.grid(row=11,column=1)
    #Close
    closeButton = Button(outputBox, text="Close", padx=50, command=outputBox.destroy)
    closeButton.grid(row=i+1,column=1)
    

#Program Title
mapQuestT = Label(root, text="MAP QUEST")
mapQuestT.grid(row=0,column=1)


#Blank Space
blankSpace = Label(root, text=" ")
blankSpace.grid(row=3,column=0)
blankSpace.grid(row=5,column=0)

#Source City Input
sourceCityLabel = Label(root, text="Source City") #Label
sourceCityLabel.grid(row=1,column=0)
sourceCity = Entry(root, width=30) #Input Field
sourceCity.grid(row=1,column=1)


#Destination City Input
destinationCityLabel = Label(root, text="Destination City")
destinationCityLabel.grid(row=2,column=0)
destinationCity = Entry(root, width=30)
destinationCity.grid(row=2,column=1)

#Go to MapQuest
myButton = Button(root, text="View", padx=50, command=mapQuest)
myButton.grid(row=4,column=1)

#Exit Button
exitButton = Button(root, text="Exit Program", padx=50, fg="red", command=root.quit)
exitButton.grid(row=6,column=1)

root.mainloop()


