# -*- coding: utf-8 -*-

# A Python script that data mines Pinterest.com using OAUTH 2.0 access token and GET requests. 
# Created by Tatiana Ensslin
# April 23rd, 2016
# Social Media Mining


import urllib2 #for urlopen
import sys
import json
import time
from dateutil.parser import parse #to parse the date
from datetime import date
from operator import itemgetter #to sort
from datetime import datetime
from time import gmtime, strftime
from datetime import datetime, timedelta, date

#Pinterest useds AOUTH 2.0 .. aqcuire access token through token generator under app development
access_token='Ae3zx8MeHSlYVUJs2S861AU19fAeFEh8FWEFUTRDCv0QnYAt5AAAAAA&'

# Returns any user's information including the first name, last name, id, URL
def returnUserInfo(user):
	
	r = urllib2.urlopen("https://api.pinterest.com/v1/users/"+user+"/?access_token="+access_token+"fields=first_name%2Cid%2Clast_name%2Curl%2Ccreated_at")
	data = json.load(r)
	return data
	#print r

# Retrieves the boards information, such as URL, date of creation, and pin count ..etc
def getBoardInfo(user,board):

	r = urllib2.urlopen("https://api.pinterest.com/v1/boards/"+user+"/"+board+"/?access_token="+access_token+"fields=id%2Cname%2Curl%2Ccounts%2Ccreated_at")
	data = json.load(r)
	return data

# Retrieves the information about all pins on a board, meaning title, URL, creation, id .. etc
def retrievePins(user,board):
	
	r = urllib2.urlopen("https://api.pinterest.com/v1/boards/"+user+"/"+board+"/pins/?access_token="+access_token+"fields=id%2Clink%2Cnote%2Curl")
	#r = urllib2.urlopen("https://api.pinterest.com/v1/boards/bethanyreul7/Shower/pins/?access_token=Ae3zx8MeHSlYVUJs2S861AU19fAeFEh8FWEFUTRDCv0QnYAt5AAAAAA&fields=id%2Clink%2Cnote%2Curl").read()
	#print "This is retrieving pins:" + r + "\n"
	#print r
	data = json.load(r)
	return data

def parser(date): #a function that takes in the date as a YY-MM-DDTHH:MM:SS and parses it to recieve just YY-MM-DD
	p = parse(date) #parse date
	p = str(p) #convert date to string
	parsedDate = p.split(" ", 1) #split the date and time
	dateOnly = parsedDate[0] #retreive the date only
	#dateOnly.replace('/', '-')
	dateOnly = dateOnly.replace("-","")
	print dateOnly 
	dateArray = []
	for i in dateOnly: 
		dateArray.append(i)
	#print dateArray
	dateArray2 = [] #create a temp array to add in ',' for dates. this is CRUCIAL for excel data charting
	dateArray2.append(dateArray[0])
	dateArray2.append(dateArray[1])
	dateArray2.append(dateArray[2])
	dateArray2.append(dateArray[3])
	dateArray2.append(",")
	dateArray2.append(dateArray[4])
	dateArray2.append(dateArray[5])
	dateArray2.append(",")
	dateArray2.append(dateArray[6])
	dateArray2.append(dateArray[7])
	dateOnly = "".join(dateArray2)
	return dateOnly

