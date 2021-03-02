import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import *
import time
import os
import pyautogui as pg
import global_var_of_ui as glui
import wheelchairGui as wg


def font_with_size(x):
    return font.Font(family='Helvetica', size=x, weight='bold')

def select(value):  # Button UI to be displayed in right frame of the window when any button is selected
    for i in range(glui.butRow):
        for j in range(glui.butCol):
            if (glui.buttons[i][j] == value):
                x,y = i,j
                break
    print(value)
    for widget in glui.frame2.winfo_children():
        widget.destroy()  # Blank the right frame before using it

    selectedBtn = tk.Label(glui.frame2, text=value)
    selectedBtn.pack()

    if glui.curBut != [-1,-1]:
        glui.buttonL[glui.curBut[0]][glui.curBut[1]].configure(bg='red')
        glui.buttonL[glui.curBut[0]][glui.curBut[1]].configure(bg='red')

    glui.curBut[:] = [x,y]
    glui.buttonL[x][y].configure(bg='red')
    glui.buttonL[x][y].configure(highlightcolor='red')
    for i in range(glui.butRow):
        for j in range(glui.butCol):
            if (i != x or j != y):
                glui.buttonL[i][j].configure(bg='black')
                glui.buttonL[i][j].configure(highlightcolor='black')

    # Selection of specific buttons which will call a specific function
    if value == 'Call Nurse':
        callNurse()
        
    elif value == 'Light':
        light()
    elif value == 'Fan':
        fan()
    elif value == 'Cold':
        cold()
    elif value == 'Hot':
        hot()
    elif value == 'Call Family':
        call_family()
    elif value == 'Bed Head':
        bed_head()
    elif value == 'Bed Leg':
        bed_Leg()
    elif value == 'Bed Left':
        bed_Left()
    elif value == 'Bed Right':
        bed_Right()
    elif value == 'Fan Speed Up':
        fan_speed_up()
    elif value == 'Fan Speed Down':
        fan_speed_down()
    elif value == 'Close':
        close()


def gifLoader(image_name, iteration, label, timer): # This function can load animation from a .gif image
    frames = [tk.PhotoImage(file=os.path.join('.\images',image_name),format = 'gif -index %i' %(i)) for i in range(iteration)]
    frames = [frames[i].subsample(2, 2) for i in range(iteration)] 
    def update(ind):
        if ind == iteration:
            ind = 0
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        label.image = frame
        glui.root.after(timer, update, ind)
    glui.root.after(0, update, 0)

# When a button is selected, the function corresponding to the button will work

def callNurse():

    call_nurse = True
    # soc.send("cn".encode())

    panel = tk.Label(glui.frame2)
    panel.pack(side="bottom", expand="yes")
    gifLoader('Call Nurse.gif', 2, panel, 500)

    call_nurse = False
    # soc.send("dcn".encode())
    
def light():

    if(glui.l == 0 or glui.l == -1):
        # soc.send("lon".encode())

        ind = 1
        glui.l = 1
        
        panel = tk.Label(glui.frame2, text="Light On")
        panel.pack(side="bottom", expand="yes")
        panel['font'] = glui.tempFont

    else:
        # soc.send("lof".encode())

        ind = 0
        glui.l = 0
        
        panel = tk.Label(glui.frame2, text="Light Off")
        panel.pack(side="bottom", expand="yes")
        panel['font'] = glui.tempFont
    
    lightLogo = tk.PhotoImage(file=r"./images/Light.gif", format='gif -index '+str(ind))
    photoimage = lightLogo.subsample(2, 2)
    panel = tk.Label(glui.frame2, image=photoimage)
    panel.image = photoimage
    panel.pack(side="bottom", expand="yes")

def fan():
    if (glui.f == 0 or glui.f == -1):
        # soc.send("fon".encode())

        panel = tk.Label(glui.frame2, text="Fan Running")
        panel.pack(side="bottom", expand="yes")
        panel['font'] = glui.tempFont

        panel = tk.Label(glui.frame2)
        panel.pack(side="bottom", expand="yes")
        gifLoader('Fan.gif', glui.fan_speed, panel, 100)
        glui.f = 1

        
    else:
        # soc.send("fof".encode())

        lightLogo = tk.PhotoImage(file=r".\images\\Fan.gif", format='gif -index 1')
        photoimage = lightLogo.subsample(2, 2)

        panel = tk.Label(glui.frame2, text="Fan not Running")
        panel.pack(side="bottom", expand="yes")
        panel['font'] = glui.tempFont

        panel = tk.Label(glui.frame2, image=photoimage)
        panel.image = photoimage
        panel.pack(side = "bottom", expand = "yes")
        glui.f = 0
        

def fan_speed_up():
    if(glui.fan_speed < 3):
        glui.fan_speed += 1
        # soc.send("t"+str(glui.fan_speed).encode())
    else:
        glui.fan_speed = 3
    fan_speed_control()
    
def fan_speed_down():
    if(glui.fan_speed > 1):
        glui.fan_speed -= 1
        # soc.send("t"+str(glui.fan_speed).encode())
    else:
        glui.fan_speed = 1
    fan_speed_control()

def fan_speed_control():

    panel = tk.Label(glui.frame2, text="Fan Speed: "+str(glui.fan_speed))
    panel.pack(side="bottom", expand="yes")
    panel['font'] = glui.tempFont

    panel = tk.Label(glui.frame2)
    panel.pack(side="bottom", expand="yes")
    gifLoader('Fan.gif', glui.fan_speed, panel, 100)
    
    glui.f = 1
    

