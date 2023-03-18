from cities1 import *
from tkinter import *
import tkinter.font as font
def andhra():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "ANDHRA PRADESH", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold")).place(relx = 0.3, rely = 0.05)
    Label(andhrawin, text="Andhra Pradesh is a state in South India.\n It is bordered by chhatisgarh, telangana, karnataka, tamil nadu, odisha.\n Amaravati is the capital city of andhra pradesh.\n Telugu is the widely spoken language in andhra pradesh.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.1, rely=0.18)
    Label(andhrawin, text = "The capital city of Andhra pradesh is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.1, rely = 0.39)
    Button(andhrawin, text = "Amaravati", fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = amar).place(relx = 0.1, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of andhra pradesh is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.1, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Sriharikota", fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = srihk).place(relx = 0.1, rely = 0.67)

def maha():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "MAHARASHTRA", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold")).place(relx = 0.3, rely = 0.05)
    Label(andhrawin, text="Maharashtra is a state in South India.\n It is bordered by chhatisgarh, telangana, karnataka, gujarat, goa, dadra and nagar haveli.\n Mumbai is the capital city of Maharashtra.\n Marathi, hindi is the widely spoken language in Maharashtra.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Maharashtra is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Mumbai",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = mum).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Maharashtra is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Pune", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = pune).place(relx = 0.06, rely = 0.67)

def arun():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "ARUNACHAL PRADESH", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold")).place(relx = 0.26, rely = 0.05)
    Label(andhrawin, text="Arunachal Pradesh is a state in North East India.\n It is bordered by assam, nagaland, bhutan, china, myanmar.\n Itanagar is the capital city of Arunachal Pradesh.\n English, Nyishi, Adi, Nepali is the widely spoken language in Arunachal Pradesh.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Arunachal Pradesh is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Itanagar",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = ita).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Arunachal Pradesh is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Tezu", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = tez).place(relx = 0.06, rely = 0.67)

def assam():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "ASSAM", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold"), width = 8).place(relx = 0.40, rely = 0.05)
    Label(andhrawin, text="Assam is a state in North East India.\n It is bordered by arunachal pradesh, nagaland, manipur, mizoram, meghalaya, tripura, west bengal.\n Dispur is the capital city of Assam.\n Assamese is the widely spoken language in Assam.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 19, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Assam is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Dispur",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = disp).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Assam is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Dibrugarh", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = dib).place(relx = 0.06, rely = 0.67)

def bihar():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "BIHAR", fg = "DarkOrange", bg = "DarkOrange4", width = 8, font = ("Royal", 45, "bold")).place(relx = 0.4, rely = 0.05)
    Label(andhrawin, text="Bihar is a state in North India.\nIt is bordered by west bengal, uttar pradesh, jharkhand, nepal.\nPatna is the capital city of Bihar.\nHindi is the widely spoken language in Bihar.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Bihar is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Patna",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = pat).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Bihar is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Vaishali", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = vaish).place(relx = 0.06, rely = 0.67)


def chhat():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "CHHATTISGARH", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold")).place(relx = 0.3, rely = 0.05)
    Label(andhrawin, text="Chhattisgarh is a state in North India.\n It is bordered by assam, nagaland, bhutan, china, myanmar.\n Raipur is the capital city of Chhattisgarh.\n Chhattisgarhi, Hindi is the widely spoken language in Chhattisgarh.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Chhattisgarh is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Raipur",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = rai).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Chhattisgarh is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Bhilai", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = bhil).place(relx = 0.06, rely = 0.67)

def goa():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "GOA", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold"), width = 8).place(relx = 0.41, rely = 0.05)
    Label(andhrawin, text="Goa is a state in central India.\nIt is bordered by karnataka, maharashtra.\nPanaji is the capital city of Goa.\nKonkani is the widely spoken language in Goa.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Goa is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Panaji",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = panaj).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Goa is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Madgaon", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = madg).place(relx = 0.06, rely = 0.67)

def guj():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "GUJARAT", fg = "DarkOrange", bg = "DarkOrange4", width = 8, font = ("Royal", 45, "bold")).place(relx = 0.36, rely = 0.05)
    Label(andhrawin, text="Gujarat is a state in North west India.\n It is bordered by rajasthan, maharahstra, madhya pradesh, sindh(pak), daman and diu, dadra and nagar haveli.\n Gandhinagar is the capital city of Gujarat.\nGujarathi is the widely spoken language in Gujarat.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 17, "bold")).place(relx=0.04, rely=0.18)
    Label(andhrawin, text = "The capital city of Gujarat is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Gandhinagar",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = gan).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Gujarat is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Ahmedabad", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = amd).place(relx = 0.06, rely = 0.67)

def har():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "HARYANA", fg = "DarkOrange", bg = "DarkOrange4", width = 8, font = ("Royal", 45, "bold")).place(relx = 0.39, rely = 0.05)
    Label(andhrawin, text="Haryana is a state in North India.\nIt is bordered by Punjab, himachal pradesh, rajasthan, uttar pradesh, uttarakhand.\nChandigarh is the capital city of Haryana.\nHaryanvi is the widely spoken language in Haryana.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Haryana is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Chandigarh",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = guru).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Haryana is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Gurugram", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = guru).place(relx = 0.06, rely = 0.67)

def him():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "HIMACHAL PRADESH", fg = "DarkOrange", bg = "DarkOrange4", font = ("Royal", 45, "bold")).place(relx = 0.26, rely = 0.05)
    Label(andhrawin, text="Himachal Pradesh is a state in North India.\nIt is bordered by jammu and kashmir, ladakh, punjab, haryana, uttarakhand, uttar pradesh.\nShimla(summer) and Dharmasala(winter) is the capital city of Himachal Pradesh.\nHindi, Pahari is the widely spoken language in Himachal Pradesh.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 20, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Himachal Pradesh is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Shimla(summer)",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = shim).place(relx = 0.06, rely = 0.46)
    Button(andhrawin, text="Dharmashala(winter)", height=1, width=16, fg="white", bg="PeachPuff4", font=("myFont", 35), command=dhar).place(relx=0.4, rely=0.46)
    Label(andhrawin, text = "One of the important cities of Himachal Pradesh is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Manali", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = manl).place(relx = 0.06, rely = 0.67)

