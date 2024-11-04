# NPC-Generator

## 📚 Table of Contents

- 🌟 [Features](#-features)
- 📜 [Overview](#-overview)
- 👨‍💻 [Authors](#-authors)
- 💻 [Code Example](#-code-example)

## 🌟 Features

This program outputs the Data of 10 NPC's. It saves time by already having a list of values
which the the program chooses by random. It can be useful when trying to generate
random people or random data that you might need for other things.

## 📜 Overview

The purpose of this program is to create a Non-Playable Character generator for an open-world video game.
My goal was to develop a program which produces 10 unique characters with different attributes. My 
program firsts imports a library called random which allows you to generate random numbers in python.
I then create a list of values which consist of the attributes of the 10 NPCs. After that, I created
a for loop which asked for the name of the NPC, stored it in a variable, generated a random choice
from the list, ages, stored it into a variable, generated a random choice from the list, heights, 
stored it into a variable.generated a random choice from the list, eyecolors, stored it into a variable,
and choosed a random number between 1 and 10000 which was stored as the power level of the NPC. This for
loop repeated 10 times, gathering data of 10 NPCs. I then added all this data to a list called, npc. Lastly,
I printed all of this data out of the NPC attributes in a clear format. The motivation behind creating this
program was for a school project. The scenario was where I had to create an NPC generator for an open-world
video game. The game developers already designed the main characters, but needed an algorithm to create
diverse NPCs. My goal was to produce at least 10 of these NPCs.

### 👨‍💻 Authors

My name is Armaan and I was tasked with creating a NPC generator. I am in the Computer Science Program at
Voorhees, and this is one of the projects I had to complete for a grade. I am in 9th grade, and we are 
currently learning python. We had to do this project to show what we learned in this class.

## 💻 Code Example

The most important piece of code in my program was the for loop.

```python
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
```

This piece of code was really important because it gathered all the data of the NPC, and
appended all the data into one list. This then allowed me to print all the data for
the user to see.
