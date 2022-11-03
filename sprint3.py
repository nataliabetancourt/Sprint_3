#Imports
from tkinter import *
import pandas as pd
from scipy import spatial


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
    #Get input user and add to array
    indexTarget = data.index[data['Nombre'] == chosenName.get() ].tolist()
    arrayTarget = []
    for i in data.iloc[indexTarget]:
        arrayTarget.append(i)

    #Go through data of other users to get distance
    for x in range(10):
        #Create array of distances
        distance = []

        #Add info to an array
        otherUser = []
        for i in data.iloc[x]:
            otherUser.append(i)

        print(arrayTarget)
        print(otherUser)

        #Get the distance of cosine between the selected and the others
        #result = 1 - spatial.distance.cosine(arrayTarget, otherUser)
        #distance.append(result)
        #print(distance)


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