def jhar():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "JHARKHAND", fg = "DarkOrange", bg = "DarkOrange4", width = 11,font = ("Royal", 45, "bold")).place(relx = 0.35, rely = 0.05)
    Label(andhrawin, text="Jharkhand is a state in North India.\nIt is bordered by chhattisgarh, bihar, uttar pradesh, west bengal, odisha.\nRanchi is the capital city of Jharkhand.\nHindi is the widely spoken language in Jharkhand.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Jharkhand is : ", fg = "white", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Ranchi",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = ranch).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Haryana is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Jamshedpur", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = jam).place(relx = 0.06, rely = 0.67)

def har():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "HARYANA", fg = "DarkOrange", bg = "DarkOrange4", width = 8, font = ("Royal", 45, "bold")).place(relx = 0.39, rely = 0.05)
    Label(andhrawin, text="Haryana is a state in North India.\nIt is bordered by Punjab, himachal pradesh, rajasthan, uttar pradesh, uttarakhand.\nChandigarh is the capital city of Haryana.\nHaryanvi is the widely spoken language in Haryana.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Haryana is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Chandigarh",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = guru).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Haryana is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Gurugram", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = guru).place(relx = 0.06, rely = 0.67)

def ben():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "WEST BENGAL", fg = "DarkOrange", bg = "DarkOrange4", width = 13, font = ("Royal", 45, "bold")).place(relx = 0.35, rely = 0.05)
    Label(andhrawin, text="West Bengal is a state in North India.\nIt is bordered by jharkhand, odisha, assam, sikkim, bihar.\nKolkata is the capital city of West Bengal.\nBengali is the widely spoken language in West Bengal.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of West Bengal is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Kolkata",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = kol).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of West Bengal is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Darjeeling", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = darj).place(relx = 0.06, rely = 0.67)

def tel():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "TELANGANA", fg = "DarkOrange", bg = "DarkOrange4", width = 12, font = ("Royal", 45, "bold")).place(relx = 0.33, rely = 0.05)
    Label(andhrawin, text="Telangana is a state in South India.\nIt is bordered by andhra pradesh, karnataka, maharashtra, odisha.\nHyderabad is the capital city of Telangana.\nTelugu is the widely spoken language in Telangana.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Telangana is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Hyderabad",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = hyd).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Telangana is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Warangal", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = war).place(relx = 0.06, rely = 0.67)

