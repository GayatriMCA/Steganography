print('data_extraction_gui starts')
from tkinter import filedialog, CENTER
from PIL import Image,ImageTk
import tkinter as tk
import AFTER_DECRYPT
import os

def openfilename():
    file=filedialog.askopenfilename(title='BROWSE')
    return file

def BROWSE_IMAGE():
    global count
    count=0
    global filename
    filename=openfilename()
    if(filename[-3:]=='jpg'):
        s.set('PLEASE SELECT STEGNO IMAGE ONLY')
    else:
        img=Image.open(filename)
        print(filename)
        os.system('DECODING_PROCESS.py')
        img = img.resize((200,200),Image.ANTIALIAS)
        count=count+1
        img=ImageTk.PhotoImage(img)
        panel=tk.Label(root,image=img,highlightbackground="black",highlightthickness=2)
        panel.image=img
        Text_heading_1 = tk.Label(root,
                                text="STEGNO IMAGE",
                                fg='black',
                                  bg="#E6DC8C",
                                  font=('Gabriola', 10, 'bold italic'))
        Text_heading_1.place(x=80,y=100)
        s.set('STEGNO IMAGE UPLOADED SUCCESSFULLY')
        panel.place(x=30,y=140)
def MAIN_PROCESS():
    try:
        if(count==1):
            msg=AFTER_DECRYPT.secret_message
            print(msg)
            Text_box = tk.Entry(root,
                                textvariable=v,justify = CENTER,bg="#C5EFE6",
                                font=('Times new roman', 12, 'bold'))
            heading_1 = tk.Label(root,
                                text="SECRET MESSAGE",
                                fg='black',
                                 bg="#E6DC8C",
                                 font=('Gabriola', 10, 'bold italic'))
            heading_1.place(x=420, y=140)
            Text_box.place(x=325, y=175, height=100, width=300)
            #Text_box.insert(tk.END,msg)
            s.set('DATA EXTRACTED FROM IMAGE')
            v.set(msg)
    except:
        s.set('PLEASE CHOOSE STEGNO IMAGE')
def Back():
    root.destroy()


root = tk.Tk()
root.geometry("700x500+250+60")
root.title("RGBS EXTRACTING")
filename='DATA_EXTRACTION_IMAGE.jpg'
img=Image.open(filename)
img = img.resize((700,500),Image.ANTIALIAS)
doge = ImageTk.PhotoImage(img)
x = tk.Label(root, image=doge)
x.grid(row = 0,column = 0)

v=tk.StringVar()

Browse_button = tk.Button(root,
                          text="BROWSE_IMAGE",
                            fg="black",
                            bg="#61E6A8", borderwidth = 10,
                            activebackground = "#EA8D74",activeforeground="white",
                            font=('Gabriola', 12,'bold italic'),
                          command=BROWSE_IMAGE,
                          height=1,
                          width=13)
Data_Extracting = tk.Button(root,
                        text = "RGBS DATA EXTRACTING",
                        bg="#6FC2D5", borderwidth = 5,
                        activebackground = "#EA8D74",activeforeground="white",
                        font=('Gabriola', 12,'bold italic'),
                        command=MAIN_PROCESS,
                        height=1,
                        width=20)

Status = tk.Label(root,
                    text="STATUS",
                  fg='black',
                  bg="#E6DC8C",
                  font=('Gabriola', 10, 'bold italic'))
s=tk.StringVar()
Status_Entry = tk.Entry(root,
                        textvariable=s,justify = CENTER,
                        bg="#EFD8C5",font=('Times new roman', 10, 'bold italic'))
Back=tk.Button(root,
                text = "BACK",
                bg="#61E6A8", borderwidth = 10,
               activebackground = "#EA8D74",activeforeground="white",
               font=('Gabriola', 12,'bold italic'),
             command=Back)

Status.place(x=198,y=19)
Status_Entry.place(x=250,y=10,height=50,width=300)
Browse_button.place(x=50,y=400)
Data_Extracting.place(x=290,y=400)
Back.place(x=550,y=400,height=50,width=100)
root.resizable(0,0)
root.mainloop()