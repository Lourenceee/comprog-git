
from tkinter import *
import calendar
import numpy
import cv2

def AniRawr():
    ani = Tk()
    ani.config(background = "white")
    ani.title("ANIMATION") 

    WIDTH = 500
    HEIGHT = 500

    anicav = Canvas(ani, width = WIDTH, height = HEIGHT)
    anicav.pack()

    photo_image = cv2.imread('images/maam.png')
    my_imageg = anicav.create_image(0,0,image = photo_image, anchor = NW )

    ani.mainloop()

def canvass():
    canvagui = Tk()
    canvagui.config(background = "white")
    canvagui.title("CANVA") 
    canvagui.geometry("250x300")

    canvaaa = Canvas(canvagui, height=250, width=300, background = 'pink')    
    line = canvaaa.create_line(20,55,100,7, width = 5)

    canvaaa.pack()
    canvagui.mainloop()

def Imagehehe():
    img = cv2.imread('images/logo.png')
    cv2.imshow('image', img)




def showCal() : 
    new_gui = Tk()     
    new_gui.config(background = "white") 
    new_gui.title("CUTE MAAM") 
    new_gui.geometry("550x600") 
    fetch_year = int(year_field.get()) 
    cal_content = calendar.calendar(fetch_year) 
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold") 
    cal_year.grid(row = 5, column = 1, padx = 20)     
    new_gui.mainloop()    


if __name__ == "__main__" : 
    gui = Tk()     
    gui.config(background = "white") 
    gui.title("CALENDER") 
    gui.geometry("500x500") 

    Nani = Label(gui, text = "COMPROG", bg = "dark gray",
                            font = ("times", 28, 'bold'))  

    topMenu = Menu(gui)
    gui.config(menu = topMenu)

    subMenu = Menu(topMenu)
    topMenu.add_cascade(menu = subMenu, label='Exit')
    subMenu.add_command(label = 'command ', command = exit)

    def papy(event):
        pop.post(event.x, event.y)
    
    def mami():
        img = cv2.imread('images/maam.jpg')
        cv2.imshow('image', img)
    
    pop = Menu(gui, tearoff = 0)
    pop.add_command(label = 'Hi Maam!', comman = mami)

    Nani.bind('<Button-3>', papy)

    cal = Label(gui, text = "        CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))    
    year = Label(gui, text = "Enter Year", bg = "light green")     
    year_field = Entry(gui) 
    Show = Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = showCal)
    ShowCanva = Button(gui, text = "Show Canva", fg = "Black",
                              bg = "Red", command = canvass)
    ShowImahe = Button(gui, text = "Show Image", fg = "Black",
                              bg = "Red", command = Imagehehe)
    Showani = Button(gui, text = "Show Animation", fg = "Black",
                              bg = "Red", command = AniRawr)

   
    Nani.grid(row = 1, column = 1)
    cal.grid(row = 1, column = 2) 
    year.grid(row = 3, column = 1) 
    year_field.grid(row = 4, column = 1) 
    Show.grid(row = 5, column = 1)
    ShowCanva.grid(row = 6, column = 1)
    ShowImahe.grid(row = 7, column = 1)  
    Showani.grid(row = 8, column = 1)
 
    gui.mainloop()