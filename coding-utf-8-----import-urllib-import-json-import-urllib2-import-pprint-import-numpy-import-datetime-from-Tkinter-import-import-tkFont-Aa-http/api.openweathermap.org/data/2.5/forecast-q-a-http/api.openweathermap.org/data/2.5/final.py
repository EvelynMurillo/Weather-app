# -*- coding: utf-8 -*-
import urllib
import json
import urllib2
import pprint
import numpy
import datetime

from Tkinter import *
import tkFont
Aa = "http://api.openweathermap.org/data/2.5/forecast?q="
a="http://api.openweathermap.org/data/2.5/weather?q="
b="&units=metric&APPID=72d94a54e72d5548bc7a01c74350762d"


root = Tk()

class textInput:
    weather = ""
    weather = ""

    futureWeather = ""
    futureWeather = ""

    location = ""
    description = ""
    imageicon = ""
    currentTemp = ""
    photo=""

    Day1max = ""
    Day1min = ""

    Day2max = ""
    Day2min = ""

    Day3max = ""
    Day3min = ""

    Day4max = ""
    Day4min = ""

    Day5max = ""
    Day5min = ""
    def __init__(self, master):
        self.Text = Label(master, text="Enter your location here:")
        self.Text.grid(row=0, column=1)
        self.Input = Entry(master)
        self.Input.grid(row=0, column=2)
        self.submitButton = Button(master, text="Submit", command=self.submit)
        self.submitButton.grid(row=0, column=3)

        self.A1 = Label(master, text=self.Day1max)
        self.A1.grid(row=1, column=1, pady=6, padx=5)
        self.A2 = Label(master, text=self.location)
        self.A2.grid(row=2, column=1, pady=6, padx=5)
        self.A3 = Label(master, text=self.Day1min)
        self.A3.grid(row=3, column=1, pady=6, padx=5)

        #self.B1 = Label(master, image=icon)
        #self.B1.grid(row=0, rowspan=3, column=2, padx=5)
        self.B2 = Label(master, text=self.description)
        self.B2.grid(row=3, column=2, padx=5, pady=5)

        self.C1 = Label(master, text=self.currentTemp)
        self.C1.grid(column=3, row=2, padx=5)



        #5 Day Forecast-------------------------------------------------------->

        #Day1-------------------------------------------------------->
        self.AA = Label(master, text="Day1")
        self.AA.grid(column=1, row=5, padx=5)

        #images go here
        #self.AB = Label(root, image= icon, width=30, height=30)
        #self.AB.grid(column=1, row=5, padx=5)

        self.AC = Label(master, text=self.Day1max)
        self.AC.grid(column=1, row=6, padx=5)

        self.AD = Label(master, text=self.Day1min)
        self.AD.grid(column=1, row=7, padx=5)

        #Day2-------------------------------------------------------->
        self.BA = Label(master, text="Day2")
        self.BA.grid(column=2, row=5, padx=5)

        #self.BB = Label(root, image= icon, width=30, height=30)
        #self.BB.grid(column=2, row=5, padx=5)

        self.BC = Label(master, text=self.Day2max)
        self.BC.grid(column=2, row=6, padx=5)

        self.BD = Label(master, text=self.Day2min)
        self.BD.grid(column=2, row=7, padx=5)


        #Day3-------------------------------------------------------->
        self.CA = Label(master, text="Day3")
        self.CA.grid(column=3, row=5, padx=5)

        #self.CB = Label(root, image= icon, width=30, height=30)
        #self.CB.grid(column=3, row=5, padx=5)

        self.CC = Label(master, text=self.Day3max)
        self.CC.grid(column=3, row=6, padx=5)

        self.CD = Label(master, text=self.Day3min)
        self.CD.grid(column=3, row=7, padx=5)


        #Day4-------------------------------------------------------->
        self.DA = Label(master, text="Day4")
        self.DA.grid(column=4, row=5, padx=5)

        #self.DB = Label(root, image= icon, width=30, height=30)
        #self.DB.grid(column=4, row=5, padx=5)

        self.DC = Label(master, text=self.Day4max)
        self.DC.grid(column=4, row=6, padx=5)

        self.DD = Label(master, text=self.Day4min)
        self.DD.grid(column=4, row=7, padx=5)


        #Day5-------------------------------------------------------->
        self.EA = Label(master, text="Day5")
        self.EA.grid(column=5, row=5, padx=5)

        #self.EB = Label(root, image= icon, width=30, height=30)
        #self.EB.grid(column=5, row=5, padx=5)

        self.EC = Label(master, text=self.Day5max)
        self.EC.grid(column=5, row=6, padx=5)

        self.ED = Label(master, text=self.Day5min)
        self.ED.grid(column=5, row=7, padx=5)


    def submit(self):
        s = self.Input.get()
        self.city(s)
        self.update(root)

    def city(self,cityName):
        self.weather = urllib2.urlopen(a+ cityName +b)
        self.weather = json.loads(self.weather.read())
        self.futureWeather = urllib2.urlopen(Aa+ cityName +b)
        self.futureWeather = json.loads(self.futureWeather.read())
        self.location = "City: "+(self.weather["name"])
        self.description = (self.weather["weather"][0]["description"])
		
		#function takes in description and matches it with the icons, displays icon according to the description
	def imageiconn(self,description):
		if description == "clear sky":
			self.imageicon="sunny.gif"
		if description == "light rain":
			self.imageicon= "rain.gif"
		if description =="scattered clouds":
			self.imageicon= "scatteredClouds.gif"
		if description == "broken clouds":
			self.imageicon= "fewClouds.gif"
		if description == "shower rain":
			self.imageicon= "showeredrans.gif"
		if description == "thunderstorm":
			self.imageicon= "thunderstorm.gif"
		if description == "snow":
			self.imageicon= "snow.gif"
		if description == "mist":
			self.imageicon="mist.gif"
		print " image name"+ self.imageicon
		
		self.photo=PhotoImage(file = "")
		
		#imageiconn(self,description)
		

   
 

        #Current temperature -------------------------------------------------------->
		self.D1_avg_a = (self.futureWeather["list"][1]["main"]["temp"])
        self.D1_avg_b = (self.futureWeather["list"][2]["main"]["temp"])
        self.D1_avg_c = (self.futureWeather["list"][3]["main"]["temp"])
        self.D1_avg_d = (self.futureWeather["list"][4]["main"]["temp"])
        self.D1_avg_e = (self.futureWeather["list"][5]["main"]["temp"])
        self.D1_avg_f = (self.futureWeather["list"][6]["main"]["temp"])
        self.D1_avg_g = (self.futureWeather["list"][7]["main"]["temp"])
        self.D1_avg_h = (self.futureWeather["list"][8]["main"]["temp"])

        #self.D1_avg_list = [self.D1_avg_a,self.D1_avg_b,self.D1_avg_c,self.D1_avg_d,self.D1_avg_e,self.D1_avg_f,self.D1_avg_g,self.D1_avg_h]
        #self.D1_avg = numpy.mean(self.D1_avg_list)
        #self.D1_avg = int(self.D1_avg)
        #self.currentTemp = str(self.D1_avg)+"°C"



        #Min. temperature-------------------------------------------------------->

        #Day 1------------------------------------------------------------------------------------------------------------------------------>
        self.D1_min_a = (self.futureWeather["list"][1]["main"]["temp_min"])
        self.D1_min_b = (self.futureWeather["list"][2]["main"]["temp_min"])
        self.D1_min_c = (self.futureWeather["list"][3]["main"]["temp_min"])
        self.D1_min_d = (self.futureWeather["list"][4]["main"]["temp_min"])
        self.D1_min_e = (self.futureWeather["list"][5]["main"]["temp_min"])
        self.D1_min_f = (self.futureWeather["list"][6]["main"]["temp_min"])
        self.D1_min_g = (self.futureWeather["list"][7]["main"]["temp_min"])
        self.D1_min_h = (self.futureWeather["list"][8]["main"]["temp_min"])

        self.D1_min_list = [self.D1_min_a,self.D1_min_b,self.D1_min_c,self.D1_min_d,self.D1_min_e,self.D1_min_f,self.D1_min_g,self.D1_min_h]
        self.D1_min = numpy.min(self.D1_min_list)
        self.D1_min = int(self.D1_min)
        self.Day1min = "L: "+str(self.D1_min)+"°C"

        #Day 2------------------------------------------------------------------------------------------------------------------------------>
        self.D2_min_a = (self.futureWeather["list"][9]["main"]["temp_min"])
        self.D2_min_b = (self.futureWeather["list"][10]["main"]["temp_min"])
        self.D2_min_c = (self.futureWeather["list"][11]["main"]["temp_min"])
        self.D2_min_d = (self.futureWeather["list"][12]["main"]["temp_min"])
        self.D2_min_e = (self.futureWeather["list"][13]["main"]["temp_min"])
        self.D2_min_f = (self.futureWeather["list"][14]["main"]["temp_min"])
        self.D2_min_g = (self.futureWeather["list"][15]["main"]["temp_min"])
        self.D2_min_h = (self.futureWeather["list"][16]["main"]["temp_min"])

        self.D2_min_list = [self.D2_min_a,self.D2_min_b,self.D2_min_c,self.D2_min_d,self.D2_min_e,self.D2_min_f,self.D2_min_g,self.D2_min_h]
        self.D2_min = numpy.min(self.D2_min_list)
        self.D2_min = int(self.D2_min)
        self.Day2min = "L: "+str(self.D2_min)+"°C"

        #Day 3------------------------------------------------------------------------------------------------------------------------------>
        self.D3_min_a = (self.futureWeather["list"][17]["main"]["temp_min"])
        self.D3_min_b = (self.futureWeather["list"][18]["main"]["temp_min"])
        self.D3_min_c = (self.futureWeather["list"][19]["main"]["temp_min"])
        self.D3_min_d = (self.futureWeather["list"][20]["main"]["temp_min"])
        self.D3_min_e = (self.futureWeather["list"][21]["main"]["temp_min"])
        self.D3_min_f = (self.futureWeather["list"][22]["main"]["temp_min"])
        self.D3_min_g = (self.futureWeather["list"][23]["main"]["temp_min"])
        self.D3_min_h = (self.futureWeather["list"][24]["main"]["temp_min"])

        self.D3_min_list = [self.D3_min_a,self.D3_min_b,self.D3_min_c,self.D3_min_d,self.D3_min_e,self.D3_min_f,self.D3_min_g,self.D3_min_h]
        self.D3_min = numpy.min(self.D3_min_list)
        self.D3_min = int(self.D3_min)
        self.Day3min = "L: "+str(self.D3_min)+"°C"


        #Day 4------------------------------------------------------------------------------------------------------------------------------>
        self.D4_min_a = (self.futureWeather["list"][25]["main"]["temp_min"])
        self.D4_min_b = (self.futureWeather["list"][26]["main"]["temp_min"])
        self.D4_min_c = (self.futureWeather["list"][27]["main"]["temp_min"])
        self.D4_min_d = (self.futureWeather["list"][28]["main"]["temp_min"])
        self.D4_min_e = (self.futureWeather["list"][29]["main"]["temp_min"])
        self.D4_min_f = (self.futureWeather["list"][30]["main"]["temp_min"])
        self.D4_min_g = (self.futureWeather["list"][31]["main"]["temp_min"])
        self.D4_min_h = (self.futureWeather["list"][32]["main"]["temp_min"])

        self.D4_min_list = [self.D4_min_a,self.D4_min_b,self.D4_min_c,self.D4_min_d,self.D4_min_e,self.D4_min_f,self.D4_min_g,self.D4_min_h]
        self.D4_min = numpy.min(self.D4_min_list)
        self.D4_min = int(self.D4_min)
        self.Day4min = "L: "+str(self.D4_min)+"°C"



        #Day 5------------------------------------------------------------------------------------------------------------------------------>
        self.D5_min_a = (self.futureWeather["list"][33]["main"]["temp_min"])
        self.D5_min_b = (self.futureWeather["list"][34]["main"]["temp_min"])
        self.D5_min_c = (self.futureWeather["list"][35]["main"]["temp_min"])
        self.D5_min_d = (self.futureWeather["list"][36]["main"]["temp_min"])
        self.D5_min_e = (self.futureWeather["list"][37]["main"]["temp_min"])
        self.D5_min_f = (self.futureWeather["list"][38]["main"]["temp_min"])
        self.D5_min_g = (self.futureWeather["list"][39]["main"]["temp_min"])

        self.D5_min_list = [self.D5_min_a,self.D5_min_b,self.D5_min_c,self.D5_min_d,self.D5_min_e,self.D5_min_f,self.D5_min_g]
        self.D5_min = numpy.min(self.D5_min_list)
        self.D5_min = int(self.D5_min)
        self.Day5min = "L: "+str(self.D5_min)+"°C"




        #max. temperature

        #Day 1------------------------------------------------------------------------------------------------------------------------------>
        self.D1_max_a = (self.futureWeather["list"][1]["main"]["temp_max"])
        self.D1_max_b = (self.futureWeather["list"][2]["main"]["temp_max"])
        self.D1_max_c = (self.futureWeather["list"][3]["main"]["temp_max"])
        self.D1_max_d = (self.futureWeather["list"][4]["main"]["temp_max"])
        self.D1_max_e = (self.futureWeather["list"][5]["main"]["temp_max"])
        self.D1_max_f = (self.futureWeather["list"][6]["main"]["temp_max"])
        self.D1_max_g = (self.futureWeather["list"][7]["main"]["temp_max"])
        self.D1_max_h = (self.futureWeather["list"][8]["main"]["temp_max"])

        self.D1_max_list = [self.D1_max_a,self.D1_max_b,self.D1_max_c,self.D1_max_d,self.D1_max_e,self.D1_max_f,self.D1_max_g,self.D1_max_h]
        self.D1_max = numpy.max(self.D1_max_list)
        self.D1_max = int(self.D1_max)
        self.Day1max = "H: "+str(self.D1_max)+"°C"



        #Day 2------------------------------------------------------------------------------------------------------------------------------>
        self.D2_max_a = (self.futureWeather["list"][9]["main"]["temp_max"])
        self.D2_max_b = (self.futureWeather["list"][10]["main"]["temp_max"])
        self.D2_max_c = (self.futureWeather["list"][11]["main"]["temp_max"])
        self.D2_max_d = (self.futureWeather["list"][12]["main"]["temp_max"])
        self.D2_max_e = (self.futureWeather["list"][13]["main"]["temp_max"])
        self.D2_max_f = (self.futureWeather["list"][14]["main"]["temp_max"])
        self.D2_max_g = (self.futureWeather["list"][15]["main"]["temp_max"])
        self.D2_max_h = (self.futureWeather["list"][16]["main"]["temp_max"])

        self.D2_max_list = [self.D2_max_a,self.D2_max_b,self.D2_max_c,self.D2_max_d,self.D2_max_e,self.D2_max_f,self.D2_max_g,self.D2_max_h]
        self.D2_max = numpy.max(self.D2_max_list)
        self.D2_max = int(self.D2_max)
        self.Day2max = "H: "+str(self.D2_max)+"°C"


        #Day 3------------------------------------------------------------------------------------------------------------------------------>
        self.D3_max_a = (self.futureWeather["list"][17]["main"]["temp_max"])
        self.D3_max_b = (self.futureWeather["list"][18]["main"]["temp_max"])
        self.D3_max_c = (self.futureWeather["list"][19]["main"]["temp_max"])
        self.D3_max_d = (self.futureWeather["list"][20]["main"]["temp_max"])
        self.D3_max_e = (self.futureWeather["list"][21]["main"]["temp_max"])
        self.D3_max_f = (self.futureWeather["list"][22]["main"]["temp_max"])
        self.D3_max_g = (self.futureWeather["list"][23]["main"]["temp_max"])
        self.D3_max_h = (self.futureWeather["list"][24]["main"]["temp_max"])

        self.D3_max_list = [self.D3_max_a,self.D3_max_b,self.D3_max_c,self.D3_max_d,self.D3_max_e,self.D3_max_f,self.D3_max_g,self.D3_max_h]
        self.D3_max = numpy.max(self.D3_max_list)
        self.D3_max = int(self.D3_max)
        self.Day3max = "H: "+str(self.D3_max)+"°C"

        #Day 4------------------------------------------------------------------------------------------------------------------------------>
        self.D4_max_a = (self.futureWeather["list"][25]["main"]["temp_max"])
        self.D4_max_b = (self.futureWeather["list"][26]["main"]["temp_max"])
        self.D4_max_c = (self.futureWeather["list"][27]["main"]["temp_max"])
        self.D4_max_d = (self.futureWeather["list"][28]["main"]["temp_max"])
        self.D4_max_e = (self.futureWeather["list"][29]["main"]["temp_max"])
        self.D4_max_f = (self.futureWeather["list"][30]["main"]["temp_max"])
        self.D4_max_g = (self.futureWeather["list"][31]["main"]["temp_max"])
        self.D4_max_h = (self.futureWeather["list"][32]["main"]["temp_max"])

        self.D4_max_list = [self.D4_max_a,self.D4_max_b,self.D4_max_c,self.D4_max_d,self.D4_max_e,self.D4_max_f,self.D4_max_g,self.D4_max_h]
        self.D4_max = numpy.max(self.D4_max_list)
        self.D4_max = int(self.D4_max)
        self.Day4max = "H: "+str(self.D4_max)+"°C"



        #Day 5------------------------------------------------------------------------------------------------------------------------------>
        self.D5_max_a = (self.futureWeather["list"][33]["main"]["temp_max"])
        self.D5_max_b = (self.futureWeather["list"][34]["main"]["temp_max"])
        self.D5_max_c = (self.futureWeather["list"][35]["main"]["temp_max"])
        self.D5_max_d = (self.futureWeather["list"][36]["main"]["temp_max"])
        self.D5_max_e = (self.futureWeather["list"][37]["main"]["temp_max"])
        self.D5_max_f = (self.futureWeather["list"][38]["main"]["temp_max"])
        self.D5_max_g = (self.futureWeather["list"][39]["main"]["temp_max"])

        self.D5_max_list = [self.D5_max_a,self.D5_max_b,self.D5_max_c,self.D5_max_d,self.D5_max_e,self.D5_max_f,self.D5_max_g]
        self.D5_max = numpy.max(self.D5_max_list)
        self.D5_max = int(self.D5_max)
        self.Day5max = "H: "+str(self.D5_max)+"°C"



    def update(self, master):
	

        self.A1 = Label(master, text="")
        self.A1.grid(row=1, column=1, pady=6, padx=5)
        self.A1 = Label(master, text=self.Day1max)
        self.A1.grid(row=1, column=1, pady=6, padx=5)

        self.A2 = Label(master, text="")
        self.A2.grid(row=2, column=1, pady=6, padx=5)
        self.A2 = Label(master, text=self.location)
        self.A2.grid(row=2, column=1, pady=6, padx=5)

        self.A3 = Label(master, text="")
        self.A3.grid(row=3, column=1, pady=6, padx=5)
        self.A3 = Label(master, text=self.Day1min)
        self.A3.grid(row=3, column=1, pady=6, padx=5)


        self.imageiconn(description)
        self.B1 = Label(master, image=self.photo)
        self.B1.grid(row=0, rowspan=3, column=2, padx=5)

        #clear entry
        self.B2 = Label(master, text="")
        self.B2.grid(row=3, column=2, padx=5, pady=5)
        self.B2 = Label(master, text=self.description)
        self.B2.grid(row=3, column=2, padx=5, pady=5)

        self.C1 = Label(master, text="")
        self.C1.grid(column=3, row=2, padx=5)
        self.C1 = Label(master, text=self.currentTemp)
        self.C1.grid(column=3, row=2, padx=5)


        #Days 1 - 5
        #Day1----------------------------------------------------------------->
        self.AA = Label(master, text="Day1")
        self.AA.grid(column=1, row=5, padx=5)

        #images go here
        #self.AB = Label(root, image= icon, width=30, height=30)
        #self.AB.grid(column=1, row=5, padx=5)

        self.AC = Label(master, text="")
        self.AC.grid(column=1, row=6, padx=5)
        self.AC = Label(master, text=self.Day1max)
        self.AC.grid(column=1, row=6, padx=5)


        self.AD = Label(master, text="")
        self.AD.grid(column=1, row=7, padx=5)
        self.AD = Label(master, text=self.Day1min)
        self.AD.grid(column=1, row=7, padx=5)


        #Day2----------------------------------------------------------------->
        self.BA = Label(master, text="Day2")
        self.BA.grid(column=2, row=5, padx=5)

        #self.BB = Label(root, image= icon, width=30, height=30)
        #self.BB.grid(column=2, row=5, padx=5)

        self.BC = Label(master, text="")
        self.BC.grid(column=2, row=6, padx=5)
        self.BC = Label(master, text=self.Day2max)
        self.BC.grid(column=2, row=6, padx=5)


        self.BD = Label(master, text="")
        self.BD.grid(column=2, row=7, padx=5)
        self.BD = Label(master, text=self.Day2min)
        self.BD.grid(column=2, row=7, padx=5)


        #Day3----------------------------------------------------------------->
        self.CA = Label(master, text="Day3")
        self.CA.grid(column=3, row=5, padx=5)

        #self.CB = Label(root, image= icon, width=30, height=30)
        #self.CB.grid(column=3, row=5, padx=5)

        self.CC = Label(master, text="")
        self.CC.grid(column=3, row=6, padx=5)
        self.CC = Label(master, text=self.Day3max)
        self.CC.grid(column=3, row=6, padx=5)


        self.CD = Label(master, text="")
        self.CD.grid(column=3, row=7, padx=5)
        self.CD = Label(master, text=self.Day3min)
        self.CD.grid(column=3, row=7, padx=5)


        #Day4----------------------------------------------------------------->
        self.DA = Label(master, text="Day4" )
        self.DA.grid(column=4, row=5, padx=5)

        #self.DB = Label(root, image= icon, width=30, height=30)
        #self.DB.grid(column=4, row=5, padx=5)

        self.DC = Label(master, text="")
        self.DC.grid(column=4, row=6, padx=5)
        self.DC = Label(master, text=self.Day4max)
        self.DC.grid(column=4, row=6, padx=5)


        self.DD = Label(master, text="")
        self.DD.grid(column=4, row=7, padx=5)
        self.DD = Label(master, text=self.Day4min)
        self.DD.grid(column=4, row=7, padx=5)


        #Day5----------------------------------------------------------------->
        self.EA = Label(master, text= "Day5")
        self.EA.grid(column=5, row=5, padx=5)

        #self.EB = Label(root, image= icon, width=30, height=30)
        #self.EB.grid(column=5, row=5, padx=5)

        self.EC = Label(master, text="")
        self.EC.grid(column=5, row=6, padx=5)
        self.EC = Label(master, text=self.Day5max)
        self.EC.grid(column=5, row=6, padx=5)

        self.ED = Label(master, text="")
        self.ED.grid(column=5, row=7, padx=5)
        self.ED = Label(master, text=self.Day5min)
        self.ED.grid(column=5, row=7, padx=5)
	def imageiconn(self,description):
		if description == "clear sky":
			self.imageicon="sunny.gif"
		if description == "light rain":
			self.imageicon= "rain.gif"
		if description =="scattered clouds":
			self.imageicon= "scatteredClouds.gif"
		if description == "broken clouds":
			self.imageicon= "fewClouds.gif"
		if description == "shower rain":
			self.imageicon= "showeredrans.gif"
		if description == "thunderstorm":
			self.imageicon= "thunderstorm.gif"
		if description == "snow":
			self.imageicon= "snow.gif"
		if description == "mist":
			self.imageicon="mist.gif"
		print " image name"+ self.imageicon
		
		self.photo=PhotoImage(file = self.imageiconn(self,description))
		#imageiconn(self,description)
		

   
 


def main():
    A = textInput(root)
    root.mainloop()
    

if __name__ == '__main__': main()
