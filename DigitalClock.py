#first import these
from tkinter import *
from time import *

#this is for the updating time later on
def update():
    #strftime is a fucntion that returns the current time in the proper format
    #%I is the hour 12 hr clock
    #%M is the minute
    #%S is the second
    #this will return a string
    #%p is for am pm
    time_string = strftime("%I:%M:%S %p")
    #and we want this time label as text
    time_label.config(text=time_string)

    #this is for the day
    #%A Gives the weekday name
    day_string = strftime("%A")
    #and we want this time label as text
    day_label.config(text=day_string)

    #this is for the date
    #%D is day
    date_string = strftime("%D")
    date_label.config(text=date_string)

    #this is how the time will change
    #this will update every 1000milisecond and we will call the update function so its recrusive
    #we changed to window becuse it will update everything
    window.after(1000, update)

#here we are going to make the window
window = Tk()
window.title("Digital Clock")

#Window size
window.geometry("350x200")
#congif lets you change the widget while it is running
window.config(bg="black")

#this is just displaying the time
#so we have the label and it will be in the window
#in the window our font is Helvetica with size 60 font
#made it bold
#fg is the font color
#the background color is black
time_label = Label(window, font=("Helvetica", 60, "bold"), fg="#00FF00", bg="black")
#always pack
#pady is for spacing from above and below
#the first nubmer is for above the second nubmer is for below
time_label.pack(pady = (20, 5))

#this is to add the day underneath
day_label = Label(window, font=("Helvetica", 40, "italic"), fg="white", bg="black")
day_label.pack(pady = (0, 10))

#this is for the date now
date_label = Label(window, font=("Helvetica", 30), fg="white", bg="black")
date_label.pack(pady = 5)

#this is to constnaly update the time
update()


#this is to run the window
window.mainloop()











