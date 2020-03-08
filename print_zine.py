#!/usr/bin/python3

######################
# Machine Yearning
# Nadine Lessio | Lee Wilkins
# Feb 2020
# unicode page: https://en.wikipedia.org/wiki/Code_page_437
######################

from __future__ import print_function
import random
import textwrap
import time
import glob
from random import choice
from threading import Thread
from PIL import Image
from datetime import datetime
from thermalprinter import *

from yearning import yearning

print("loaded libraries")

#### LOAD PRINTER #######################################

try:
	printer = ThermalPrinter(port="/dev/cu.usbserial-A4016WUR", baudrate=9600, timeout=5, heat_time=200, heat_interval=10, most_heated_point=200)
except:
	print("no printer")
	print("")
	print("")

print("loaded printer")

#### TEXT #######################################

text_list = ("One", """To the man who smiled at me in the Sofia subway. 
You: faint. Saw You when I Was a Boy. An Idiot Wish
An Idiot Wouldn't Tell You This Maybe. 
- by Looking""")


#### Images #######################################

def getImages():
	img_list = []
	for filename in glob.glob('images/*.png'): 
		im = Image.open(filename)
		#im.thumbnail((95,95))
		img_list.append(im)
	return img_list

image_list = getImages()
print(len(image_list))

############### ON SCREEN TESTING ####################### 

def onScreenHeader():
	title = "MACHINE YEARNING [1.0]"
	tp = "{0}{1}{2}".format("╪╪ ",title," ╪╪")
	print("{:^32}".format(tp))
	print("{:^32}".format("by Lee, Hil, Nadine"))
	print("{:^32}".format("Stupidhacks TO 2020"))
	print("{:^32}".format("♥♥♥ ╪╪╪ ♥♥♥"))
	print("")


def printOnScreen(text):
	title = text[0]
	poem = text[1].split('\n')
	poem = [x for x in poem if x.strip()]
	tp = "{0}{1}{2}".format("╤╩╤╩╤╩╤╩ ",title," ╤╩╤╩╤╩╤╩")
	print("{:^32}".format(tp))
	print("")
	for i in poem:
		d = textwrap.dedent(i).strip()
		w = textwrap.fill(d,width=32)
		print("{0}{1}".format(w,"\n"))
	print("")
	print("")


def allOnScreen(t):
	onScreenHeader()
	for i in t:
		printOnScreen(i)



############### PRINTER ################################# 

def printHeader():
	title = "MACHINE YEARNING [1.0]"
	#tp = "{0}{1}{2}".format("+++ ",title," +++")
	tp = "{0}{1}{2}".format("╪╪ ",title," ╪╪")
	printer.feed(1)
	printer.out("{:^32}".format(tp),bold=True)
	printer.out("{:^32}".format("by: Lee, Hil, Nadine"))
	printer.out("{:^32}".format("for: StupidhacksTO 2020"))
	printer.out("{:^32}".format("♥♥♥ ╪╪╪ ♥♥♥"))
	printer.feed(2)

def printOne(text):
	#printer.out("{:^32}".format("╤╩╤╩╤╩"),bold=True)
	title = text[0]
	poem = text[1].split('\n')
	poem = [x for x in poem if x.strip()]
	tp = "{0}{1}{2}".format("╤╩╤╩╤╩╤╩ ",title," ╤╩╤╩╤╩╤╩")
	printer.out("{:^32}".format(tp),bold=True)
	printer.feed(1)
	
	for i in poem:
		d = textwrap.dedent(i).strip()
		w = textwrap.fill(d,width=32)
		printer.out("{0}{1}".format(w,"\n"))
	printer.feed(2)

def printAll(t):
	printHeader()
	for i in t:
		printOne(i)
		time.sleep(2)

	printer.feed(3)

printHeader()
#onScreenHeader()
#printAll(yearning)
#allOnScreen(yearning)
#printOnScreen(yearning[2])

#printAll(yearning)
#printOne(random.choice(yearning))
