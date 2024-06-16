import tkinter as tk
import time
import math
import pygame
pygame.mixer.init()
tick_sound = pygame.mixer.Sound("tick.wav")
app_window = tk.Tk()
app_window.title("Clock")
app_window.geometry("500x500")
app_window.resizable(False, False)
time_font = ("Helvetica", 14, 'bold')
date_font = ("Helvetica", 10)
background_color = "#282c34"
circle_color = "#61dafb"
time_color = "#ffffff"
date_color = "#ffffff"
hand_color = "#ffffff"
canvas = tk.Canvas(app_window, width=500, height=500, bg=background_color, highlightthickness=0)
canvas.pack()
center_x, center_y = 250, 250
radius = 200
canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill=circle_color, outline="#282c34", width=4)
for i in range(12):
    angle = math.radians((i / 12) * 360)
    x_start = center_x + radius * 0.9 * math.cos(angle)
    y_start = center_y + radius * 0.9 * math.sin(angle)
    x_end = center_x + radius * 0.8 * math.cos(angle)
    y_end = center_y + radius * 0.8 * math.sin(angle)
    canvas.create_line(x_start, y_start, x_end, y_end, fill=hand_color, width=2)
label_time = tk.Label(app_window, font=time_font, bg=circle_color, fg=time_color)
label_date = tk.Label(app_window, font=date_font, bg=circle_color, fg=date_color)
canvas.create_window(center_x, center_y + 40, window=label_time)
canvas.create_window(center_x, center_y + 60, window=label_date)
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %B %d, %Y")
    label_time.config(text=current_time) 
    label_date.config(text=current_date)
    tick_sound.play()
    canvas.delete("hands")
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    sec_angle = math.radians((seconds / 60) * 360 - 90)
    min_angle = math.radians((minutes / 60) * 360 - 90)
    hour_angle = math.radians(((hours % 12) / 12) * 360 + (minutes / 60) * 30 - 90)
    sec_hand = (center_x + radius * 0.9 * math.cos(sec_angle), center_y + radius * 0.9 * math.sin(sec_angle))
    min_hand = (center_x + radius * 0.75 * math.cos(min_angle), center_y + radius * 0.75 * math.sin(min_angle))
    hour_hand = (center_x + radius * 0.5 * math.cos(hour_angle), center_y + radius * 0.5 * math.sin(hour_angle))
    canvas.create_line(center_x, center_y, sec_hand[0], sec_hand[1], fill="red", width=1, tags="hands")
    canvas.create_line(center_x, center_y, min_hand[0], min_hand[1], fill=hand_color, width=3, tags="hands")
    canvas.create_line(center_x, center_y, hour_hand[0], hour_hand[1], fill=hand_color, width=6, tags="hands")
    app_window.after(1000, update_clock)
update_clock()
app_window.mainloop()
