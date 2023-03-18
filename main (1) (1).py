from tkinter import *
def blore():
    c1 = Toplevel(root,bg="cornflower blue")
    c1.geometry("500x500")
 #l2 = Label(c1, text="Welcome to bangalore").pack()
    img=PhotoImage(file="blore3.png")
    l2 = Label(c1,image=img)
    l2.image=img
    l2.pack()
    t1=Text(c1,height=10,width=60,font=("Arial",16,"italic"),bg="MistyRose2")
    t1.insert(INSERT,'''Bangalore, also known as Bengaluru (Kannada) is the capital of the Indian State of Karnataka. Bangalore is nicknamed the Garden City and was once called a Pensioner's Paradise. Located on the Deccan Plateau in the south-eastern part of Karnataka, Bangalore is India's third most populous city. There are a number of expats from across the world living in the city,
     thanks to the growing presence of Multi-National Companies.''')
    t1.pack()


def mys():
    c2 = Toplevel(root,bg="LightGoldenrod1")
    l3 = Label(c2, text="welcome to mysore").pack()
def kar():
    new=Toplevel(root)
    b = Button(new,text="Bangalore", command=blore).pack()
    b1 = Button(new,text="Mysore", command=mys).pack()


def maha():
    new1=Toplevel(root)
    b2 = Button(new1,text="Mumbai").pack()
    b3 = Button(new1,text="Pune").pack()


def tn():
    new2=Toplevel(root)
    b4 = Button(new2,text="Chennai").pack()
    b5 = Button(new2,text="Madurai").pack()


def ker():
    new3=Toplevel(root)
    b6 = Button(new3,text="Thiruvananthapuram").pack()
    b7 = Button(new3,text="Trivandrum").pack()


def uttar():
    new4=Toplevel(root)
    b8 = Button(new4,text="Dehradun").pack()
    b9 = Button(new4,text="M").pack()


root = Tk()
img2=PhotoImage(file="ind.png")
canvas1=Canvas(root)
canvas1.pack(fill ="both", expand = True)
canvas1.create_image(0, 0, image=img2,
                     anchor="nw")
canvas1.create_text(200, 250, text="Welcome to statesofindia",font=('Helvetica',30))

#label = Label(root, text="Welcome to statesofindia", width=100)
button = Button(root, text="Karnataka", command=kar)
button1 = Button(root, text="Maharashtra", command=maha)
button2 = Button(root, text="Tamil Nadu", command=tn)
#button= canvas1.create_window(1000, 100,anchor="s",window=button,height=70,width=150)
button= canvas1.create_window(1000, 100,anchor="s",window=button,height=70,width=150)
button1 = canvas1.create_window(100, 40,anchor="nw",window=button1)


button2= canvas1.create_window(100, 70, anchor="nw", window=button2)


#button3 = Button(root, text="Kerala", command=ker)
#button4 = Button(root, text="Uttarakhand", command=uttar)
#label.pack()
'''button.pack(side=LEFT)
button1.pack()
button2.pack()
button3.pack()
button4.pack()'''
root.mainloop()
