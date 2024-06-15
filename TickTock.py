from tkinter import Label, Tk 
import time
import pygame
pygame.mixer.init()
tick_sound = pygame.mixer.Sound("tick.wav")
app_window = Tk() 
app_window.title("Python Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=0, columnspan=2)
def python_clock(): 
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    tick_sound.play()
    label.after(1000, python_clock)
python_clock()
app_window.mainloop()
