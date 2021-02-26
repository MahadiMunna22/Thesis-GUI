import tkinter as tk
import tkinter.font as font
from tkinter import *
import time
import os
import pyautogui as pg
import global_var_of_ui as glui
import socket
import globalFunc as gf

# soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address=("192.168.4.1", 81)
# soc.connect(address)

def test():
    r = tk.Tk()
    glui.root = r
    glui.tempFont = font.Font(family='Helvetica', size=40, weight='bold')
    glui.callFamilyFont = font.Font(family='Helvetica', size=20, weight='bold')

    gf.frameLeft()
    gf.frameRight()
    r.mainloop()

def main():
    glui.root = tk.Tk()
        
    glui.tempFont = font.Font(family='Helvetica', size=40, weight='bold')
    glui.callFamilyFont = font.Font(family='Helvetica', size=20, weight='bold')
    
    fs = True   # Full Screen / not Full Screen

    glui.root.attributes("-fullscreen", fs)

    gf.frameLeft()
    gf.frameRight()

    gf.closeButton(1320,2)
    gf.wheelChairBtn(50,680)

    glui.root.geometry("1360x780")  # When full screen is false, Window size will be 1000 x 600
    glui.root.mainloop()  # Continue the whole frame again

test()