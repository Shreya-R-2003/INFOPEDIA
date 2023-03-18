from tkinter import *
from PIL import ImageTk, Image
def amar():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="amaravati.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill = "both", expand = True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 90, text = '''AMARAVATI''', fill = "green", activefill = None, font = ("ALGERIAN", 40, "bold"))
    canvas.create_text(500, 390, text='''Amaravati is a proposed city and the capital of the Indian state of Andhra Pradesh. The city is located on the banks of river Krishna in Guntur District.

The Prime Minister of India, Narendra Modi laid the foundation stone at a ceremonial event in Uddandarayunipalem village on 22 October 2015.

The office of the Chief Minister of Andhra Pradesh has operated from Velagapudi since April 2016. The Andhra Pradesh Legislature remained in Hyderabad until March 2017, when it was relocated to newly constructed interim legislative buildings in Velagapudi.''', width = 800, fill="black", activefill = None,  font = ("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))
def srihk():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="sriharikota.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill = "both", expand = True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text = '''SRIHARIKOTA''', fill = "green", activefill = None, font = ("ALGERIAN", 40, "bold"))
    canvas.create_text(500, 370, text='''Sriharikota is a barrier island off the Bay of Bengal coast located in the Shar Project settlement of Nellore district in Andhra Pradesh, India.
    
    It houses the Satish Dhawan Space Centre, one of the two satellite launch centres in India (the other being the Thumba Equatorial Rocket Launching Station in Thiruvananthapuram).
    
    Indian Space Research Organisation (ISRO) launches satellites using multistage rockets such as the Polar Satellite Launch Vehicle and the Geosynchronous Satellite Launch Vehicle from Sriharikota.''', width = 800, fill="black", activefill = None,  font = ("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def mum():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="mumbai.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''MUMBAI''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(560, 370, text='''Mumbai, also known as Bombay, (the official name until 1995) is the capital city of the Indian state of Maharashtra. According to the United Nations, as of 2018, Mumbai is the second-most populous city in India after Delhi and the eighth-most populous city in the world with a population of roughly 2 crore (20 million).
    
    As per the Indian government population census of 2011, Mumbai was the most populous city in India with an estimated city proper population of 1.25 crore (12.5 million) living under the Municipal Corporation of Greater Mumbai.
    
    Mumbai is the centre of the Mumbai Metropolitan Region, the sixth most populous metropolitan area in the world with a population of over 2.3 crore (23 million).Mumbai lies on the Konkan coast on the west coast of India and has a deep natural harbour. In 2008, Mumbai was named an alpha world city.It has the highest number of millionaires and billionaires among all cities in India.
    
    Mumbai is home to three UNESCO World Heritage Sites: the Elephanta Caves, Chhatrapati Shivaji Maharaj Terminus, and the city's distinctive ensemble of Victorian and Art Deco buildings designed in the 19th and 20th centuries.''',width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 15, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def pune():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="pune.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''PUNE''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 400, text='''Pune, formerly known as Poona, (the official name until 1978) is the seventh most populous city in India and the second-largest city in the state of Maharashtra, with an estimated population of 7.4 million as of 2020.
    It has been ranked as "the most liveable city in India" several times.
Along with the municipal corporation limits of PCMC and the three cantonment towns of Camp, Khadki and Dehu Road, Pune forms the urban core of the eponymous Pune Metropolitan Region (PMR).''',
                       width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 24, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))
def ita():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="itanagar.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''ITANAGAR''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Itanagar is the capital and largest city of the Indian state of Arunachal Pradesh. The seat of Arunachal Pradesh Legislative Assembly, the seat of government of Arunachal Pradesh, and the seat of Gauhati High Court permanent bench at Naharlagun are all in Itanagar
    Ita Fort, one of the most important historical sites in the state of Arunachal Pradesh. The name literally means "Fort of bricks"( brick being called "Ita" in the Assamese language).The Ita Fort was built as early as the 14th or the 15th century. The fort has an irregular shape, built mainly with bricks dating back to the 14th-15th Century.
    The total brickwork is of 16,200 cubic meter lengths which have been identified by some scholars with the Chutiya kingdom.The fort has three different entrances at three different sides, which are western, eastern, and southern sides.''',
                       width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 19, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def tez():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="tezu.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''TEZU''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Tezu is a census town and the headquarters of Lohit district in the Indian state of Arunachal Pradesh.
    It is the fifth largest town in Arunachal Pradesh and one of its most developed. The major Mishmi God is Ringyajabmalu and the major Mishmi festival is known as Tamladu puja.It is celebrated each year on 15 February.
    People from all communities and all walks of life are invited to join in the celebrations.
    The Holy Parshuram Kund is also nearby and thousands of Hindu pilgrims from all over India, and also from neighbouring countries, come to take a holy dip and wash away the sins of millions of births. This is accompanied with a fair at Tezu and takes place every year during the month of January.The major agricultural products are mustard, ginger and oranges.''',
                       width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 19, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def disp():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="dispur.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''DISPUR''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Dispur is the capital of the Indian state of Assam and is a sub-urban locality located at Guwahati.

It became the capital in 1973, when Shillong the erstwhile capital, became the capital of the state of Meghalaya that was carved out of Assam.
Dispur is the seat of power of Government of Assam. The Assam Secretariat (Janata Bhawan) building is located in Dispur along with the Assam Legislative Assembly House, MLA Hostels and the State Emergency Operations Centre. The Assam Trunk road and the G S road passes through Dispur.
To the south of Dispur lies the theologically important site of Basistha Ashram and the Shankardev Kalakshetra, a cultural centre created in the 1990s. Next to Dispur is the township of Jatia.
Though it is well known as the capital of Assam, Dispur is also known for the Guwahati Tea Auction Centre.''',
                       width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 15, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def dib():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="dibrugarh.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''DIBRUGARH''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Dibrugarh is an Industrial city in Upper Assam with sprawling tea gardens. Located 435 km East from the state capital Dispur.
    
    It serves as the headquarters of Dibrugarh district in the state of Assam in India. Dibrugarh serves as the headquarters of the Sonowal Kachari Autonomous Council, which is the governing council of the Sonowal Kachari tribe (found predominantly in the Dibrugarh district).
    
    Currently, the city Master Plan area of Dibrugarh is 71.83 km² and population is 154,296. Dibrugarh railway station under the Tinsukia railway division of Northeast Frontier Railway Zone acts as the top largest Railway Junction in entire Northeast India. Also it is the largest city in Upper Assam Region.''',
                       width=1000, fill="black", activefill=None, font=("Bahnschrift SemiLight SemiConde", 18, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def pat():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="patna.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''PATNA''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Patna historically known as Pataliputra, is the capital and largest city of the state of Bihar in India.
    
    According to the United Nations, as of 2018, Patna had a population of 2.35 million, making it the 19th largest city in India.Covering 250 square kilometres (97 sq mi) and over 2.5 million people, its urban agglomeration is the 18th largest in India. Patna serves as the seat of Patna High Court.
    
    The Buddhist, Hindu and Jain pilgrimage centres of Vaishali, Rajgir, Nalanda, Bodh Gaya and Pawapuri are nearby and Patna City is a sacred city for Sikhs as the tenth Sikh Guru, Guru Gobind Singh was born here.The modern city of Patna is mainly on the southern bank of the river Ganges. The city also straddles the rivers Sone, Gandak and Punpun. The city is approximately 35 kilometres (22 mi) in length and 16 to 18 kilometres (9.9 to 11.2 mi) wide.''',
                       width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 15, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def vaish():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="vaishali.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''VAISHALI''', fill="green", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Vaishali derives its name from King Vishal. Even before the advent of Buddhism and Jainism, Vaishali was the capital of the vibrant Vajji confederation, since before the birth of Mahavira (c. 599 BC), which suggests that it was the first republic in the world, similar to those later found in ancient Greece.
        In that period, Vaishali was an ancient metropolis and the capital city of the republic of the Vajji confederation of Mithila, which covered most of the Himalayan Gangetic region of present-day Bihar.''',
                       width=1000, fill="black", activefill=None, font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def rai():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="raipur.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''RAIPUR''', fill="green", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(590, 400, text='''Raipur is the capital city of the Indian state of Chhattisgarh. Raipur is also the administrative headquarters of Raipur district and Raipur division, and the largest city of the state.
    It was a part of Madhya Pradesh before the state of Chhattisgarh was formed on 1 November 2000.It has exponential industrial growth, and has become a major business hub in Central India. It has been ranked as India's 6th cleanest city as per the Swachh Survekshan for the year 2021.
    Raipur is ranked 7th in Ease of Living Index 2019 and 7th in Municipal Performance Index 2020 by Union Ministry of Housing and Urban Affairs (MoHUA).''',
                       width=1000, fill="black", activefill=None, font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def bhil():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="bhilai.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''BHILAI''', fill="green", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(600, 400, text='''Bhilai is a city in the Indian state of Chhattisgarh, in eastern central India. With a population of 1,064,077, Bhilai is the second-largest urban area in Chhattisgarh after Raipur.
    Bhilai is a major industrial city in India as well as an education hub of central India. The Bhilai metropolis contains three municipal corporations: Bhilai Municipal Corporation, Bhilai-Charoda Municipal Corporation and Risali Municipal Corporation.
    Bhilai is home to the Bhilai Steel Plant, the first Indian plant to produce steel rails and the inauguration of the first blast furnace of Bhilai Steel Plant done by then president of India Dr. Rajendra Prasad, which was established with help from the Soviet Union in 1955.''',
                       width=1000, fill="white", activefill=None, font=("Bahnschrift SemiLight SemiConde", 23, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def panaj():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="panaji.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''PANAJI''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(600, 400, text='''Panaji is the capital of the Indian state of Goa and the headquarters of North Goa district. Previously, it was the territorial capital of the former Portuguese India. It lies on the banks of the Mandovi river estuary in the Tiswadi sub-district (tehsil). With a population of 114,759 in the metropolitan area, Panaji is Goa's largest urban agglomeration, ahead of Margao and Mormugao.

Panaji has terraced hills, concrete buildings with balconies and red-tiled roofs, churches, and a riverside promenade. There are avenues lined with gulmohar, acacia and other trees. The baroque Our Lady of the Immaculate Conception Church is located overlooking the main square known as Praça da Igreja. Panaji has been selected as one of hundred Indian cities to be developed as a smart city under the Smart Cities Mission.

The city was built with stepped streets and a seven kilometre long promenade on a planned grid system after the Portuguese relocated the capital from Velha Goa in the 17th century.It was elevated from a town to a city on 22 March 1843.''',
                       width=1000, fill="black", activefill=None, font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def madg():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="madgaon.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''MADGAON''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(640, 440, text='''Margao or Madgaon is the commercial capital of the Indian state of Goa. It stands on banks of the Sal river and is the administrative headquarters of Salcete sub-district and South Goa district. It is Goa's second largest city by population after Vasco.
    Margão is the Portuguese spelling, with मडगांव (Madgao) being used in Konkani. One theory holds that the name is derived from the Sanskrit मठग्राम (Maṭhagrāma) which means "a village of monasteries".
    Another theory drawing from popular history suggests that is that the name in fact derives from its being the settlement of the caste of Mahars, hence "Mahar gão" (village of Mahars).''',
                       width=1000, fill="green yellow", activefill=None, font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def gan():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="gandhinagar.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''GANDHINAGAR''', fill="green", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 440, text='''Gandhinagar is the capital of the state of Gujarat in India. Gandhinagar is located approximately 23 km north of Ahmedabad, on the west central point of the Industrial corridor between Delhi, the political capital of India, and Mumbai, the financial capital of India.

Gandhinagar lies on the west bank of the Sabarmati River, about 545 km (338 miles) north of Mumbai and 901 km (560 miles) southwest of Delhi. The Akshardham temple is located in Gandhinagar.

There was a determination to make Gandhinagar a purely Indian enterprise, partly because the state of Gujarat was the birthplace of Mahatma Gandhi. For this reason, the planning was done by two Indian town planners: Prakash M Apte and H. K. Mewada, who had apprenticed with Le Corbusier in Chandigarh.''',
                       width=1000, fill="black", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def amd():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="ahmedabad.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''AHMEDABAD''', fill="green", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 440, text='''Ahmedabad, also known as amdavad, is the most populous city in the Indian state of Gujarat. It is the administrative headquarters of the Ahmedabad district and the seat of the Gujarat High Court.
    
    Ahmedabad's population of 8,253,000 (as per 2021 population-census) makes it the fifth-most populous city in India, and the encompassing urban agglomeration population estimated at 6,357,693 is the seventh-most populous in India. Ahmedabad is located near the banks of the Sabarmati River, 25 km (16 mi) from the capital of Gujarat, Gandhinagar, also known as its twin city.
    
    The Indian independence movement developed roots in the city when Mahatma Gandhi established two ashrams – the Kochrab Ashram near Paldi in 1915 and the Satyagraha Ashram (now Sabarmati Ashram) on the banks of the Sabarmati in 1917 – which would become centres of nationalist activities.''',
                       width=1000, fill="white", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def guru():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="gurugram.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''GURUGRAM''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 440, text='''Gurgaon, officially named Gurugram, is a city located in the northern Indian state of Haryana. It is situated near the Delhi–Haryana border, about 30 kilometres (19 mi) southwest of the national capital New Delhi and 268 km (167 mi) south of Chandigarh, the state capital.
    
    It is one of the major satellite cities of Delhi and is part of the National Capital Region of India.[6] As of 2011, Gurgaon had a population of 1,153,000.
    
    Gurgaon is India's second largest information technology hub and third largest financial and banking hub. Gurgaon is also home to India's largest medical tourism industry.''',
                       width=1000, fill="white", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def shim():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="shimla.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''SHIMLA''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 440, text='''Shimla also known as Simla, the official name until 1972) is the capital and the largest city of the Northern Indian state of Himachal Pradesh.
    
    In 1864, Shimla was declared as the summer capital of British India. After independence, the city became the capital of Punjab and was later made the capital city of Himachal Pradesh.
    
    It is the principal commercial, cultural and educational centre of the state. It was the capital city in exile of British Burma (present-day Myanmar) from 1942 to 1945.''',
                       width=1000, fill="white", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def dhar():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="dharmasala.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(700, 70, text='''DHARMASHALA''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 420, text='''Dharamshala, also speled as dharmasala is the winter capital city of Himachal Pradesh, India.
    
    It has served as the location for the administrative headquarters of the Kangra district after they were relocated from Kangra, a city located 18 kilometres (11 mi) away from Dharamshala, in 1855.
    
     The McLeod Ganj town, lying in the upper reaches, is known worldwide for the presence of the Dalai Lama.
     
     Several thousand Tibetan exiles have now settled in the area; most live in and around McLeod Ganj in Upper Dharamshala, where they have built monasteries, temples and schools. It has become an important tourist destination with many hotels and restaurants, leading to growth in tourism and commerce.''',
                       width=1000, fill="white", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def manl():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="manali.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''MANALI''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 420, text='''Manali is a town in the Indian state of Himachal Pradesh. It is situated in the northern end of the Kullu Valley, formed by the Beas River. The town is located in the Kullu district, approximately 270 kilometres (170 mi) north of the state capital of Shimla and 544 kilometres (338 mi) northeast of the national capital of Delhi.
    
    With a population of 8,096 people recorded in the 2011 Indian census Manali is the beginning of an ancient trade route through Lahaul and Ladakh, over the Karakoram Pass and onto Yarkand and Hotan in the Tarim Basin of China. Manali is a popular tourist destination in India and serves as the gateway to the Lahaul and Spiti district as well as the city of Leh in Ladakh.''',
                       width=1000, fill="black", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 17, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def ranch():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="ranchi.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''RANCHI''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 420, text='''Ranchi is the capital of the Indian state of Jharkhand. Ranchi was the centre of the Jharkhand movement, which called for a separate state for the tribal regions of South Bihar, northern Orissa, western West Bengal and the eastern area of what is present-day Chhattisgarh. The Jharkhand state was formed on 15 November 2000 by carving out the Bihar divisions of Chota Nagpur and Santhal Parganas. Ranchi has been selected as one of the hundred Indian cities to be developed as a smart city under PM Narendra Modi's flagship Smart Cities Mission.''',
                       width=1000, fill="white", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def jam():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="jamshedpur.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''JAMSHEDPUR''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(670, 420, text='''Jamshedpur or Tatanagar is the largest and most populous city in Jharkhand and first planned industrial city in India. It was ranked as the cleanest city of India in the year 2019.

It was founded by Jamsetji Tata, founder of Tata Groups in the 1900s, and was named after him. It was established in 1919.

Jamshedpur was ranked as the 13th cleanest city of India in 2020 by Swach Survekshan in 2020.[11] Jamshedpur was ranked the 7th cleanest city of India in 2010.[12] The city is also ranked as 2nd in India in terms of 'Quality of Life'. Jamshedpur is the 84th fastest growing city in the world according to City Mayors Foundation.
It is the headquarters of the East Singhbhum district of Jharkhand and is the 36th – largest urban agglomeration. And 72nd largest city in India by population.''',
                       width=1000, fill="white", activefill=None, justify="center",
                       font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def hyd():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="hyderabad.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''HYDERABAD''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(500, 420, text='''Hyderabad is the capital and largest city of the Indian state of Telangana and the de jure capital of Andhra Pradesh.
    It occupies 650 km2 (250 sq mi) on the Deccan Plateau along the banks of the Musi River, in the northern part of South India. With an average altitude of 542 m (1,778 ft), much of Hyderabad is situated on hilly terrain around artificial lakes, including the Hussain Sagar lake, predating the city's founding, in the north of the city centre.
    According to the 2011 Census of India, Hyderabad is the fourth-most populous city in India with a population of 6.9 million residents within the city limits, and has a population of 9.7 million residents in the metropolitan region, making it the sixth-most populous metropolitan area in India. With an output of US$74 billion, Hyderabad has the fifth-largest urban economy in India.''',
                       width=800, fill="black", activefill=None, justify="left",
                       font=("Bahnschrift SemiLight SemiConde", 20, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def war():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="warangal.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''WARANGAL''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(500, 420, text='''Warangal is a city in the Indian state of Telangana. It is the second largest city in Telangana with a population of 830,281 per 2011 Census of India, and spreading over an 406 km2 (157 sq mi).
    
    Warangal served as the capital of the Kakatiya dynasty which was established in 1163. The monuments left by the Kakatiyas include fortresses, lakes, temples and stone gateways which, in the present, helped the city to become a popular tourist attraction.
    
    The Kakatiya Kala Thoranam was included in the emblem of Telangana by the state government and Warangal is also touted as the cultural capital of Telangana.''',
                       width=800, fill="black", activefill=None, justify="left",
                       font=("Bahnschrift SemiLight SemiConde", 20, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def imp():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="imphal.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''IMPHAL''', fill="white", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(580, 420, text='''Imphal is the capital city of the Indian state of Manipur. The metropolitan centre of the city contains the ruins of Kangla Palace (also known as Kangla Fort), the royal seat of the former Kingdom of Manipur, surrounded by a moat. Spread over parts of the districts of Imphal West and Imphal East, the former contains the majority of the city's area and population.
    Imphal is part of the Smart Cities Mission under the Ministry of Housing and Urban Affairs.
    Imphal offers sites of religious and historical importance within and around the city. Kangla Palace (also known as Kangla Fort) is on the banks of the Imphal River. Kangla means "dry land" in the Meitei language. It was the palace of King Pakhangba, and has religious significance with multiple temples present within the complex.''',
                       width=1000, fill="white", activefill=None, justify="left",
                       font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def thou():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="thoubal.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''THOUBAL''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(580, 420, text='''Thoubal is a town, a municipal council with 18 municipal wards and district Headquarters in Thoubal district in the Indian state of Manipur. The name 'Thoubal' comes from 'Athouba' meaning brave people symbolising the courageous people of the district. It is one of the larger towns of Manipur. It is idyllic and has many lakes and rivers, paddy fields, and gardens. It is also the window to South-East Asia as the Trans-Asian highway (AH1) passes through it. It is well connected with Imphal, Kakching, Moreh, and Yairipok.

The main attractions include Chinga Lairembi temple, Tenjing ching, Panthoibee temple, Thoubal bazar, Tangjeng ching(from where one can have a bird's eye view of waithou lake) and Khangabok Menjor garden.''',
                       width=1000, fill="white", activefill=None, justify="left",
                       font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def kol():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="kolkata.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''KOLKATA''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(580, 420, text='''Kolkata the official name until 2001) is the capital of the Indian state of West Bengal.
    Located on the eastern bank of the Hooghly River, the city is approximately 80 kilometres (50 mi) west of the border with Bangladesh.
    It is the primary business, commercial, and financial hub of Eastern India and the main port of communication for North-East India.[17] According to the 2011 Indian census, Kolkata is the seventh-most populous city in India, with a population of 45 lakh (4.5 million) residents within the city limits, and a population of over 1.41 crore (14.1 million) residents in the Kolkata Metropolitan Area. It is the third-most populous metropolitan area in India.
    In 2021, Kolkata metropolitan area crossed 1.5 crore (15 million) registered voters. The Port of Kolkata is India's oldest operating port and its sole major riverine port. Kolkata is regarded as the Cultural Capital of India.''',
                       width=1000, fill="white", activefill=None, justify="left",
                       font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))

def darj():
    amarwin = Toplevel()
    amarimg = ImageTk.PhotoImage(file="darjeeling.png")
    canvas = Canvas(amarwin)
    canvas.image = amarimg
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=amarimg)
    canvas.create_text(680, 70, text='''DARJEELING''', fill="black", activefill=None, font=("ALGERIAN", 40, "bold"))
    canvas.create_text(580, 420, text='''Darjeeling is a city and a municipality in the Indian state of West Bengal. It lies in the Lesser Himalayas at an elevation of 2,000 metres (6,560 ft).
    It is noted for its tea industry, its scenic views of the world's third-highest mountain Kangchenjunga, and the Darjeeling Himalayan Railway, a narrow-gauge mountain railway which is on the UNESCO World Heritage List.
    Darjeeling is the headquarters of the Darjeeling district which has a partially autonomous status called Gorkhaland Territorial Administration within the state of West Bengal. It is also a popular tourist destination in India.''',
                       width=1000, fill="black", activefill=None, justify="left",
                       font=("Bahnschrift SemiLight SemiConde", 22, "bold"))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def blore():
    c1 = Toplevel()
    img1 = PhotoImage(file="blore1.png")
    canvas = Canvas(c1)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(740, 70, text="BANGALORE", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(600, 400, text=
    ''' 
    Bangalore is one of the fastest-growing cities in India, situated in Karnataka. 
    It is popularly known as the Silicon Valley of India and Garden City of India.

    The climate of Bangalore is pleasant. So, tourists mainly visit the city 
    during winter to witness the flower blossom with vibrant colours.
    Bangalore is famously called the Garden City because of its beautiful gardens.

    The city also includes numerous technology companies, public sector heavy industries, 
    aerospace, defence organisations and telecommunications.
    For example,Bharat Electronics Limited (BEL).

    Major tourist destinations include Cubbon Park, Botanical Garden Lalbagh,
    Bangalore Palace,Nandi or Bull temple, etc.
    '''
                       , font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1180, 660, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def mysore():
    c2 = Toplevel()
    img1 = PhotoImage(file="m5.png")
    canvas = Canvas(c2)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="MYSORE", font=('ALGERIAN', 48, 'bold'), fill='dark slate blue')
    canvas.create_text(670, 340, text=
    '''
    Mysore is a city in the Indian state of Karnataka, and the administrative
    seat of Mysore District,one of the largest districts in Karnataka. 
    Patrons of art and culture the Wodeyars ruled Mysore kingdom and contributed
    significantly to the cultural growth of Mysore city.

    Mysore, the cultural capital of the Karnataka state, has many educational,
    commercial, administrative centers and heritage monuments.The city with the 
    majestic Mysore Palace, the royal mansions,public buildings,gardens, water bodies
    and planned markets exhibit an indelible impression of the vision of the Maharajas.

    The total harmony of buildings,sites, lakes,parks and open spaces of Mysore
    and the back drop of Chamundi hill adds to the city’s attraction.
    ''', justify="center", font=('Bahnschrift SemiLight SemiConde', 20, 'bold'), fill='RoyalBlue4')
    canvas.create_text(1180, 670, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def chennai():
    c3 = Toplevel()
    img1 = PhotoImage(file="c2.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="CHENNAI", font=('ALGERIAN', 48, 'bold'), fill='RoyalBlue4')
    canvas.create_text(680, 300, text='''
    Chennai is the capital of the Indian state of Tamil Nadu. Located on the Coromandel Coast off the
    Bay of Bengal,it is one of the biggest cultural, economic and educational centres in South India.

    The city together with the adjoining regions constitute the Chennai Metropolitan Area, which is 
    the 36th-largest urban area by population in the world. Chennai is one of the Indian cities most 
    visited by foreign tourists,and is the 47th most visited city in the world. 

    The Quality of Living Survey rated Chennai as the safest city in India.Chennai attracts 45 percent 
    of health tourists visiting India, and 30 to 40 percent of domestic health tourists.As such, 
    it is termed "India's health capital".
    ''', font=('Bahnschrift SemiLight SemiConde', 20, 'bold'), fill='midnight blue')
    canvas.create_text(1180, 670, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def madurai():
    c3 = Toplevel()
    img1 = PhotoImage(file="madurai5.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="MADURAI", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(670, 330, text='''
    Madurai is a major city and cultural headquarters in the state of Tamil Nadu in India. It is the 
    administrative headquarters of Madurai District and the 31st largest urban agglomeration in India. 
    Madurai is the third largest city by population in Tamil Nadu.

    Located on the banks of River Vaigai,Madurai has been a major settlement for two millennia
    and is one of the oldest continuously inhabited cities in the world.The city is believed to 
    be of significant antiquity and has been ruled, at different times,by the Pandyas, Cholas,
    Madurai Sultanate, Vijayanagar Empire, Madurai Nayaks, Carnatic kingdom, and the British.

    The city has a number of historical monuments,with the Meenakshi Amman Temple and Tirumalai 
    Nayak Palace being the most prominent.
    ''', font=('Bahnschrift SemiLight SemiConde', 20, 'bold'), fill='RoyalBlue4')
    canvas.create_text(1180, 670, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def thiruvananthapuram():
    c3 = Toplevel()
    img1 = PhotoImage(file="tri2.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="THIRUVANANTHAPURAM", font=('ALGERIAN', 48, 'bold'),
                       fill='midnight blue')
    canvas.create_text(950, 370, text='''
    Thiruvananthapuram formerly known as Trivandrum, is the capital 
    and the largest city of the Indian state of Kerala.It is located
    on the west coast of India near the extreme south of the mainland.

    Referred to by Mahatma Gandhi as the "Evergreen city of India",
    it is classified as a Tier-II city by the Government of India.
    Thiruvananthapuram was a trading post for spices, sandalwood 
    and ivory.

    The city was ruled by the Ays and was captured by 
    the rulers of Venad in tenth century A.D. In 1729, Marthanda Varma 
    founded the princely state of Thiruvithamkoor and made 

    Thiruvananthapuram the capital in 1745. It remained as a princely 
    state ruled by Travancore under the loose governance of the British
    before joining the Indian Union in 1948. 
    ''', fill = "white", justify="center", font=('Bahnschrift SemiLight SemiConde', 15, 'bold'))
    canvas.create_text(1180, 670, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def kochi():
    c3 = Toplevel()
    img1 = PhotoImage(file="kochi.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="KOCHI", font=('ALGERIAN', 48, 'bold'), fill='red4')
    canvas.create_text(650, 300, text='''
    Kochi also known as Cochin (ko-chin), is a major port city on the south-west coast of India by 
    the Arabian Sea and the Laccadive Sea and is part of the district of Ernakulam in the state
    of Kerala.
    It is often called Ernakulam, which refers to the mainland part of the city. With a corporation
    limit population of 612,343, and metropolitan population of 2.1 million, Kochi city
    is also a part of the Greater Cochin region and is classified as a Tier-II city
    by the Government of India.
    Kochi also known as the Queen of the Arabian Sea, was an important spice trading centre
    on the west coast of India from the 14th century onward, and maintained a trade
    network with Arab merchants from the pre-Islamic era.
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1180, 670, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def dehradun():
    c3 = Toplevel()
    img1 = PhotoImage(file="deh1.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="DEHRADUN", font=('ALGERIAN', 48, 'bold'), fill='RoyalBlue4')
    canvas.create_text(740, 400, text=
    '''
    Dehradun or Dehra Dun is the capital city of the state of Uttarakhand 
    in the northern part of India. Dehradun is in the Doon Valley on the foothills
    of the Himalayas nestled between the river Ganges on the east and the river Yamuna
    on the west.

    The city is famous for its picturesque landscape and slightly milder 
    climate and provides a gateway to the surrounding region. It is well connected and 
    in proximity to Himalayan tourist destinations such as Mussoorie, and Auli and the
    Hindu holy cities of Haridwar and Rishikesh along with the Himalayan pilgrimage
    circuit of Chota Char Dham.

    Located in the Garhwal region, it lies 236 kilometres (147 mi)
    north of India's capital New Delhi and is one of the "Counter Magnets" of the
    National Capital Region (NCR) being developed as an alternative centre of growth
    to help ease the migration and population explosion in the Delhi metropolitan area.
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'), fill='midnight blue')
    canvas.create_text(1180, 670, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 15, 'bold'))


def kedarnath():
    c3 = Toplevel()
    img1 = PhotoImage(file="kedarnath1.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(700, 60, text="KEDARNATH", font=('ALGERIAN', 48, 'bold'), fill='RoyalBlue4')
    canvas.create_text(660, 420, text=
    '''
    Kedarnath is a town located in the Indian state of Uttarakhand and has gained
    importance because of Kedarnath Temple. It is a nagar panchayat in Rudraprayag
    district. The most remote of the four Chota Char Dham sites, Kedarnath is 
    located in the Himalayas, about 3,583 m (11,755 ft) above sea level near 
    Chorabari Glacier, the head of river Mandakini, and is flanked by snow-capped
    peaks.

    The nearest road head is at Gaurikund. The town suffered extensive destruction
    during June 2013 from flash floods caused by torrential rains in Uttarakhand state.
    Other than Kedarnath temple, on the eastern side of the town is Bhairava temple
    and the deity of this temple, the Bhairava, is believed to protect the town during
    winter months.

    About 6 km upstream from the town, lies Chorabari Tal, a lake
    and glacier also called Gandhi Sarovar. 
    ''', justify="center", font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def chandigarh():
    c3 = Toplevel()
    img1 = PhotoImage(file="chandigarh1.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(700, 70, text="CHANDIGARH", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(660, 400, text=
    '''
     Chandigarh is bordered by the state of Punjab to the north, west and south, and to the state
     of Haryana to the east. Chandigarh is considered to be a part of the Chandigarh capital
     region or Greater Chandigarh, which includes Chandigarh, and the city of Panchkula
     (in Haryana) and cities of Kharar, Kurali, Mohali, Zirakpur (in Punjab).Chandigarh was
     one of the early planned cities in the post-independence India and is internationally 
     known for its architecture and urban design.

     It consists of many theme parks, botanical gardens and green belts, including Rajendra 
     Park in Sector 1, the Bougainvillea Garden in Sector 3 and the Physical Fitness Trails
     in Sector 10.Sukhna Lake is the venue for many festive celebrations. The most popular is 
     the Mango Festival held during the monsoons. 
    ''', justify="center", font=('Bahnschrift SemiLight SemiConde', 17, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def amritsar():
    c3 = Toplevel()
    img1 = PhotoImage(file="amritsar.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(750, 50, text="AMRITSAR", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 350, text=
    '''
    Amritsar historically also known as Ramdaspur and colloquially as Ambarsar, is a city
    in north-western India which is the administrative headquarters of the Amritsar district
    - located in the Majha region of the Indian state of Punjab. According to the 2011 census,
    the population of Amritsar was 1,132,761. The city is situated 217 km (135 mi) northwest
    of state capital Chandigarh.

    It is near Pakistan, with the Wagah Border being only 28 km
    (17.4 mi) away. The nearest city is Lahore, the second largest city in Pakistan, 
    located 50 km (31.1 mi) to the west. Hinduism and Sikhism are the main religions of 
    Amritsar city, practised by 49.4% and 48% of the total population, respectively. Amritsar
    is home to the Harmandir Sahib (commonly known as the Golden Temple), the spiritual and
    cultural centre for the Sikh religion. 
    ''', fill = "white" , font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def bhopal():
    c3 = Toplevel()
    img1 = PhotoImage(file="bhopal.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="BHOPAL", font=('ALGERIAN', 48, 'bold'), fill='RoyalBlue4')
    canvas.create_text(700, 400, text=
    '''
    Bhopal is the capital of the Indian state of Madhya Pradesh and the administrative headquarters
    of Bhopal district and Bhopal division. The city was the capital of the former Bhopal State.

    Bhopal is known as the City of Lakes for its various natural as well as artificial lakes and is 
    also one of the greenest cities in India. It is the 17th largest city in the country and 131st in
    the world.

    A Y-class city, Bhopal houses various institutions and installations of national
    importance, including ISRO's Master Control Facility and BHEL. Bhopal is home to the largest 
    number of Institutes of National Importance in India, namely IISER, MANIT, SPA, AIIMS and NLIU.

    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'), fill='midnight blue')
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def indore():
    c3 = Toplevel()
    img1 = PhotoImage(file="indore.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(715, 50, text="INDORE", font=('ALGERIAN', 48, 'bold'), fill='dark slate blue')
    canvas.create_text(650, 430, text=
    '''
    Indore is the most populous city of the Indian state of Madhya Pradesh.
    It serves as the headquarters of both Indore District and Indore Division.

    Indore was described by the Economic Times as the commercial capital
    of the state. It is also considered as an education hub of the state and
    houses campuses of both the Indian Institute of Technology and the Indian
    Institute of Management.

    Located on the southern edge of Malwa Plateau,
    the city is 190 km west of the state capital of Bhopal.

    With a census-estimated 2011 population of 2,170,295 (municipal corporation)
    and 3,254,238 (urban agglomeration), the Indore Metropolitan Area's
    population is the state's largest. 
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def jaipur():
    c3 = Toplevel()
    img1 = PhotoImage(file="jai1.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(710, 50, text="JAIPUR", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 300, text=
    '''
    Jaipur is the capital and largest city (in term of size) of the Indian state of Rajasthan in 
    Northern India. Jaipur is also known as the Pink City of India. Jaipur is a major tourist
    destination in India forming a part of the Golden Triangle.
    It was founded on 18 November 1726 by Maharaja Jai Singh II, the ruler of Amer after
    whom the city is named. As of 2011, the city has a population of 3.1 million,
    making it the tenth most populous city in the country.
    Located 260 km (162 miles) from the Indian capital New Delhi, Jaipur forms a part of the west
    Golden Triangle tourist circuit along with Agra (240 km, 149 mi). Jaipur is a popular tourist
    destination in India and serves as a gateway to other tourist destinations in Rajasthan such
    as Jodhpur (348 km, 216 mi), Jaisalmer (571 km, 355 mi) and Udaipur (421 km, 262 mi). 
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def jodhpur():
    c3 = Toplevel()
    img1 = PhotoImage(file="jodh.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(715, 50, text="JODHPUR", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(950, 370, text=
    '''
    Jodhpur is the second largest city in the Indian state of Rajasthan.
    The capital of the kingdom known as Marwar. Jodhpur is a popular
    tourist destination, featuring many palaces,forts and temples, 
    set in the stark landscape of the Thar Desert. The city is known as
    the "Sun City" for the bright and sunny weather it enjoys all the
    year round. It is the second metropolitan city of the state and the
    thirty-fifth largest city in India. It was formerly the seat of a 
    princely state of the same name. The old city circles the fort and
    is bounded by a wall with several gates. Jodhpur is also known as 
    "Blue City" because of the blue colours that decorate many of the 
    houses in the old city area. However, the city has expanded greatly
    outside the wall over the past several decades.
    ''',justify="center", font=('Bahnschrift SemiLight SemiConde', 17, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def aizawl():
    c3 = Toplevel()
    img1 = PhotoImage(file="aizawl.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="AIZAWL", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 400, text=
    '''
    Aizawl is the capital of the state of Mizoram in India.
    With a resident population of 293,416, it is the largest city in the state.

    It is also the centre of administration containing all the
    important government offices, state assembly house and civil secretariat.
    The population of Aizawl strongly reflects the different communities 
    of the ethnic Mizo people.

    Bara Bazar is the main shopping centre of Aizawl in Dawrpui Veng locality. 
    The steep Zion Street is lined with stalls selling garments. 
    ''', font=('Bahnschrift SemiLight SemiConde', 20, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def lunglei():
    c3 = Toplevel()
    img1 = PhotoImage(file="lunglei.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(710, 70, text="LUNGLEI", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 450, text=
    '''
    Lunglei is a town, situated in the south-central part of Mizoram state, northeastern India.
    Lunglei, sometimes spelled Lungleh, literally meaning 'bridge of rock' got its name from
    a bridge like rock found in the riverine area around Nghasih - a small tributary of the river
    Tlawng.

    It is the second largest town after the capital, Aizawl, located 165 km (102 miles)
    south of Aizawl. Lunglei was the Capital of South Lushai Hill Districts for 10 years from 1888,
    as was Aizawl for the North Hill Districts.

    The two were united in 1898. Lunglei is the second-largest town in Mizoram and was an 
    important town until the partition of India as it had direct access to Chittagong,
    a big city in Bangladesh which made Lunglei the commercial and education centre.
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def bhubaneswar():
    c3 = Toplevel()
    img1 = PhotoImage(file="bhubaneswar.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(710, 80, text="BHUBANESWAR", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(900, 400, text=
    '''
            Bhubaneswar is the capital of the Indian state of Odisha. It is the
            largest city in Odisha and is a centre of economic and religious 
            importance in Eastern India. Along with the old town,the region of 
            Bhubaneswar, historically was often depicted as Ekamra Kshetra.
            With the diverse ranges of heritage resources, it showcases 
            significant sacred cultural landscape components which have evolved 
            with the support of available natural resource base and cultural trigger.
            Although the modern city of Bhubaneswar was formally established only in
            1948, the history of the areas in and around the present-day city can be
            traced to 1st century BCE and earlier.
    ''', font=('Bahnschrift SemiLight SemiConde', 17, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def cuttack():
    c3 = Toplevel()
    img1 = PhotoImage(file="cuttack.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="CUTTACK", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 350, text=
    '''
Cuttack is the former capital and the second largest city in the eastern Indian state of Odisha.\n It is also the headquarters of the Cuttack district. The name of the city is an anglicised form of \nKatak which literally means The Fort, a reference to the ancient Barabati\n Fort around which the city initially developed. \nCuttack is also known as the Millennium City as well as\n the Silver City due to its history of 1000 years and famous silver filigree works.\n It is also considered as the judicial capital of Odisha as the Odisha High Court is located here.\n It is also the commercial capital of Odisha which hosts a large number of \ntrading and business houses in and around the city.
    ''', width = 1200, font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def lucknow():
    c3 = Toplevel()
    img1 = PhotoImage(file="lucknow.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="LUCKNOW", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(750, 350, text=
    '''
    Lucknow is the largest city of the state of Uttar Pradesh, India. A major metropolitan
    city of India, Lucknow is the administrative headquarters of the eponymous District and 

    Division and the capital of the state of Uttar Pradesh. It is the third largest city 
    in north, east and central India, after Delhi and Kolkata, and the second largest city
    in north and central India after New Delhi. It is also the largest city in Uttar Pradesh.

    Lucknow has always been known as a multicultural city that flourished as a North Indian
    cultural and artistic hub, and the seat of power of Nawabs in the 18th and 19th centuries.
    It continues to be an important centre of governance, administration, education, commerce,
    aerospace, finance, pharmaceuticals, technology, design, culture, tourism, music and poetry. 
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def agra():
    c3 = Toplevel()
    img1 = PhotoImage(file="agra.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(740, 70, text="AGRA", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(690, 350, text=
    '''
    Agra is a city on the banks of the river Yamuna in the northern state of Uttar Pradesh, India. 
    Agra can also refer to the administrative district that has its headquarters in Agra city. 
    It is a major tourist destination because of its many splendid Mughal-era buildings, 
    most notably the Taj Mahal, Agra Fort and Fatehpur Sikri, all three of which are 
    UNESCO World Heritage Sites.
    Agra is included on the Golden Triangle tourist circuit, along with Delhi and Jaipur;
    and the Uttar Pradesh Heritage Arc, tourist circuit of UP state, along Lucknow
    the capital of the state and Varanasi.
    Agra falls within the Braj cultural region. The city was first mentioned in the 
    epic Mahabharata, where it was called Agrevaa (derived from Sanskrit meaning
    "the border of the forest").
    ''',justify="center", font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def kohima():
    c3 = Toplevel()
    img1 = PhotoImage(file="kohima.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(730, 70, text="KOHIMA", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(750, 450, text=
    '''
    Kohima is the hilly capital of India's north eastern border state of Nagaland 
    which shares its borders with Burma.
    With a resident population of 267,988 it is the second largest city
    in the state.
    Originally known as Kewhira, it was founded in 1878 when 
    the British Empire established its headquarters of the then Naga Hills.
    It officially became the capital after the state of Nagaland was 
    inaugurated in 1963. Kohima is the land of the Angami Naga tribe.
    It is situated in the foothills of Japfu range located south of 
    Kohima District.
    ''', font=('Bahnschrift SemiLight SemiConde', 20, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def ungma():
    c3 = Toplevel()
    img1 = PhotoImage(file="ungma2.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(740, 70, text="UNGMA", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 350, text=
    '''
    Ungma is a historic village situated 10 km south of the heart of Mokokchung town in India. 
    Ungma is one of the most ancient Ao villages and of great tourist interest to view the
    folklore, customs and traditions of Ao Naga. Ungma is one of the more developed villages
    in Nagaland. Legends indicate the early Aos settled here first after coming from 
    Chungliyimti before migrating to the rest of Ao areas. An old log drum in the village
    is worth visiting. There is also a beautiful Park on the outskirts of the village.
    ''',justify="center", font=('Bahnschrift SemiLight SemiConde', 20, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def agartala():
    c3 = Toplevel()
    img1 = PhotoImage(file="agartala.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="AGARTALA", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(750, 400, text=
    '''
    Agartala is the capital as well as the largest city of the Indian state of
    Tripura and also is the second largest city in North-east India after Guwahati, 
    both in municipal area and population. The city is the seat of the Government
    of Tripura. Agartala is one of the fastest developing cities of India.

    Agartala is a component of two words, namely "Agar", a kind of oily valuable
    perfume tree, + suffix "tala", a store house. The city is governed by the Agartala
    Municipal Corporation.

    Agartala lies on the bank of the Haora River and is located 2 km
    from the Bangladesh Border. Agartala is India's third international internet gateway after 
    the ones in Mumbai and Chennai. 
    ''', font=('Bahnschrift SemiLight SemiConde', 20, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def dharmanagar():
    c3 = Toplevel()
    img1 = PhotoImage(file="dharmanagar.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 50, text="DHARMANAGAR", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(710, 320, text=
    '''
    Dharmanagar is a district town and a Municipal Council in the North East of India and
    the North Tripura district of the state of Tripura, India. Dharmanagar is renowned for
    its natural beauty. It has many top quality schools. The city also has its great history
    regarding the several emperors who ruled the city. Earlier in the ancient times the city
    had a large geographical area but along time it has been reduced drastically due to
    partition and other reasons. The city of Dharmanagar is very famous for its historical
    monuments and palaces. The city has many such historic ruins which display the ancient old 
    history of the city. Dharmanagar being a small town geographically the city is not so l
    arge and stretches up to 7.7 km2 in area.
    ''', font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def gangtok():
    c3 = Toplevel()
    img1 = PhotoImage(file="gangtok1.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="GANGTOK", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(730, 400, text=
    '''
    Gangtok is a municipality, the capital and the largest town of the Indian state of Sikkim.
    It also is the headquarters of the East Sikkim district.

    The town's population of 100,000 belongs to different ethnicities such as Nepali, 
    Lepchas and Bhutia.

    Nestled within higher peaks of the Himalaya and enjoying a year-round mild
    temperate climate, Gangtok is at the centre of Sikkim's tourism industry. 
    Gangtok is located in the eastern Himalayan range,at an elevation of 1,650 m (5,410 ft).
    ''',fill = "white", font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def lachung():
    c3 = Toplevel()
    img1 = PhotoImage(file="lachung.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(750, 70, text="LACHUNG", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(700, 400, text=
    '''
    Lachung is a town and hill station in northeast Sikkim, India. It is located in the 
    North Sikkim district near the border with Tibet.

    Lachung is at an elevation of about 9,600 feet (2,900 m) and at the confluence 
    of the lachen and Lachung Rivers, both tributaries of the River Teesta. 

    The word Lachung means 'small pass'. The town is approximately 125 kilometres 
    (78 mi) from the capital Gangtok. The Indian Army has a forward base in the town.

    Before the Chinese annexation of Tibet in 1950, Lachung was a trading post between
    Sikkim and Tibet, after which it was closed down.
    ''',fill = "white", font=('Bahnschrift SemiLight SemiConde', 20, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


def shillong():
    c3 = Toplevel()
    img1 = PhotoImage(file="shillong.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="SHILLONG", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(750, 400, text=
    '''
    Shillong is the capital and hill station of Meghalaya, also known as 'The Abode of Clouds',
    one of the smallest states in India. It is said that the rolling hills around the town reminded
    the European settlers of Scotland. Hence, they would also refer to it as the
    'Scotland of the East'.


    It is the headquarters of the East Khasi Hills district and is situated at an average altitude
    of 4,908 feet (1,496 m) above sea level, with the highest point being Shillong Peak at
    6,449 feet (1,966 m). Shillong is the 330th most populous city in India with population
    of 143,007 according to the 2011 census. 
    ''', font=('Bahnschrift SemiLight SemiConde', 20, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))


# noinspection PyArgumentList
def cherrapunji():
    c3 = Toplevel()
    img1 = PhotoImage(file="cherrapunji.png")
    canvas = Canvas(c3)
    canvas.image = img1
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img1, anchor="nw")
    canvas.create_text(720, 70, text="CHERRAPUNJI", font=('ALGERIAN', 48, 'bold'), fill='midnight blue')
    canvas.create_text(740, 400, text=
    '''
    Cherrapunji is a subdivisional town in the East Khasi Hills district in the Indian
    state of Meghalaya.It is credited as being the wettest place on Earth, but nearby 
    Mawsynram currently holds that record.Cherrapunji still holds the all-time record
    for the most rainfall in a calendar month and in a year.

    It received 9,300 mm (366 in) in July 1861 and 26,461 mm (1,041.75 in) between
    1 August 1860 and 31 July 1861. Cherrapunji is the traditional capital of the 
    Nongkhlaw hima (Khasi tribal chieftainship constituting a petty state) known as
    Sohra or Churra.

    Cherrapunji is also famous for its living bridges. Over hundreds of years the 
    people in Cherrapunji have developed techniques for growing roots of trees into
    large bridges. 
    ''',fil = "white",  font=('Bahnschrift SemiLight SemiConde', 19, 'bold'))
    canvas.create_text(1184, 674, text=
    '''
    source:
    information-www.famousplacesinindia.in
    background image-Google images
    ''', font=('Helvetica', 13, 'bold'))