#Front-End Imports
from pathlib import Path
from tkinter import *

#MapQuest Imports
import urllib.parse
import requests

#Fix PATHS
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

#Return ASSETS_PATH Function
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Main Function of the Program with KM
def mapQuest():
    outputBox = Toplevel()
    #Api and key for URL Access
    main_api = "http://www.mapquestapi.com/directions/v2/route?"
    key = "ptA1mBi4uz4PZtAhPot62IBhPZEqFd6j"
    url = main_api + urllib.parse.urlencode({"key":key, "from":entry_1.get(), "to":entry_2.get()})
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
        dirFrom = Label(outputBox,text=("Directions from " + (entry_1.get()) + " to " + (entry_2.get())))
        dirFrom.grid(row=10,column=1)
        #Print the Trip Duration
        tripDuration = Label(outputBox, text=("Trip Duration: " + (json_data["route"]["formattedTime"])))
        tripDuration.grid(row=11,column=1)
        #Print the Kilometers
        kilometers = Label(outputBox, text=("Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"]*1.6))))
        kilometers.grid(row=12, column=1)
        #Print the Fuel Cost
        fuelCost = Label(outputBox, text=("Estimated Fuel Cost: ₱" + str("{:.2f}".format(((json_data["route"]["distance"])/25)*268))))
        fuelCost.grid(row=13, column=1)
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

#Main Function of the program with Miles
def mapQuestMiles():
    outputBox = Toplevel()
    #Api and key for URL Access
    main_api = "http://www.mapquestapi.com/directions/v2/route?"
    key = "ptA1mBi4uz4PZtAhPot62IBhPZEqFd6j"
    url = main_api + urllib.parse.urlencode({"key":key, "from":entry_1.get(), "to":entry_2.get()})
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
        dirFrom = Label(outputBox,text=("Directions from " + (entry_1.get()) + " to " + (entry_2.get())))
        dirFrom.grid(row=10,column=1)
        #Print the Trip Duration
        tripDuration = Label(outputBox, text=("Trip Duration: " + (json_data["route"]["formattedTime"])))
        tripDuration.grid(row=11,column=1)
        #Print the Kilometers
        kilometers = Label(outputBox, text=("Miles: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6 * 0.62137119))))
        kilometers.grid(row=12, column=1)
        #Print the Fuel Cost
        fuelCost = Label(outputBox, text=("Estimated Fuel Cost: ₱" + str("{:.2f}".format(((json_data["route"]["distance"])/25)*268))))
        fuelCost.grid(row=13, column=1)
        #Divider
        equalLine1 = Label(outputBox,text="=============================================")
        equalLine1.grid(row=14,column=1)
        #Initialize i for looping
        i=15
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            i+=1
            #Print the direction steps
            direction = Label(outputBox,text=((each["narrative"])))
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
#Main Function of the program with Miles
def mapQuestMeters():
    outputBox = Toplevel()
    #Api and key for URL Access
    main_api = "http://www.mapquestapi.com/directions/v2/route?"
    key = "ptA1mBi4uz4PZtAhPot62IBhPZEqFd6j"
    url = main_api + urllib.parse.urlencode({"key":key, "from":entry_1.get(), "to":entry_2.get()})
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
        dirFrom = Label(outputBox,text=("Directions from " + (entry_1.get()) + " to " + (entry_2.get())))
        dirFrom.grid(row=10,column=1)
        #Print the Trip Duration
        tripDuration = Label(outputBox, text=("Trip Duration: " + (json_data["route"]["formattedTime"])))
        tripDuration.grid(row=11,column=1)
        #Print the Kilometers
        kilometers = Label(outputBox, text=("Meters: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6 * 1000))))
        kilometers.grid(row=12, column=1)
        #Print the Fuel Cost
        fuelCost = Label(outputBox, text=("Estimated Fuel Cost: ₱" + str("{:.2f}".format(((json_data["route"]["distance"])/25)*268))))
        fuelCost.grid(row=13, column=1)
        #Divider
        equalLine1 = Label(outputBox,text="=============================================")
        equalLine1.grid(row=14,column=1)
        #Initialize i for looping
        i=15
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            i+=1
            #Print the direction steps
            direction = Label(outputBox,text=((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61*1000) + " Meters)")))
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

#Initialize Window
window = Tk()

#Edit Window Design
window.geometry("740x524")
window.configure(bg = "#FFFFFF")
window.title("Map Quest")

#Background Image
canvas = Canvas(window, bg = "#FFFFFF", height = 524, width = 740, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(369.86492919921875,261.97845458984375,image=image_image_1)

#Source City Input
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(454.5,262.75,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
entry_1.place(x=348.0,y=252.0,width=213.0,height=19.5)

#Destination City
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(454.5,306.75,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
entry_2.place(x=348.0,y=296.0,width=213.0,height=19.5)

#View Button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=mapQuest,relief="flat")
button_1.place(x=201.0,y=345.0,width=153.0,height=37.0)

#View Button
button_image_M = PhotoImage(file=relative_to_assets("button_3.png"))
button_M = Button(image=button_image_M,borderwidth=0,highlightthickness=0,command=mapQuestMiles,relief="flat")
button_M.place(x=386.0,y=345.0, width=153.0,height=37.0)

#View Button
button_image_Me = PhotoImage(file=relative_to_assets("button_4.png"))
button_Me = Button(image=button_image_Me,borderwidth=0,highlightthickness=0,command=mapQuestMeters,relief="flat")
button_Me.place(x=284.0,y=397.0, width=153.0,height=37.0)

#Exit Button
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=window.quit,relief="flat")
button_2.place(x=284.0,y=449.0,width=153.0,height=37.0)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(369.1875,176.0,image=image_image_2)

#Source City Label
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(269.0, 262.25,image=image_image_3)

#Destination City Label
image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(261.0,300.0,image=image_image_4)

#Show Window
window.resizable(False, False)
window.mainloop()
