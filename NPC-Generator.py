#Imports random library
import random

#Creates lists of all of my values
ages = [10,20,30,40,50,60,70,80,90,100]
heights = [4.0, 4.5, 5.3, 6.0, 6.3, 6.5]
eyecolors = ['blue', 'green', 'brown', 'black', 'white']
npc = []

#Loops code 10 times
for i in range(10):
    #Asks for input of NPC name and stores in variable
    npc1 = input('Enter an NPC name: ')
    #Chooses random age from ages list and stores in variable
    age1 = random.choice(ages)
    #Chooses random height from heights list and stores in variable
    height1 = random.choice(heights)
    #Chooses a number between 1-10000 and stores in variable
    power1 = random.randint(1, 10000)
    #Chooses random eyecolor from eyecolors list and stores in variable
    eyecolor1 = random.choice(eyecolors)
    #Adds all this data to a list
    npc.append(npc1)
    npc.append(age1)
    npc.append(height1)
    npc.append(power1)
    npc.append(eyecolor1)

#Prints all the data
print("\n\nName:",npc[0],"\nAge:",npc[1],"\nHeight:",npc[2],"\nPower:",npc[3],"\nEyecolor:",npc[4],
"\n\nName:",npc[5],"\nAge:",npc[6],"\nHeight:",npc[7],"\nPower:",npc[8],"\nEyecolor:",npc[9],
"\n\nName:",npc[10],"\nAge:",npc[11],"\nHeight:",npc[12],"\nPower:",npc[13],"\nEyecolor:",npc[14],
"\n\nName:",npc[15],"\nAge:",npc[16],"\nHeight:",npc[17],"\nPower:",npc[18],"\nEyecolor:",npc[19],
"\n\nName:",npc[20],"\nAge:",npc[21],"\nHeight:",npc[22],"\nPower:",npc[23],"\nEyecolor:",npc[24],
"\n\nName:",npc[25],"\nAge:",npc[26],"\nHeight:",npc[27],"\nPower:",npc[28],"\nEyecolor:",npc[29],
"\n\nName:",npc[30],"\nAge:",npc[31],"\nHeight:",npc[32],"\nPower:",npc[33],"\nEyecolor:",npc[34],
"\n\nName:",npc[35],"\nAge:",npc[36],"\nHeight:",npc[37],"\nPower:",npc[38],"\nEyecolor:",npc[39],
"\n\nName:",npc[40],"\nAge:",npc[41],"\nHeight:",npc[42],"\nPower:",npc[43],"\nEyecolor:",npc[44],
"\n\nName:",npc[45],"\nAge:",npc[46],"\nHeight:",npc[47],"\nPower:",npc[48],"\nEyecolor:",npc[49])
