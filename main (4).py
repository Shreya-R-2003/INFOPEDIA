from states import *
from tkinter import *
import tkinter.font as font
from tkmacosx import Button
root = Tk()
root.geometry("1500x1500")
#l=Label(root,bg="black")
img2=PhotoImage(file="state7.png")
canvas1=Canvas(root)
canvas1.pack(fill ="both", expand = True)
canvas1.create_image(0, 0, image=img2,anchor="nw")
#canvas1.create_text(200, 150, font=('Helvetica',30))
myFont=font.Font(family="Helvetica",size=30,weight='bold')

label=Label(root,text="STATES OF INDIA",font=("Times",70,'bold'),bg='LightSteelBlue3',fg='RoyalBlue4').place(relx=0.5,rely=0.05,anchor="center")

button = Button(root, text="Karnataka",height=50,width=300, command=karnataka,fg="gray",bg="white",font=myFont).place(relx=0.39,rely=0.27)
button1 = Button(root, text="Maharashtra",height=50,width=300, command=maharashtra,bg="medium blue",fg="white",font=myFont).place(relx=0.39,rely=0.54)
button2 = Button(root, text="Tamil Nadu", height=50,width=300,command=tamilnadu,bg="green4",fg="white",font=myFont).place(relx=0.77,rely=0.50)
button3 = Button(root,text="Kerala", height=50,width=300,command=kerala,fg="gray",bg="white",font=myFont).place(relx=0.39,rely=0.36)
button4 = Button(root,text="Uttarakhand", height=50,width=300,command=uttarakhand,fg="white",bg="green4",font=myFont).place(relx=0.77,rely=0.82)
button5 = Button(root,text="Punjab",height=50,width=300, command=punjab,bg="green4",fg="white",font=myFont).place(relx=0.77,rely=0.26)
button6 = Button(root,text="Madhya Pradesh",height=50,width=300, command=madhyapradesh,fg="gray",bg="white",font=myFont).place(relx=0.39,rely=0.45)
button7 = Button(root,text="Rajasthan",height=50,width=300, command=rajasthan,fg="white",bg="green4",font=myFont).place(relx=0.77,rely=0.34)
button8 = Button(root,text="Mizoram", height=50,width=300,command=mizoram,bg="white",fg="gray",font=myFont).place(relx=0.39,rely=0.81)
button9 = Button(root,text="Uttar Pradesh",height=50,width=300, command=uttarpradesh,bg="green4",fg="white",font=myFont,).place(relx=0.77,rely=0.74)
button10 = Button(root,text="Odisha",height=50,width=300, command=odisha,bg="green4",fg="white",font=myFont).place(relx=0.77,rely=0.18)
button11 = Button(root,text="Nagaland", height=50,width=300,command=nagaland,bg="white",fg="gray",font=myFont).place(relx=0.39,rely=0.90)
button12 = Button(root,text="Tripura",height=50,width=300, command=tripura,fg="white",bg="green4",font=myFont).place(relx=0.77,rely=0.66)
button13 = Button(root,text="Sikkim", height=50,width=300,command=sikkim,bg="green4",fg="white",font=myFont).place(relx=0.77,rely=0.42)

Button(text = "Andhra Pradesh   ", height = 50 , width = 300, fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.18)
Button(text = "Arunachal Pradesh", height = 50 , width = 300,fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.27)
Button(text = "Assam", height = 50 , width =300,fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.36)
Button(text = "Bihar", height = 50 , width =300,fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.45)
Button(text = "Chhattisgarh",height = 50 , width = 300, fg = "white", bg = "DarkOrange2", font =myFont).place(relx = 0.02, rely = 0.54)
Button(text = "Goa",height = 50 , width = 300, fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.63)
Button(text = "Gujarat",height = 50 , width = 300, fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.72)
Button(text = "Haryana", height = 50 , width = 300,fg = "white", bg = "DarkOrange2", font = myFont).place(relx = 0.02, rely = 0.81)
Button(text = "Himachal Pradesh",height = 50 , width = 300, fg = "white", bg = "DarkOrange2", font =myFont).place(relx = 0.02, rely = 0.90)

Button(text = "Jharkhand", height = 50 , width = 300,fg = "gray", bg = "white", font = myFont).place(relx = 0.39, rely = 0.18)
Button(text = "Manipur", height = 50 , width = 300,fg = "gray", bg = "white", font = myFont).place(relx = 0.39, rely = 0.63)
Button(text = "Meghalaya", height = 50 , width = 300,fg = "gray", bg = "white", font = myFont).place(relx = 0.39, rely = 0.72)
Button(text = "Telangana",  height = 50 , width = 300,fg = "white", bg = "green4", font = myFont).place(relx = 0.77, rely = 0.58)
Button(text = "West Bengal",  height = 50 , width = 300,fg = "white", bg = "green4", font = myFont).place(relx = 0.77, rely = 0.90)

root.mainloop()