def mani():
    andhrawin = Toplevel()
    andhraimg = PhotoImage(file = "statesbg.png")
    canvas = Canvas(andhrawin, width = 1200, height = 600)
    canvas.create_image(0,0, anchor = "nw", image = andhraimg)
    canvas.image = andhraimg
    canvas.pack(fill = "both", expand = True, anchor = "nw")
    #canvas.create_text(andhrawin, 0.1,0.1,fg = "blue", text = "hello")
    Label(andhrawin, text = "MANIPUR", fg = "DarkOrange", bg = "DarkOrange4", width = 12, font = ("Royal", 45, "bold")).place(relx = 0.33, rely = 0.05)
    Label(andhrawin, text="Manipur is a state in North East India.\nIt is bordered by Assam, Nagaland, Mizoram, Myanmar.\nImphal is the capital city of Manipur.\nManipuri Meiteilon is the widely spoken language in Manipur.", fg="white", bg = "DarkOrange3", justify = "left", font=(None, 22, "bold")).place(relx=0.06, rely=0.18)
    Label(andhrawin, text = "The capital city of Telangana is : ", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.39)
    Button(andhrawin, text = "Imphal",height = 1 , width = 16, fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = imp).place(relx = 0.06, rely = 0.46)
    Label(andhrawin, text = "One of the important cities of Manipur is :", fg = "beige", bg = "DarkOrange3", font = ("Royal", 22, "bold")).place(relx = 0.06, rely = 0.60)
    #Label(andhrawin, text = "One of the important cities of Andhra Pradesh is : ", fg = "brown", bg = "beige", font = (None, 35)).place(relx = 0.1, rely = 0.45)
    Button(andhrawin, text = "Thoubal", height = 1 , width = 16,fg = "white", bg = "PeachPuff4", font = ("myFont", 35), command = thou).place(relx = 0.06, rely = 0.67)


