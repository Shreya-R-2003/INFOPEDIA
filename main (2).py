from states import *
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()

#l=Label(root,bg="black")

img2=ImageTk.PhotoImage(Image.open("transparancy image1.png"))

canvas1 = Canvas(root, width=1300, height=600,)

canvas1.grid(row=2, column=3)


canvas1.create_image(0, 0, anchor=NW, image=img2)
canvas1.pack(fill = "both", expand = True)

canvas1.create_text(200, 150, font=('Helvetica',30))

myFont=font.Font(family="Helvetica",size=30,weight='bold')

Button(text = "Andhra Pradesh", height = 1 , width = 18, fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = andhra).place(relx = 0.02, rely = 0.18)
Button(text = "Arunachal Pradesh", height = 1 , width = 18,fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = arun).place(relx = 0.02, rely = 0.27)
Button(text = "Assam", height = 1 , width = 18,fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = assam).place(relx = 0.02, rely = 0.36)
Button(text = "Bihar", height = 1 , width = 18,fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = bihar).place(relx = 0.02, rely = 0.45)
Button(text = "Chhattisgarh",height = 1 , width = 18, fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = chhat).place(relx = 0.02, rely = 0.54)
Button(text = "Goa",height = 1 , width = 18, fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = goa).place(relx = 0.02, rely = 0.63)
Button(text = "Gujarat",height = 1 , width = 18, fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = guj).place(relx = 0.02, rely = 0.72)
Button(text = "Haryana", height = 1 , width = 18,fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = har).place(relx = 0.02, rely = 0.81)
Button(text = "Himachal Pradesh",height = 1 , width = 18, fg = "white", bg = "DarkOrange2", font = ("myFont", 19), command = him).place(relx = 0.02, rely = 0.90)
Button(text = "Jharkhand", height = 1 , width = 18,fg = "gray", bg = "white", font = ("myFont", 19), command = jhar).place(relx = 0.39, rely = 0.18)
Button(text = "Karnataka",height = 1 , width = 18, fg = "gray", bg = "white", font = ("myFont", 19), command = karnataka).place(relx = 0.39, rely = 0.27)
Button(text = "Kerala", height = 1 , width = 18,fg = "gray", bg = "white", font = ("myFont", 19), command = kerala).place(relx = 0.39, rely = 0.36)
Button(text = "Madhya Pradesh", height = 1 , width = 18,fg = "gray", bg = "white", font = ("myFont", 19), command = madhyapradesh).place(relx = 0.39, rely = 0.45)
Button(text = "Maharashtra",height = 1 , width = 18, fg = "white", bg = "medium blue", font = ("myFont", 19), command = maharashtra).place(relx = 0.39, rely = 0.54)
Button(text = "Manipur", height = 1 , width = 18,fg = "gray", bg = "white", font = ("myFont", 19), command = mani).place(relx = 0.39, rely = 0.63)
Button(text = "Meghalaya", height = 1 , width = 18,fg = "gray", bg = "white", font = ("myFont", 19), command = meghalaya).place(relx = 0.39, rely = 0.72)
Button(text = "Mizoram",height = 1 , width = 18, fg = "gray", bg = "white", font = ("myFont", 19), command = mizoram).place(relx = 0.39, rely = 0.81)
Button(text = "Nagaland",  height = 1 , width = 18,fg = "gray", bg = "white", font = ("myFont", 19), command = nagaland).place(relx = 0.39, rely = 0.90)
Button(text = "Odisha",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = odisha).place(relx = 0.77, rely = 0.18)
Button(text = "Punjab",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = punjab).place(relx = 0.77, rely = 0.26)
Button(text = "Rajasthan",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = rajasthan).place(relx = 0.77, rely = 0.34)
Button(text = "Sikkim",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = sikkim).place(relx = 0.77, rely = 0.42)
Button(text = "Tamil Nadu",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = tamilnadu).place(relx = 0.77, rely = 0.50)
Button(text = "Telangana",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = tel).place(relx = 0.77, rely = 0.58)
Button(text = "Tripura",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = tripura).place(relx = 0.77, rely = 0.66)
Button(text = "Uttar Pradesh",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = uttarpradesh).place(relx = 0.77, rely = 0.74)
Button(text = "Uttarakhand",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = uttarakhand).place(relx = 0.77, rely = 0.82)
Button(text = "West Bengal",  height = 1 , width = 18,fg = "white", bg = "green4", font = ("myFont", 16), command = ben).place(relx = 0.77, rely = 0.90)


Label(text = "STATES OF INDIA",fg = "RoyalBlue4", bg = "LightSteelBlue3", font = ("Calibri", 56)).place(relx = 0.267, rely = 0.01)





root.mainloop()