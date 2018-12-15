import csv
from tkinter import*


window=Tk()
window.title("Options")

window.geometry("230x270")
window.configure(bg = '#000022')

def year():
    window.destroy()
    with open('data.csv', 'r') as theFile:
        file = csv.reader(theFile)
        a=input('Input the year:')
        for line in file:
            if line[0] == a or line[0]== 'Year':
                print(line)
    exit()


def number():
    window.destroy()
    with open('data.csv', 'r') as theFile:
        file = csv.reader(theFile)
        a=input('Input the number of deaths:')
        for line in file:
            if line[4] == a or line[0]== 'Year':
                print(line)

        exit()


def reason():
    window.destroy()
    with open('data.csv', 'r') as theFile:
        file = csv.reader(theFile)
        string = input("Input the reason of death:")
        string = string.lower()
        x=0
        for line in file:
            lineLower = line[1].lower()
            if lineLower.find(string) != -1 or line[0]== 'Year':
                print(line)
                y = calculations(x)
                a=swap(y)
                x=a
        if x == 1:
            print('No data found.')
    exit()


def name():
    window.destroy()
    with open('data.csv', 'r') as theFile:
        file = csv.reader(theFile)
        string = input("Input the name of disease:")
        string = string.lower()
        x=0
        for line in file:
            lineLower = line[2].lower()
            if lineLower.find(string) != -1 or line[0]== 'Year':
                print(line)
                y = calculations(x)
                a=swap(y)
                x=a
        if x == 1:
            print('No data found.')
    exit()


def state():
    window.destroy()
    with open('data.csv', 'r') as theFile:
        file = csv.reader(theFile)
        string = input("Input the state name:")
        string = string.lower()
        x=0
        for line in file:
            lineLower = line[3].lower()
            if lineLower.find(string) != -1 or line[0]== 'Year':
                print(line)
                y = calculations(x)
                a=swap(y)
                x=a
        if x == 1:
            print('No data found.')
    exit()


def rate():
    window.destroy()
    with open('data.csv', 'r') as theFile:
        file = csv.reader(theFile)
        string = input("Input the rate:")
        string = string.lower()
        x=0
        for line in file:
            lineLower = line[5].lower()
            if lineLower.find(string) != -1 or line[0]== 'Year':
                print(line)
                y = calculations(x)
                a=swap(y)
                x=a
        if x == 1:
            print('No data found.')
    exit()


def calculations(x):
    x = x+1
    return x

def swap(y):
    a=y
    return a


Label(window, text="Search by what?", font= 20).grid()

Button(window, text="by DEATH YEAR", width=20, font= 5, command=year).grid(row=3, column=0)
Button(window, text="by REASON OF DEATH", width=20, font= 5, command=reason).grid(row=4, column=0)
Button(window, text="by DISEASE NAME", width=20, font= 5, command=name).grid(row=5, column=0)
Button(window, text="by STATE", width=20, font= 5, command=state).grid(row=6, column=0)
Button(window, text="by NUMBER OF DEATHS", width=20, font= 5, command=number).grid(row=7, column=0)
Button(window, text="by DEATH RATE", width=20, font= 5, command=rate).grid(row=8, column=0)


window.mainloop()