def cold():
    glui.temp -= 1
    panel = tk.Label(glui.frame2, text="Decreasing Temperature\n"+ str(glui.temp) +" degree")
    panel.pack(side="bottom", expand="yes")
    panel['font'] = glui.tempFont

def hot():
    glui.temp += 1
    panel = tk.Label(glui.frame2, text="Increasing Temperature\n"+ str(glui.temp) +" degree")
    panel.pack(side="bottom", expand="yes")
    panel['font'] = glui.tempFont

def call_family():
    glui.call_family = True
    panel = tk.Label(glui.frame2, text="Your family will visit you soon")
    panel.pack(side="bottom", expand="yes")
    panel['font'] = glui.callFamilyFont
    # ui_to_firebase()
    # call_family = False

def bed_head():
    print("Head", glui.head)
    if glui.head == "Down":
        glui.head = "Up"
        # soc.send("hu".encode())
    else:
        glui.head = "Down"
        # soc.send("hd".encode())

    img = tk.PhotoImage(file=os.path.join(".\images","Bed Head "+glui.head+".png"))
    photoimage = img.subsample(2, 2)
    panel = tk.Label(glui.frame2, image=photoimage)
    panel.image = photoimage
    panel.pack(side="bottom", expand="yes")
    # ui_to_firebase()

def bed_Leg():
    print("Leg", glui.leg)
    if glui.leg == "Down":
        glui.leg = "Up"
        # soc.send("bu".encode())

    else:
        glui.leg = "Down"
        # soc.send("bd".encode())

    img = tk.PhotoImage(file=os.path.join(".\images","Bed Leg "+glui.leg+".png"))
    photoimage = img.subsample(2, 2)
    panel = tk.Label(glui.frame2, image=photoimage)
    panel.image = photoimage
    panel.pack(side="bottom", expand="yes")
    # ui_to_firebase()

def bed_Left():
    print("Head", glui.bed_left)
    if glui.bed_left == "Down":
        glui.bed_left = "Up"
        # soc.send("lu".encode())

    else:
        glui.bed_left = "Down"
        # soc.send("ld".encode())

    img = tk.PhotoImage(file=os.path.join(".\images","Bed Head "+glui.bed_left+".png"))
    photoimage = img.subsample(2, 2)
    panel = tk.Label(glui.frame2, image=photoimage)
    panel.image = photoimage
    panel.pack(side="bottom", expand="yes")
    # ui_to_firebase()

def bed_Right():
    print("Head", glui.bed_right)
    if glui.bed_right == "Down":
        glui.bed_right = "Up"
        # soc.send("ru".encode())

    else:
        glui.bed_right = "Down"
        # soc.send("rd".encode())

    img = tk.PhotoImage(file=os.path.join(".\images","Bed Head "+glui.bed_right+".png"))
    photoimage = img.subsample(2, 2)
    panel = tk.Label(glui.frame2, image=photoimage)
    panel.image = photoimage
    panel.pack(side="bottom", expand="yes")
    # ui_to_firebase()

def frameLeft():
    # Left frame that contains all the buttons
    glui.frame = tk.Frame(glui.root, bg='black')
    glui.frame.place(relx=0.02, rely=0.04)

    ButtonFrame()

def frameRight():
    # Right frame that contains the Animations / UI Screen
    glui.frame2 = tk.Frame(glui.root, height=700, width=820)
    glui.frame2.place(relwidth=0.5, relheight=0.8, relx=0.45, rely=0.1)

def buttonImg(name):
    # im = Image.open(file=os.path.join(".\images",name+".png"))
    # ButtonImg = ImageTk.PhotoImage(file=os.path.join(".\images",name+".png"), master=glui.root).subsample(7, 7)
    ButtonImg = (tk.PhotoImage(file=os.path.join(".\images",name+".png"))).subsample(7, 7)
    label = Label(glui.root, image=ButtonImg)
    label.image=ButtonImg
    return ButtonImg  

def close():
    glui.stopVoice = True
    glui.root.destroy()

def ButtonFrame():
    for x in glui.buttons:  # getting all the buttons individually and providing specific characteristics
        for button in x:
            
            but = tk.Button(glui.frame, text=button, width=150, bg="#000000", fg="#ffffff", highlightthickness=4, image=buttonImg(button),
                            compound=tk.TOP, activebackground="gray65", highlightcolor='red', activeforeground="#000000",
                            relief="raised", padx=5, pady=1, bd=4, command=lambda x=button, i=glui.varRow-1, j=glui.varColumn: select(x))
            but.bind('<Return>', lambda event, x=button, i=glui.varRow-1, j=glui.varColumn: select(x))
            glui.buttonL[glui.varRow-1].append(but)
            but.grid(row=glui.varRow, column=glui.varColumn, padx=5, pady=5)

            # Making the specific grid [3x3]
            glui.varColumn += 1
            if glui.varColumn > glui.butCol - 1: # after having specified no of columns, it will create a new row for the next button
                glui.varColumn = 0
                glui.varRow += 1
                glui.buttonL.append([])

def closeButton(x, y):
    # Close button at the right-top corner of the screen which will close the window
    close_btn = tk.Button(glui.root, text="   X   ", command=lambda: close(), fg="black", bg="red")
    close_btn.place(x=x, y=y)

def wheelChairBtn(x,y):
    wheelchair_btn = tk.Button(glui.root, text="Wheelchair Mode Activate",width=24, command=lambda: wg.wheelchair(glui.root), fg="white", bg="black")
    wheelchair_btn.place(x=x, y=y)
    wheelchair_btn['font'] = font_with_size(28)
