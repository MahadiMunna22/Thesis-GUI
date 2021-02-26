import tkinter as tk
import tkinter.font as font
from tkinter import *
import time
import os
import pyautogui as pg
# import tkinter.font as font
########## GLOBAL VARIABLES ##########
l = 0 # Initial condition of light (0 = off, 1 = on)
f = 0 # Initial condition of fan (0 = off, 1 = on)
temp = 30  # Initial temp of AC
call_nurse = False
call_family = False
fan_speed = 2
head = "Down"
leg = "Down"
bed_left = "Down"
bed_right = "Down"

frame = []
frame2 = []

# Fonts
tempFont = []
callFamilyFont = []

root=[]

# Creating a 1D array of all the buttons we have used
buttons = [
    ['Call Nurse', 'Call Family', 'Fan'],
    ['Fan Speed Up', 'Fan Speed Down', 'Light'],
    ['Cold', 'Hot', 'Bed Head'],
    ['Bed Leg', 'Bed Left', 'Bed Right']
]

# Some important variables
curBut = [-1,-1] # Currently selected button's position
buttonL = [[]] # It specifies the color of the button [red -> selected, black -> unselected]
varRow = 1 # Initial Start Row + 1
varColumn = 0 # Initial Start Col
butRow = 4 # Total num of Row
butCol = 3 # Total num of col
startfocusKey = 0 # The focus button in top [Press down arrow at the last row]
endfocusKey = 10 # The focus button in bottom [Press up arrow at the first row]

# tempFont = font.Font(family='Helvetica', size=40, weight='bold')
# callFamilyFont = font.Font(family='Helvetica', size=20, weight='bold')