import tkinter as tk
import tkinter.font as font
from tkinter import *
import time
import os
import pyautogui as pg
import global_var_of_ui as glui
import socket
import globalFunc as gf
import threading
import VoiceModule as vm
import imageBasedInteraction as ibi

# soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address=("192.168.4.1", 81)
# soc.connect(address)

def voice(widget):
    for i in range(len(widget)):
        widget[i].pack_forget()
    threading.Thread(target=vm.voiceModule).start()
    threading.Thread(target=main).start()

def imageBased(root, widget):
    for i in range(len(widget)):
        widget[i].pack_forget()
    threading.Thread(target=ibi.imageBasedInteraction(root)).start()
    threading.Thread(target=main).start()

def test():
    r = tk.Tk()
    glui.root = r
    icon = tk.PhotoImage(file=("./images/Icon.png"))
    icon = icon.subsample(2, 2)
    panel = tk.Label(glui.root, image=icon)
    panel.image = icon
    panel.pack(side="top", expand="yes")
    v = tk.Button(r, text="Voice Based Interaction", command=lambda: voice([v,nt,panel]), fg="white", bg="black")
    v.pack(side=BOTTOM, padx=5, pady=5)
    nt = tk.Button(r, text="Image Based Interaction", command=lambda: imageBased(r,[v,nt,panel]), fg="white", bg="black")
    nt.pack(side=BOTTOM, padx=5, pady=5)
    r.geometry("500x500")
    r.mainloop()

def main():
    # glui.root = tk.Tk()
        
    glui.tempFont = font.Font(family='Helvetica', size=40, weight='bold')
    glui.callFamilyFont = font.Font(family='Helvetica', size=20, weight='bold')
    
    fs = True   # Full Screen / not Full Screen

    glui.root.attributes("-fullscreen", fs)

    gf.frameLeft()
    gf.frameRight()

    gf.closeButton(1320,2)
    gf.wheelChairBtn(25,680)

    glui.root.geometry("1360x780")  # When full screen is false, Window size will be 1000 x 600
    # glui.root.mainloop()  # Continue the whole frame again

test()