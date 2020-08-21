import tkinter as tk
from PIL import Image,ImageTk
import os

def data_hiding():
    os.system('python DATA_HIDING_GUI.py')

def data_extraction():
    os.system('python DATA_EXTRACTION_GUI.py')

root = tk.Tk()
root.title("HOMEPAGE")
root.geometry("500x400+450+175")
filename='ashduyas.jpg'
img=Image.open(filename)
img = img.resize((500,400),Image.ANTIALIAS)
doge = ImageTk.PhotoImage(img)
x = tk.Label(root, image=doge)
x.grid(row = 0,column = 0)


button_1 = tk.Button(root,
                   text="RGBS EMBEDDING",
                   fg="black",
                   bg="#75A6E7", borderwidth = 10,
                   activebackground = "#EA8D74",activeforeground="white",
                   font=('Gabriola', 12,'bold italic'),
                                   command=data_hiding)
button_1.place(x=180,y=150,width=150,height=50)
button_2 = tk.Button(root,
                   text="RGBS EXTRACTING",
                   fg="black",
                   bg="#7E75E7",borderwidth = 10,
                   activebackground = "#EA8D74",
                   font=('Gabriola', 12,'bold italic'),
                   command=data_extraction)
button_2.place(x=180,y=210,width=150,height=50)
root.resizable(0,0)
root.mainloop()