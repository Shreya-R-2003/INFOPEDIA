from states import *
from tkinter import *
import tkinter.font as font
root = Tk()
#l=Label(root,bg="black")
img2=PhotoImage(file="ind8.png")
canvas1=Canvas(root)
canvas1.pack(fill ="both", expand = True)
canvas1.create_image(0, 0, image=img2,anchor="nw")
#canvas1.create_text(200, 150, font=('Helvetica',30))
myFont=font.Font(family="Helvetica",size=30,weight='bold')

button = Button(root, text="Karnataka", command=kar)
button['font']=myFont
button1 = Button(root, text="Maharashtra", command=maha)
button1['font']=myFont
button2 = Button(root, text="Tamil Nadu", command=tn)
button2['font']=myFont
button3 = Button(root,text="Kerala", command=ker)
button3['font']=myFont
button4 = Button(root,text="Uttarakhand", command=uttar)
button4['font']=myFont
button5 = Button(root,text="Punjab", command=pun)
button5['font']=myFont
button6 = Button(root,text="Madhya Pradesh", command=mp)
button6['font']=myFont
button7 = Button(root,text="Rajasthan", command=raj)
button7['font']=myFont
button8 = Button(root,text="Mizoram", command=miz)
button8['font']=myFont

button = canvas1.create_window(700,150,anchor="e",window=button)
button1 = canvas1.create_window(900, 170,anchor="w",window=button1)
button2 = canvas1.create_window(100, 70, anchor="nw", window=button2)
button3 = canvas1.create_window(200,300, anchor="s",window=button3)
button4 = canvas1.create_window(700,400, anchor="e",window=button4)
button5 = canvas1.create_window(100,500, anchor="sw",window=button5)
button6 = canvas1.create_window(1400,500, anchor="e",window=button6)
button7 = canvas1.create_window(800,80, anchor="e",window=button7)
button8 = canvas1.create_window(900,600, anchor="s",window=button8)
root.mainloop()