def karnataka():
    new = Toplevel()
    img3 = PhotoImage(file="statesbg.png")
    canvas2 = Canvas(new)
    canvas2.image = img3
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=img3, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=70, weight='bold')
    Button(new, text="Bangalore", command=blore, fg="beige", bg="OrangeRed4", width = 12, font=("myFont1", 32)).place(relx=0.46, rely=0.65)

    Button(new, text="Mysore", command=mysore, fg="beige", bg="OrangeRed4", width = 12, font=("myFont1", 32)).place(relx=0.46, rely=0.8)
    canvas2.create_text(427, 495, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas2.create_text(327,  604, text='One of the important cities is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas2.create_text(330, 30, text="Welcome to Karnataka", font=('Helvetica', 50, 'bold'), fill="coral4", anchor="nw")
    canvas2.create_text(680, 280, text='''Capital of Karnataka is Bangalore. Kannada is the most widely spoken language in Karnataka. It is the largest state in South India. The neighbouring states of Karnataka are Goa, Maharashtra, Telangana, Andhra Pradesh, Kerala and Tamil Nadu. It is bound by Arabian Sea to its West. Karnataka has many colleges and universities serving the needs of a large Indian population. The silicon valley of India is located in Karnataka. There are many scientific organisations located in Karnataka. Karnataka is the 6th largest state in India by area and 8th largest state in India by population. There are 31 districts in the state of Karnataka. Karnataka was earlier known as the State of Mysore. Some of the most famous tourist attractions in Karnataka are its beaches, Mysore Palace, Hampi, Badami, Aihole, Pattadakal, Coorg, Shivanasamudra Falls, Jog Falls, different wildlife sanctuaries etc. Karnataka has many Eastward flowing and Westward flowing rivers.''', width = 1200, font=('Helvetica', 19, 'italic'), fill="red4")



def maharashtra():
    new1 = Toplevel()
    img3 = PhotoImage(file="statesbg.png")
    canvas2 = Canvas(new1)
    canvas2.image = img3
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=img3, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=70, weight='bold')
    Button(new1, text="Mumbai", fg="beige", bg="OrangeRed4", width = 12, font=("myFont1", 32), command = mum).place(relx=0.46, rely=0.66)

    Button(new1, text="Pune", fg="beige", bg="OrangeRed4", width = 12, font=("myFont1", 32), command = pune).place(relx=0.46, rely=0.80)
    canvas2.create_text(427, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas2.create_text(335, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas2.create_text(307, 30, text="Welcome to Maharashtra", font=('Helvetica', 50, 'bold'), fill="coral4",anchor="nw")
    canvas2.create_text(660,285,text='''Regarded as the Land of Marathas, Maharashtra is the 3rd largest state in India. The capital city of Maharashtra is Mumbai. Official language of this state is Marathi and it is the second largest state in the nation by population. Maharashtra shares its borders with 6 states –To the northwest lies Gujarat, to the north lies Madhya Pradesh, to the east lies Chhattisgarh, to the southeast lies Telangana and Karnataka and Goa lie to the south.The richest state of the nation – Maharashtra whose capital is Mumbai which is regarded as the financial capital of India.Maharashtra is a distinctcultural region. Its long artistic tradition is manifested in the ancient cave paintings found at Ajanta and Ellora.Pune, where numerous organizations sustain those great traditions, is the state’s undisputed cultural capital. ''', width = 1200, font=('Helvetica', 19, 'italic'), fill="red4")



def tamilnadu():
    new2 = Toplevel()
    img5 = PhotoImage(file="statesbg.png")
    canvas4 = Canvas(new2)
    canvas4.image = img5
    canvas4.pack(fill="both", expand=True)
    canvas4.create_image(0, 0, image=img5, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new2, text="Chennai", command=chennai, fg="beige", bg="OrangeRed4", font=myFont1).place(relx=0.469, rely=0.66)

    Button(new2, text="Madurai", command=madurai, fg="beige", bg="OrangeRed4", font=myFont1).place(relx=0.469, rely=0.81)
    canvas4.create_text(437, 510, text='''The capital city is:''', font=("myFont1", 28, "bold"), fill='coral4')
    canvas4.create_text(327, 600, text='''One of the important cities is:''', font=("myFont1" , 28, "bold") , fill='coral4')
    canvas4.create_text(307, 30, text="Welcome to Tamil Nadu", font=("myFont1", 50, "bold"), fill="coral4",
                             anchor="nw")
    canvas4.create_text(700,300,text=
'''Tamil Nadu is bounded by the Indian Ocean to the east and south and by the states of Kerala to the west, Karnataka (formerly Mysore) to the northwest, and Andhra Pradesh to the north.The climate of Tamil Nadu is essentially tropical. In May and June, the hottest months, maximum daily temperatures in Chennai average about 100 °F (38 °C), Hinduism lies at the core of the culture of Tamil Nadu. Among the most famous of the state’s temples, which number in the tens of thousands, are the 7th- and 8th-century structures at Mamallapura. Bharata natyam,one of India’s major classical dance forms, and Carnatic music (South Indian classical music) are both widely practiced.Tamil Nadu has some of the most remarkable temple architecture in the country,and a living tradition of music, dance, folk arts and fine arts. Tamil Nadu is well renowned for its temple towns and heritage sites, hill stations, waterfalls, national parks, local cuisine, natural environment and wildlife.''', width = 1230, font=("myFont1", 19, "italic"),fill="red4")



def kerala():
    new3=Toplevel()
    img6 = PhotoImage(file="statesbg.png")
    canvas5 = Canvas(new3)
    canvas5.image = img6
    canvas5.pack(fill="both", expand=True)
    canvas5.create_image(0, 0, image=img6,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new3, text="Thiruvananthapuram",command=thiruvananthapuram, fg="beige",bg="OrangeRed4",width = 17, font=myFont1).place(relx=0.46,rely=0.66)

    Button(new3, text="Kochi",command=kochi,fg="beige",bg="OrangeRed4",font=myFont1, width = 17).place(relx=0.46,rely=0.81)
    canvas5.create_text(427, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas5.create_text(337, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas5.create_text(347, 30, text="Welcome to Kerala", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    canvas5.create_text(700, 300,text='''Kerala situated on the tropical Malabar Coast of southwestern India, is one of the most popular tourist destinations in the country. Named as one of the ten paradises of the world by National Geographic Traveler, Kerala is famous especially for its ecotourism initiatives and beautiful backwaters. Its unique culture and traditions, coupled with its varied demography, have made Kerala one of the most popular tourist destinations in the world.Kerala is well known for its beaches, backwaters in Alappuzha and Kollam, mountain ranges and wildlife sanctuaries.The major festival in Kerala is Onam. Kerala has a number of religious festivals. Thrissur Pooram, Attukal Pongala, Beema Palli Uroos, and Chettikulangara Bharani are the major temple festivals in Kerala.n respect of Fine Arts,the State has an abounding tradition of both ancient and contemporary art and artists. The traditional Kerala murals are found in ancient temples, churches and palaces across the State.''',font=('Helvetica', 19 ,'italic'),width = 1200, fill="red4")



def uttarakhand():
    new4=Toplevel()
    img7 = PhotoImage(file="statesbg.png")
    canvas6 = Canvas(new4)
    canvas6.image = img7
    canvas6.pack(fill="both", expand=True)
    canvas6.create_image(0, 0, image=img7,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new4, text="Dehradun",command=dehradun,fg="beige",bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.46,rely=0.66)

    Button(new4, text="Kedarnath",command=kedarnath,fg="beige",bg="OrangeRed4",width = 12, font=myFont1).place(relx=0.46,rely=0.80)
    canvas6.create_text(427, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas6.create_text(337, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas6.create_text(317, 30, text="Welcome to Uttarakhand", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    canvas6.create_text(700, 300, text=
'''Uttarakhand, formerly Uttaranchal, state of India, located in the northwestern part of the country. It is bordered to the northwest by the Indian state of Himachal Pradesh, to the northeast by the Tibet Autonomous Region of China, to the southeast by Nepal, and to the south and southwest by the Indian state of Uttar Pradesh. Its capital is the northwestern city of Dehra Dun.Uttarakhand has a highly varied topography, with snow-covered peaks, glaciers, deep canyons, roaring streams, beautiful lakes, and a few patches of dusty plains in the south. Some of the highest mountains in the world are found in Uttarakhand.The climate of Uttarakhand is temperate, marked by seasonal variations in temperature but also affected by tropical monsoons.Some of Hinduism’s holiest shrines and temples, which are also pilgrimage centres, are located in the mountains of Uttarakhand.At Kedarnath, is a stone temple to Shiva that is considered to be more than 1,000 years old; a large statue of the bull Nandi, one of Shiva’s chief attendants, stands outside the temple door. ''',font=('Helvetica', 19 ,'italic'), width = 1200,fill="red4")



def punjab():
    new5 = Toplevel()
    img8 = PhotoImage(file="statesbg.png")
    canvas7 = Canvas(new5)
    canvas7.image=img8
    canvas7.pack(fill="both", expand=True)
    canvas7.create_image(0, 0, image=img8,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new5, text="Chandigarh",command=chandigarh,fg="beige",bg="OrangeRed4",width =12, font=myFont1).place(relx=0.46,rely=0.66)

    Button(new5, text="Amritsar",command=amritsar,fg="beige",bg="OrangeRed4",width = 12, font=myFont1).place(relx=0.46,rely=0.80)
    canvas7.create_text(427, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas7.create_text(327, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas7.create_text(367, 30, text="Welcome to Punjab", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    canvas7.create_text(700, 300, text='''Punjab is bounded by Jammu and Kashmir union territory to the north, Himachal Pradesh state to the northeast, Haryana state to the south and southeast, and Rajasthan state to the southwest.The city of Chandigarh, within the Chandigarh union territory, is the joint capital of Punjab and Haryana.The word Punjab is a compound of two Persian words, panj (“five”) and āb (“water”), thus signifying the land of five waters, or five rivers.Some two-fifths of Punjab’s population is engaged in the agricultural sector, which accounts for a significant segment of the state’s gross product.Punjab holds numerous religious and seasonal festivals, such as Dussehra.Dancing is a typical feature of such festivities, with bhangra, jhumar, and sammi among the most popular genres.The state’s outstanding architectural monument is the Harmandir Sahib (Golden Temple) at Amritsar, which blends Indian and Muslim styles. Its chief motifs, such as the dome and the geometric design, are repeated in most of the Sikh places of worship. ''', width = 1200, font=('Helvetica', 19 ,'italic'),fill="red4")


def madhyapradesh():
    new6 = Toplevel()
    img9 = PhotoImage(file="statesbg.png")
    canvas8 = Canvas(new6)
    canvas8.image = img9
    canvas8.pack(fill="both", expand=True)
    canvas8.create_image(0, 0, image=img9,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new6, text="Bhopal",command=bhopal,fg="beige",bg="OrangeRed4",width = 12,font=myFont1).place(relx=0.46,rely=0.66)

    Button(new6, text="Indore",command=indore,fg="beige",bg="OrangeRed4",width = 12,font=myFont1).place(relx=0.46,rely=0.80)
    canvas8.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas8.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas8.create_text(237, 30, text="Welcome to Madhya Pradesh", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    canvas8.create_text(700, 300, text='''Madhya Pradesh,as its name implies—madhya means “central” and pradesh means “region” or “state”— is situated in the heart of the country. The state has no coastline and no international frontier.Madhya Pradesh lies over a transitional area between the Indo-Gangetic Plain in the north and the Deccan plateau in the south.The climate in Madhya Pradesh is governed by a monsoon weather pattern.Madhya Pradesh has anumber of national parks and many wildlife sanctuaries, of which the best known are Kanha National Park, in the southeastern part of the state.Ancient temples, fortresses, and cave works reflect the rich history of Madhya Pradesh. In the foothills of the Vindhya Range, prehistoric paintings dating from roughly 10,000 BCE adorn the walls of the Bhimbetka rock shelters. In west-central Madhya Pradesh, one of the state’s oldest historical monuments is the stupa (Buddhist mound forming a memorial shrine) at Sanchi, near Vidisha.The state has several well-known annual cultural events, such as Kalidas Samaroh (for the visual and performing arts) in Ujjain, Tansen Samaroh (classical music) in Gwalior, and a dance festival in Khajuraho, where artists from all over India participate.''', width = 1200, font=('Helvetica', 17 ,'italic'),fill="red4")


def rajasthan():
    new7 = Toplevel()
    img10 = PhotoImage(file="statesbg.png")
    canvas9 = Canvas(new7)
    canvas9.image = img10
    canvas9.pack(fill="both", expand=True)
    canvas9.create_image(0, 0, image=img10,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new7, text="Jaipur",command=jaipur,fg="beige",bg="OrangeRed4",width = 12, font=myFont1).place(relx=0.469,rely=0.66)

    Button(new7, text="Jodhpur",command=jodhpur,fg="beige",bg="OrangeRed4",width = 12,font=myFont1).place(relx=0.469,rely=0.80)
    canvas9.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas9.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas9.create_text(317, 30, text="Welcome to Rajasthan", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    canvas9.create_text(700, 300, text=
'''Rajasthan,is located in the northwestern part of the Indian subcontinent. It is bounded to the north and northeast by the states of Punjab and Haryana, to the east and southeast by the states of Uttar Pradesh and Madhya Pradesh, to the southwest by the state of Gujarat, and to the west and northwest by the provinces of Sindh and Punjab in Pakistan. The capital city is Jaipur, in the east-central part of the state.Rajasthan, meaning “The Abode of the Rajas,” was formerly called Rajputana, “The Country of the Rajputs” .The typical dance of Rajasthan is the ghoomar, which is performed on festive occasions by only women. Other well-known dances include the geer, which is performed by men and women.Splendid princely palaces, many elaborately decorated with wall paintings, are scattered throughout the state.Those and other historic structures (e.g., temples) are often within several historic Rajput hill forts, six of which—including those at Chittaurgarh, Jaipur.Cultural life in Rajasthan is characterized by numerous religious festivals. Among the most popular of those celebrations is the Gangaur festival, during which clay images of Mahadevi and Parvati (representing the benevolent aspects of the Hindu mother goddess) are worshipped by women. ''', width = 1200, font=('Helvetica', 17 ,'italic'),fill="red4")


def mizoram():
    new8 = Toplevel()
    img11 = PhotoImage(file="statesbg.png")
    canvas10 = Canvas(new8)
    canvas10.image = img11
    canvas10.pack(fill="both", expand=True)
    canvas10.create_image(0, 0, image=img11,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new8, text="Aizawl",command=aizawl,fg="beige",bg="OrangeRed4",width = 12,font=myFont1).place(relx=0.469,rely=0.66)

    Button(new8, text="Lunglei",command=lunglei,fg="beige",bg="OrangeRed4",width = 12,font=myFont1).place(relx=0.469,rely=0.80)
    canvas10.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas10.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas10.create_text(357, 30, text="Welcome to Mizoram", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    canvas10.create_text(700, 300, text='''Mizoram, is located in the northeastern part of the country and is bounded by Myanmar (Burma) to the east and south and Bangladesh to the west and by the states of Tripura to the northwest, Assam to the north, and Manipur to the northeast. The capital is Aizawl, in the north-central part of the state.Mizoram (“Land of the Mizos”) was known as the Lushai Hills District of Assam before it was renamed the Mizo Hills District in 1954.Most of the Mizo are Tibeto-Burman peoples, speaking Mizo or a closely related Tibeto-Burman language or dialect.Mizoram is one of the most sparsely populated states of India. Music and dance are important elements in Mizo cultural life, with many festivities associated with the Christian holidays. pawl kut is also a harvest festival, which takes place in December or January. Among shifting agriculturalists, the chapchar kut is held at the start of the agricultural year, after the forest has been felled and before the burning of the new fields begins—usually sometime in March.''',width = 1200, font=('Helvetica', 17 ,'italic'),fill="red4")


def odisha():
    new9 = Toplevel()
    img12 = PhotoImage(file="statesbg.png")
    canvas11 = Canvas(new9)
    canvas11.image = img12
    canvas11.pack(fill="both", expand=True)
    canvas11.create_image(0, 0, image=img12,anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    b18 = Button(new9, text="Bhubaneswar",command=bhubaneswar,fg="beige",bg="OrangeRed4",width = 12,font=myFont1).place(relx=0.469,rely=0.66)

    b19 = Button(new9, text="Cuttack",command=cuttack,fg="beige",bg="OrangeRed4",width = 12 ,font=myFont1).place(relx=0.469,rely=0.80)
    canvas11.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas11.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    t16 = canvas11.create_text(357, 30, text="Welcome to Odisha", font=('Helvetica', 50, 'bold'), fill="coral4",
                             anchor="nw")
    t17 = canvas11.create_text(700, 300, text='''Odisha, formerly called Orissa, is located in the northeastern part of the country, it is bounded by the states of Jharkhand and West Bengal to the north and northeast, by the Bay of Bengal to the east, and by the states of Andhra Pradesh and Telangana to the south and Chhattisgarh to the west. Odisha is located in a climatic region known as tropical wet-dry (or tropical savanna).Odisha has a rich artistic heritage and has produced some of the finest examples of Indian art and architecture. Among the most-notable traditions in the visual arts are mural painting, stone carving, wood carving, icon painting (known as patta), and painting on palm leaves.For the promotion of dancing and music, the Kala Vikash Kendra centre was founded at Cuttack in 1952, and it has continued to be a prominent arts performance and training venue in Odisha.''',width = 1200, font=('Helvetica', 17 ,'italic'),fill="red4")


def uttarpradesh():
    new10 = Toplevel()
    img13 = PhotoImage(file="statesbg.png")
    canvas11 = Canvas(new10)
    canvas11.image = img13
    canvas11.pack(fill="both", expand=True)
    canvas11.create_image(0, 0, image=img13, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new10, text="Lucknow",command=lucknow, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.66)

    Button(new10, text="Agra",command=agra, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.80)
    canvas11.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas11.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas11.create_text(317, 30, text="Welcome to Uttar Pradesh", font=('Helvetica', 50, 'bold'), fill="coral4",
                               anchor="nw")
    canvas11.create_text(700, 300, text='''Uttar Pradesh is the largest state in India by population.Uttar Pradesh is a popular travel destination in India. The climate of Uttar Pradesh is the tropical monsoon type, with warm weather year-round.Most of the festivals and holidays in the state are tied to the Hindu calendar. They include Dussehra, celebrating the victory of Rama over Ravana, the symbol of evil on earth; Diwali, a festival of lights devoted to Lakshmi, the goddess of wealth; Shivaratri, a day devoted to the worship of the god Shiva; Holi, a colourful spring festival; and Janmashtami, celebrating the birthday of the god Krishna.Thanks to it’s large population and area, the state of Uttar Pradesh has highest number of Lok Sabha constituencies.Many popular tourist attractions are located in the state, such as Taj Mahal, Agra Fort, Dayal Bagh, Fatehpur Sikri, Ganga River, Yamuna River, Baby Taj, Bara Imambara, and many more. The state is blessed with countless tourist attractions. ''', width = 1200, font=('Helvetica', 17, 'italic'), fill="red4")


def nagaland():
    new11 = Toplevel()
    img14 = PhotoImage(file="statesbg.png")
    canvas10 = Canvas(new11)
    canvas10.image = img14
    canvas10.pack(fill="both", expand=True)
    canvas10.create_image(0, 0, image=img14, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new11, text="Kohima",command=kohima, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.66)

    Button(new11, text="Ungma",command=ungma, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.80)
    canvas10.create_text(447, 510, text='''The capital city is:''', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas10.create_text(357, 600, text='''One of the important cities is:''', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas10.create_text(357, 50, text='''Welcome to Nagaland''', font=('Helvetica', 50, 'bold'), fill="coral4",
                               anchor="nw")
    canvas10.create_text(700, 300, text='''Nagaland is one of the smaller states of India. Nagaland is bounded by the Indian states of Arunachal Pradesh to the northeast, Manipur to the south, and Assam to the west and northwest and the country of Myanmar (Burma) to the east. The state capital is Kohima.Nearly all of Nagaland is mountainous. In the north the Naga Hills rise abruptly from the Brahmaputra valley to about 2,000 feet (610 metres).A central feature of Naga life is the Feast of Merit, a series of ceremonies culminating with the sacrifice of a mithan (a domesticated guar). Each tribe has its gennas, or festivals, and Naga dance, music, song, and folklore all express an exuberant concern for life.''', width = 1200, font=('Helvetica', 19, 'italic'), fill="red4")


def tripura():
    new12 = Toplevel()
    img11 = PhotoImage(file="statesbg.png")
    canvas10 = Canvas(new12)
    canvas10.image = img11
    canvas10.pack(fill="both", expand=True)
    canvas10.create_image(0, 0, image=img11, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new12, text="Agartala",command=agartala ,fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.66)

    Button(new12, text="Dharmanagar",command=dharmanagar, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.80)
    canvas10.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas10.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas10.create_text(367, 30, text="Welcome to Tripura", font=('Helvetica', 50, 'bold'), fill="coral4",
                               anchor="nw")
    canvas10.create_text(700, 300, text='''Tripura is located in the northeastern part of the subcontinent. It is bordered to the north, west, and south by Bangladesh, to the east by the state of Mizoram, and to the northeast by the state of Assam.The capital is Agartala . Two of Tripura’s largest festivals are the Kharchi Puja and the Garia. The Kharchi Puja—also known as the Festival of the 14 Gods—has its origins in tribal tradition but is now a major temple festival celebrated within a predominantly Hindu framework by both tribal and nontribal peoples; it takes place in Agartala every July and honours the deities and the Earth.The Garia celebration is a prominent festival of the indigenous population and is associated particularly with the Tripuri people. Garia is held each April following the planting of the fields to pray for a successful agricultural year.''', width = 1200, font=('Helvetica', 17, 'italic'), fill="red4")


def sikkim():
    new13 = Toplevel()
    img11 = PhotoImage(file="statesbg.png")
    canvas10 = Canvas(new13)
    canvas10.image = img11
    canvas10.pack(fill="both", expand=True)
    canvas10.create_image(0, 0, image=img11, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new13, text="Gangtok",command=gangtok, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.66)

    Button(new13, text="Lachung",command=lachung, fg="beige", bg="OrangeRed4", width = 12, font=myFont1).place(relx=0.469,rely=0.80)
    canvas10.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas10.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas10.create_text(387, 30, text="Welcome to Sikkim", font=('Helvetica', 50, 'bold'), fill="coral4",
                               anchor="nw")
    canvas10.create_text(700, 300, text='''Sikkim, state of India, located in the northeastern part of the country, in the eastern Himalayas. It is one of the smallest states in India. Sikkim is bordered by the Tibet Autonomous Region of China to the north and northeast, by Bhutan to the southeast, by the Indian state of West Bengal to the south, and by Nepal to the west. The capital is Gangtok, in the southeastern part of the state.Sikkim is a basin surrounded on three sides by precipitous mountain walls. There is little lowland, and the variation in relief is extreme.The most important festival of the year is the two-day Phanglhapsol festival in August or September, in which masked dancers perform in honour of Kanchenjunga, the presiding deity. ''',width = 1200, font=('Helvetica', 19, 'italic'), fill="red4")

def meghalaya():
    new13 = Toplevel()
    img11 = PhotoImage(file="statesbg.png")
    canvas10 = Canvas(new13)
    canvas10.image = img11
    canvas10.pack(fill="both", expand=True)
    canvas10.create_image(0, 0, image=img11, anchor="nw")
    myFont1 = font.Font(family="Helvetica", size=30, weight='bold')
    Button(new13, text="Shillong",command=shillong, fg="beige", bg="OrangeRed4", width = 15, font=myFont1).place(relx=0.469,rely=0.66)

    Button(new13, text="Cherrapunji",command=cherrapunji, fg="beige", bg="OrangeRed4", width = 15, font=myFont1).place(relx=0.469,rely=0.80)
    canvas10.create_text(447, 510, text='The capital city is:', font=('Helvetica', 28, 'bold'), fill='coral4')
    canvas10.create_text(357, 600, text='One of the important cities is:', font=('Helvetica', 28, 'bold'),fill='coral4')
    canvas10.create_text(327, 30, text="Welcome to Meghalaya", font=('Helvetica', 50, 'bold'), fill="coral4",anchor="nw")
    canvas10.create_text(700, 300, text=
    ''' 
     Meghalaya is bounded by the Indian state of Assam to the north and northeast and by Bangladesh to the south and
     southwest. The state capital is the hill town of Shillong, located in east-central Meghalaya.Meghalaya—alaya 
     (“abode”) and megha (“of the clouds”)—occupies a mountainous plateau of great scenic beauty.One of the world’s 
     wettest regions is found in Meghalaya—Cherrapunji, which has an average annual precipitation of about 450 inches 
     (11,430 mm) during monsoon season (from May to September). Drinking and dancing to the accompaniment of music 
     from singas (buffalo horns), bamboo flutes, and drums are integral parts of religious ceremonies and
     social functions. 
    ''', font=('Helvetica', 18, 'italic'), fill="red4")