#Imports
from tkinter import *
import pandas as pd
import math

#Create frame where interaction happens
main = Tk()
main.geometry("400x400")

# Load csv - database
data = pd.read_csv('pizza.csv')

#Methods
def test():
    index = data.index[data['Nombre'] == chosenName.get() ].tolist()
    print(data.iloc[index])


def calculateDistance():
    indexTarget = data.index[data['Nombre'] == chosenName.get() ].tolist()
    target = data.iloc[indexTarget]
    distance = ((data.loc[:, 1]-target[1])**2 + (data.loc[:, 2]-target[2])**2 + (data.loc[:, 3]-target[3])**2 + (data.loc[:, 4]-target[4])**2 + (data.loc[:, 5]-target[5])**2 + (data.loc[:, 6]-target[6])**2 + (data.loc[:, 7]-target[7])**2) **0.5
    print(distance)


#List of names for dropdown menu from csv
names = data.loc[:, "Nombre"]
print(names)

#Chosen name variable
chosenName = StringVar()
chosenName.set(names[0])
print(chosenName.get())

# Create Dropdown menu
drop = OptionMenu( main , chosenName , *names )
drop.pack()

#Button for function to work
button = Button(main, text="Ejecutar", command= calculateDistance).pack()

# Create Label
label = Label(main, text = "El valor del index es: ")
label.pack()
testValue = Label( main , text = " " )
testValue.pack()

main.mainloop()
