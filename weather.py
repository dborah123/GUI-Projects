from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("Learning to Code")
root.iconbitmap('C:/Users/danie/Code/Python/gui/iconEx.ico')
root.geometry("600x100")

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=02494&distance=20&API_KEY=D674E766-B443-449F-ADA0-CAC2E807B21E

#Creating zip code lookup ftn
def zipLookup():
    # zip.get()
    # zipLabel = Label(root, text = zip.get())
    # zipLabel.grid(row = 1, column = 0, columnspan = 2)

    try:
        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() + '&distance=20&API_KEY=D674E766-B443-449F-ADA0-CAC2E807B21E')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if(category == "Good"):
            weather_color = "#0C0"
        elif(category == "Moderate"):
            weather_color = "FFFF00"
        elif(category == "Unhealthy for Sensitive Groups"):
            weather_color = "#ff9900"
        elif(category == "Unhealthy"):
            weather_color = "#FF0000"
        elif(category == "Very Unhealthy"):
            weather_color = "990066"
        elif(category == "Hazardous"):
            weather_color = "#660000"

        root.configure(background = weather_color)

        myLabel = Label(root, text = city + "\tAir Quality: " + str(quality) + " \tCategory: " + str(category), font = ("Helvetica", 10), background = weather_color)
        myLabel.grid(row = 1, column = 0, columnspan = 2)
    except Exception as e:
        api = "Error..."



zip = Entry(root)
zip.grid(row = 0, column = 0, stick = W+E+N+S)

zipButton = Button(root, text = "Lookup Zipcode", command = zipLookup)
zipButton.grid(row = 0, column = 1, stick = W+E+N+S)

root.mainloop()