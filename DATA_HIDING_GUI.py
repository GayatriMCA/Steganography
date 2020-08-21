import cv2

print("data_hiding_gui starts")
from tkinter import filedialog,CENTER,NO,BOTH,Frame
from PIL import Image,ImageTk
import tkinter as tk
import DIVIDE_MESSAGE
import DIVIDE_IMAGE
import BEFORE_ENCRYPT
import EMBEDDING_PROCESS
import MAIL_SENT
import cv2


def openfilename():
    file=filedialog.askopenfilename(title='BROWSE')
    return file

def BROWSE_IMAGE():
    global count
    count=0
    global filename
    filename=openfilename()
    print(filename)
    DIVIDE_IMAGE.DIVIDE_PARTS(filename)
    count=count+1
    img=Image.open(filename)
    image_size=cv2.imread(filename)
    n_bytes = image_size.shape[0] * image_size.shape[1] * 3 // 8
    # print("[*] Maximum bytes to encode:", n_bytes)
    img = img.resize((200,200),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    panel=tk.Label(root,image=img, highlightbackground="black",highlightthickness=2)
    panel.image=img
    Text_heading_1 = tk.Label(root,
                            text="SOURCE IMAGE",
                            fg='black',bg="#E6DC8C",
                    font=('Gabriola', 10,'bold italic'))
    Text_heading_1.place(x=85,y=100)

    s.set('IMAGE CAN STORE DATA UP TO '+str(n_bytes)+' BYTES')
    panel.place(x=30,y=140)


def GET_MSG():
    global count
    global embedded
    message=Text_box.get()
    try:
        if(count==0):
            s.set("PLEASE CHOOSE IMAGE")
        elif(message==''):
            s.set('PLEASE ENTER SECERT MESSAGE')
        else:
            #print(message)
            count=count+1
            split_data=DIVIDE_MESSAGE.getting_msg(message)
            res=len(message.encode('utf-8'))
            embedded=BEFORE_ENCRYPT.hiding_message(message)
            Text_box.delete(first=0, last=1000)

            '''part_1 image'''
            block_1 = Image.open('part_1.jpg')
            block_1 = block_1.resize((80, 80), Image.ANTIALIAS)
            block_1 = ImageTk.PhotoImage(block_1)
            panel_1 = tk.Label(root, image=block_1,highlightbackground="black",highlightthickness=2)
            panel_1.image = block_1
            panel_1.place(x=350, y=80)
            sm_1.place(x=325, y=170, height=40, width=125)
            a.set(split_data[0])

            '''part_2 image'''
            block_2 = Image.open('part_2.jpg')
            block_2 = block_2.resize((80, 80), Image.ANTIALIAS)
            block_2 = ImageTk.PhotoImage(block_2)
            panel_2 = tk.Label(root, image=block_2,highlightbackground="black",highlightthickness=2)
            panel_2.image = block_2
            panel_2.place(x=500, y=80)
            sm_2.place(x=485, y=170, height=40, width=125)
            b.set(split_data[1])

            '''part_3 image'''
            block_3 = Image.open('part_3.jpg')
            block_3 = block_3.resize((80, 80), Image.ANTIALIAS)
            block_3 = ImageTk.PhotoImage(block_3)
            panel_3 = tk.Label(root, image=block_3,highlightbackground="black",highlightthickness=2)
            panel_3.image = block_3
            panel_3.place(x=350, y=225)
            sm_3.place(x=325, y=315, height=40, width=125)
            c.set(split_data[3])

            '''part_4 image'''
            block_4 = Image.open('part_4.jpg')
            block_4 = block_4.resize((80, 80), Image.ANTIALIAS)
            block_4 = ImageTk.PhotoImage(block_4)
            panel_4 = tk.Label(root, image=block_4,highlightbackground="black",highlightthickness=2)
            panel_4.image = block_4
            panel_4.place(x=500, y=225)
            sm_4.place(x=485, y=315, height=40, width=125)
            d.set(split_data[2])

            s.set('Embedding '+str(res)+' bytes of data to an image')
    except:
        s.set("PLEASE CHOOSE IMAGE")

def MAIN_PROCESS():
    #print(embedded)
    #print(filename)
    global count

    try:
        count=count+1
        EMBEDDING_PROCESS.main_data(filename,embedded)
        stegno = Image.open('Encrypted_image.PNG')
        stegno = stegno.resize((200, 200), Image.ANTIALIAS)
        stegno = ImageTk.PhotoImage(stegno)
        panel_5 = tk.Label(root, image=stegno,
                           highlightbackground="black",highlightthickness=2)
        panel_5.image = stegno
        panel_5.place(x=670, y=140)
        stegno_heading_1 = tk.Label(root,
                                  text="STEGNO-IMAGE",
                                  fg='black',bg="#E6DC8C",
                        font=('Gabriola', 10,'bold italic'))
        stegno_heading_1.place(x=720, y=100)
        s.set('SECRET MESSAGE EMBEDDED SUCCESSFULLY')
    except:
        s.set('PLEASE SPLITE IMAGE AND MESSAGE')

def Send():
    #try:
    if(count==3):
        print(count)
        mail = Receiver.get()
        MAIL_SENT.SendMail('Encrypted_image.PNG',mail)
        Receiver.delete(first=0, last=1000)
        s.set('MAIL SEND SUCCESSFULLY')
    else:
        s.set("PLEASE GENERATE STEGNO IMAGE")
    #except:
        #s.set("PLEASE ENTER RECEIVER MAIL")

def Back():
    root.destroy()


root = tk.Tk()
root.geometry("900x550+250+60")
root.title("RGBS EMBEDDING")
filename='DATA_HIDING_IMAGE.jpg'
img=Image.open(filename)
img = img.resize((900,550),Image.ANTIALIAS)
doge = ImageTk.PhotoImage(img)
x = tk.Label(root, image=doge)
x.grid(row = 0,column = 0)

Browse_button = tk.Button(root,
                          text="BROWSE_IMAGE",
                          fg="black",
                          bg="#61E6A8", borderwidth = 10,
                          activebackground = "#EA8D74",activeforeground="white",
                          font=('Gabriola', 12,'bold italic'),
                          command=BROWSE_IMAGE,
                          height=1,
                          width=13)
Text_heading = tk.Label(root,
                    text="ENTER SECRET MESSAGE",
                    fg='black',
                    bg="#E6DC8C",
                    font=('Gabriola', 10,'bold italic'))
Text_box = tk.Entry(root,justify = CENTER,bg="#EFD8C5")

#Encrypt = tk.Button(root,
 #                   text="ENCRYPTION")
split = tk.Button(root,
                    text="SPLITING PROCESS",
                    bg="#61E6A8", borderwidth = 5,
                          activebackground = "#EA8D74",activeforeground="white",
                          font=('Gabriola', 12,'bold italic'),
                    command=GET_MSG,height=1,
                          width=18)
Data_Hiding = tk.Button(root,
                        text = "RGBS DATA HIDING",
                        bg="#6FC2D5", borderwidth=5,
                        activebackground="#EA8D74", activeforeground="white",
                        font=('Gabriola', 12,'bold italic'),
                        command=MAIN_PROCESS,
                        height=1,
                        width=18)
Back=tk.Button(root,
                text = "BACK",
                bg="#61E6A8", borderwidth = 10,
                activebackground = "#EA8D74",activeforeground="white",
               font=('Gabriola', 12,'bold italic'),
             command=Back)
Status = tk.Label(root,
                    text="STATUS",
                    fg='black',
                    bg="#E6DC8C",
                    font=('Gabriola', 10, 'bold italic'))


Text_mail = tk.Label(root,
                    text="ENTER RECEVIER MAIL ADDRESS",
                    fg='black',bg="#E6DC8C",
                    font=('Gabriola', 10, 'bold italic'))
Receiver = tk.Entry(root,bg="#EFD8C5")

s=tk.StringVar()
Status_Entry = tk.Entry(root,
                        textvariable=s,justify= CENTER,bg="#EFD8C5",
                        font=('Times new roman', 10, 'bold italic'))
Send_Button = tk.Button(root,
                        text = "SEND",
                        bg="#61E6A8", borderwidth = 10,
                        activebackground = "#EA8D74",activeforeground="white",
                        font=('Gabriola', 12,'bold italic'),
                        command=Send)
a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()
d=tk.StringVar()

sm_1=tk.Entry(root,
              textvariable=a,bg="#C5EFE6",justify= CENTER,
              font=('Times new roman', 10, 'bold italic'))
sm_2=tk.Entry(root,
              textvariable=b,bg="#C5EFE6",justify= CENTER,
              font=('Times new roman', 10, 'bold italic'))
sm_3=tk.Entry(root,
              textvariable=c,bg="#C5EFE6",justify= CENTER,
              font=('Times new roman', 10, 'bold italic'))
sm_4=tk.Entry(root,
              textvariable=d,bg="#C5EFE6",justify= CENTER,
              font=('Times new roman', 10, 'bold italic'))

Status.place(x=250,y=15)
Status_Entry.place(x=320,y=10,height=50,width=350)
Browse_button.place(x=30,y=430)
Text_heading.place(x=230,y=410)
Text_box.place(x=170,y=450,height=50,width=250)
split.place(x=440,y=400)
Data_Hiding.place(x=440,y=460)
Text_mail.place(x=660,y=400)
Receiver.place(x=615,y=435,height=25,width=250)
Send_Button.place(x=620,y=465,height=50,width=100)
Back.place(x=750,y=465,height=50,width=100)
root.resizable(0,0)
root.mainloop()