def dog(): #preform data mining on DOGS category

	# dogUsers contains 150 list of users with boards named dogs
	dogUsers = ['playbuzz','paola_gambetti','birob','funnyordie','leasheffield','chicoulino','kittyklan','gwylfa','carinageuther','enmibolso','thubtnguyen','doublecloth','newfinish','warda278','justintpalmer','alisaquint','alaridesign','christelkelz','lisskis','carleencoulter','retrogoddess','whippets4ever','muttimamma','angelicasara','wunderworker','sagegardencon','ellenbrok','apricou','Peggylholland','fetchsilversp','paperandstyleco','born2rock1974','mamapenny','caitlin_cawley','equip2survive','StephLaughlin','luvleo10','gabbiandrade','fineanddapper','neyselima','eziosgrandma','kinaps','judioliver','AlessandrD','bibibibibibibib','monikan754','l0503','espritk','avlogginggirl','karolinabeaudet','marrycullen','runintoflowers','johnsparkssandf','Meggssmithh','littlelargo','TheButtonMaker','gracie_baldwin','nellieviloria','carol1977','coquidv','nds3535','enchantedmuse','fuchia57','wendi_gratz','ozbarb','willemijn26','jonathan930','fritela','deboernicole','msjoni56','hrtmb','thedreamerco','wilko2412','mllenorma','brandyo71','paigenyna','federicandco','disneymagic','freeallorcas','mmbfotografia','yannbros','sextoysestore','almapropia','philip1227','Souyzee','plainsimplehome','creddie','Hoosierpin84','charisseandrews','tay7lor','shaunashaw','debmalewski','nancylilypad','unodedos','namolio','emilyvvhite0637','hella49','meryltruett','thehananaa','HerPoisonMind','leerburg','MuffinMerriam','dfco','vionavandijk','jurakoncius','resmarie','zbrown115','wallinbuerkle','peppermintsplay','julier','marybethlarson','jannyroo','trendswb','POPSUGARPets','ivabrozkova','crescentmoon06','ameliamims','iminclover','equestrianco','Scarrick23','vall','blank2325','ginavalerio','montanameador','filmingbear321','shadowdog','loldamn','englandathomeuk','kateuhry','bioyoshimoto','czarchild51','esdesigns','ticktock7','ahirose','rocioespina','cuudulieutrsang','emperornorton47','shorterdigital','sue_aylesbury','jaxonmike','agneteemilie','lesaiz','shaehopkins','FaithOConnor9','ltree21','JeanneMelanson','gtrzilla','lizziekailey','dolerf','cnccookbook']
	dogPins = []#collects pin count per board
	
	t=0
	for x in range(0, 150):
		data = getBoardInfo(dogUsers[t],'dogs') #search 150 users' boards who all have a board titled dogs
		print t
		print dogUsers[t]
		print "Dog pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "Dogs board created at:"
		date = data["data"]["created_at"]
		dateOnly = parser(date)
		dogPins.append([dateOnly,data["data"]["counts"]["pins"],dogUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print dogPins[0:150] #print out all 150 users' information
	sortedDogs = sorted(dogPins,key=itemgetter(0)) #sort the creation dates
	print "sortedDogs", sortedDogs

	#save data to a file to be opened in excel and plotted
	with open('dogdata.txt', 'w') as outfile:
		s = str(sortedDogs)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	return sortedDogs

def cat(): #preform data mining
	catUsers = ['paola_gambetti','juwely','pribomilcar','laineyok','warda278','joyceeuverman','GGBeautifulLife','ozbarb','elizspinohza','sapperlott','11je12je','christelkelz','genevievekoenig','cisnerosmtz','LebenTina','streetform','amandaonwriting','teenwitches','honeybea1982','muttimamma','enmibolso','funnyordie','whippets4ever','BrokenDarkenss','perpetualkid','popupshop','applering','minandaminanda','liten','FrankieZeus','asemar','peterfwisser','socovina','theforestideas','SandraMeier','unodedos','cynthikelly','maryelizadoane','fetchsilversp','Souyzee','swtharvestmoon','SnoodleDoodles','jwmchristie','samegarr','AnkeWeckmann','retrogoddess','swallowtail8','archidaniels','deboernicole','Busy_Beesz','AlessandrD','karosj','Hanatirusato','keyen2','kenderfrau','letilor','babayaga1','carlavangalen','alaridesign','kasemier','MarciaCarrillo','queenzofia','InAustralia','judioliver','nuria1966','2lifestyle','morejoea','conquette','catsandkittys','l0503','bethany_s','sirenasnails','eziosgrandma','gracie_baldwin','queenmanu','thedreamerco','Seamssewcool','enid','avlogginggirl','swipurr','label29','nancydooren','iraco','mullenbry','lilmsjess','mixzublue','margot59','mzpeach','glutenfreemaman','noraburns','Turnike','avlogginggirl','paulamildon','mixzublue','Lazygirlsbeauty','tessalee','minimimi18','Meggssmithh','chihuahuabites','Eljy','eziosgrandma','fritela','arielmeier','susanelise','inyrdreemz','catslikeus','thcrazyteaparty','motleycrafter','juhbueno','zatras','FunnyBratt','napaneedlepoint','ltblogged','pamgreer','nuria1966','hopihapi','ravenlost','mllenorma','littlelargo','fofysfactory','hgaller','jcphoto','candilou31','TanuLee','Hoosierpin84','willemijn26','msjoni56','marier24','shotbyshola','mamacitalopez62','imreagnes','jogo10','emilyvvhite0637','karakulia','swsana','misshenriques','junyatate','ofallonlibrary','ticktock7','FaithOConnor9','catlover24','thepinksamurai','enchantedmuse','bunchou2','teresasoares','hella49','aylinkilic','marilynfranko','kittykataqua','paola_sigal']
	catPins = []#collects pin count per board

	t=0
	for x in range(0, 150):
		data = getBoardInfo(catUsers[t],'cats') #search 150 users' boards 
		print t
		print catUsers[t]
		print "Cat pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "Cats board created at:"
		date = data["data"]["created_at"] 
		dateOnly = parser(date)
		catPins.append([dateOnly,data["data"]["counts"]["pins"],catUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print catPins[0:150] #print out all 150 users' information

	sortedCats = sorted(catPins,key=itemgetter(0)) #sort the creation dates
	print "sortedCats", sortedCats

	#save data to a file to be opened in excel and plotted
	with open('catdata.txt', 'w') as outfile:
		s = str(sortedCats)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	
	return sortedCats

def getDateTimeFromISO8601String(s):
    d = dateutil.parser.parse(s)
    return d

def bunnies(): #preform data mining on BUNNIES category
	with open('bunnies.txt', 'r') as f: #read in 150 usernames from file
			bunniesUsers = [line.rstrip('\n') for line in f] #save into List

	bunnyPins = [] #collects pin count per board

	t=0
	for x in range(0, 150):
		data = getBoardInfo(bunniesUsers[t],'bunnies') #search 150 users' boards 
		print t
		print bunniesUsers[t]
		print "Bunny pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "Bunnies board created at:"
		date = data["data"]["created_at"]
		dateOnly = parser(date)
		bunnyPins.append([dateOnly,data["data"]["counts"]["pins"],bunniesUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print bunnyPins[0:150] #print out all 150 users' information

	sortedBunnies = sorted(bunnyPins,key=itemgetter(0)) #sort the creation dates
	print "sortedBunnies", sortedBunnies

	#save data to a file to be opened in excel and plotted
	with open('bunnydata.txt', 'w') as outfile:
		s = str(sortedBunnies)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	return sortedBunnies

def summer(): 
	with open('summer.txt', 'r') as f: #read in 150 usernames from file
			summerUsers = [line.rstrip('\n') for line in f] #save into List

	summerPins = [] #collects pin count per board

	t=0
	for x in range(0, 150):
		data = getBoardInfo(summerUsers[t],'summer') #search 150 users' boards 
		print t
		print summerUsers[t]
		print "Summer pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "Summer board created at:"
		date = data["data"]["created_at"]
		dateOnly = parser(date)
		summerPins.append([dateOnly,data["data"]["counts"]["pins"],summerUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print summerPins[0:150] #print out all 150 users' information

	sortedSummer = sorted(summerPins,key=itemgetter(0)) #sort the creation dates
	print "sortedSummer", sortedSummer

	#save data to a file to be opened in excel and plotted
	with open('summerdata.txt', 'w') as outfile:
		s = str(sortedSummer)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	return sortedSummer

def winter(): #preform data mining 
	with open('winter.txt', 'r') as f: #read in 150 usernames from file
			winterUsers = [line.rstrip('\n') for line in f] #save into List

	winterPins = [] #collects pin count per board

	t=0
	for x in range(0, 150):
		data = getBoardInfo(winterUsers[t],'winter') #search 150 users' board
		print t
		print winterUsers[t]
		print "winter pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "winter board created at:"
		date = data["data"]["created_at"]
		dateOnly = parser(date)
		winterPins.append([dateOnly,data["data"]["counts"]["pins"],winterUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print winterPins[0:150] #print out all 150 users' information

	sortedWinter = sorted(winterPins,key=itemgetter(0)) #sort the creation dates
	print "sortedWinter", sortedWinter

	#save data to a file to be opened in excel and plotted
	with open('winterdata.txt', 'w') as outfile:
		s = str(sortedWinter)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	return sortedWinter

def fall(): #preform data mining 
	with open('fall.txt', 'r') as f: #read in 150 usernames from file
			fallUsers = [line.rstrip('\n') for line in f] #save into List

	fallPins = [] #collects pin count per board

	t=0
	for x in range(0, 150):
		data = getBoardInfo(fallUsers[t],'fall') #search 150 users' boards who all have a board titled dogs
		print t
		print fallUsers[t]
		print "fall pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "fall board created at:"
		date = data["data"]["created_at"]
		dateOnly = parser(date)
		fallPins.append([dateOnly,data["data"]["counts"]["pins"],fallUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print fallPins[0:150] #print out all 150 users' information

	sortedFall = sorted(fallPins,key=itemgetter(0)) #sort the creation dates
	print "sortedFall", sortedFall

	#save data to a file to be opened in excel and plotted
	with open('falldata.txt', 'w') as outfile:
		s = str(sortedFall)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	return sortedFall

def spring(): #preform data mining 
	with open('spring.txt', 'r') as f: #read in 150 usernames from file
			springUsers = [line.rstrip('\n') for line in f] #save into List

	springPins = [] #collects pin count per board

	t=0
	for x in range(0, 150):
		data = getBoardInfo(springUsers[t],'spring') #search 150 users' boards 
		print t
		print springUsers[t]
		print "spring pins:"
		print data["data"]["counts"]["pins"] #enter data and counts to print pin
		print "spring board created at:"
		date = data["data"]["created_at"]
		dateOnly = parser(date)
		springPins.append([dateOnly,data["data"]["counts"]["pins"],springUsers[t]]) #store a list of [created date, pins, user] in a tuple
		t=t+1

	print springPins[0:150] #print out all 150 users' information

	sortedSpring = sorted(springPins,key=itemgetter(0)) #sort the creation dates
	print "sortedSpring", sortedSpring


	#save data to a file to be opened in excel and plotted
	with open('springdata.txt', 'w') as outfile:
		s = str(sortedSpring)
		s = s.split("], [") #parse between each tuple to create a new line
		json.dump(s, outfile , indent = 3)
	return sortedSpring

def main(): 
	
	#Mine different types of boards for pin counts under the following ANIMALS. Save data to a txt file to be parsed and displayed in excel
	dog()
	cat()	
	bunnies()

	#Mine all four seasons for pin count. Save data to a txt file to be parsed and displayed in excel.
	#summer()
	#winter()
	#spring()
	#fall()


if __name__ == "__main__":# main()
    import sys
    main()