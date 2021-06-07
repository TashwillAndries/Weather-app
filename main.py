# importing  tkinter and request
from tkinter import *
from tkinter import messagebox
import requests
import requests.exceptions

# setting up tkinter window
app = Tk()
app.title("Weather App")
app.geometry("750x650")
app.config(bg="blue")

# setting up frame
frame = Frame(app, width=500, height=200, highlightthickness=5, highlightbackground="red", highlightcolor="red")
frame.place(x=150, y=170)


# function to get the information from the API
def get_weather():
    try:
        city = city_name.get()
        url = 'https://api.openweathermap.org/data/2.5/weather'
        weather_key = '2fa6c21adb23da2dddb59a678e3c5dbd'
        params1 = {'appid': weather_key, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params1)
        weather = response.json()
        description_label.configure(text='Description: ' + str(weather['weather'][0]['main']))
        temp_label.configure(text='Temperature: ' + str(weather['main']['temp']))
        humidity_label.configure(text='Humidity: ' + str(weather['main']['humidity']))
        wind_speed.configure(text='Wind Speed: ' + str(weather['wind']['speed']))
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "NO internet Connection")

    except ValueError:
        messagebox.showerror("Error", "City cannot be found")

# Clear function
def clear():
    city_name.delete(0, END)
    description_label.config(text="")
    temp_label.config(text="")
    humidity_label.config(text="")
    wind_speed.config(text="")

# exit function
def kill():
    app.destroy()

# Layout for the window
city_name = Entry(app, width=50)
city_name.place(x=200, y=51)
display_btn = Button(app, text="Display Weather", command=get_weather, borderwidth=5, padx=2, pady=2, bg="crimson")
display_btn.place(x=350, y=100)
description_label = Label(frame)
description_label.place(x=50, y=51)
temp_label = Label(frame)
temp_label.place(x=50, y=75)
humidity_label = Label(frame)
humidity_label.place(x=50, y=100)
wind_speed = Label(frame)
wind_speed.place(x=50, y=125)
clear_btn = Button(app, text="Clear", borderwidth=5, padx=2, pady=2, bg="crimson", command=clear)
clear_btn.place(x=150, y=400)
exit_button = Button(app, text="Exit", borderwidth=5, padx=2, pady=2, bg="crimson", command=kill)
exit_button.place(x=600, y=400)
app.mainloop()
