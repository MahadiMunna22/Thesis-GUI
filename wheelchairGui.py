import tkinter as tk

def Forward():
    return 0

def Backward():
    return 0

def Left():
    return 0

def Right():
    return 0

def wheelchair(root):
    wgui = tk.Toplevel(root)

    forward = tk.Button(wgui, text="FORWARD",height=10,width = 20,bg = "green", fg="white", command=Forward())
    forward.pack(side=tk.TOP, padx = 5,pady = 5)
    left = tk.Button(wgui, text="LEFT", height=10,width = 20, bg = "yellow", command=Left())
    left.pack(side=tk.LEFT, padx = 5,pady = 5)
    right = tk.Button(wgui, text="RIGHT", height=10,width = 20, bg = "yellow", command=Right())
    right.pack(side=tk.RIGHT, padx = 5,pady = 5)
    backward = tk.Button(wgui, text="BACKWARD", height=10,width = 20, bg = "red", fg="white", command=Backward())
    backward.pack(side=tk.BOTTOM, padx = 5,pady = 5)
    
    wgui.title("WheelChair Control")
    wgui.geometry("500x500")

def main():
    root = tk.Tk()
    wheelchair(root)
    root.mainloop()
main()