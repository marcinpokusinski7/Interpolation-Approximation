import warnings
from tkinter import *
from tkinter.filedialog import askopenfilename

import numpy
from numpy import floor
from numpy.lib.npyio import loadtxt

import Interpolation
import numpy as np
import Approximation

warnings.filterwarnings('ignore')


def chooseReading():
    print("Wybierz w jaki sposób chcesz dostarczyc punkty do programu \n"
          "\r1 - Plik \n"
          "\r2 - Konsola \n")

    while True:
        try:
            choose = int(input("Wybierz z menu: "))
            if choose == 1:
                return excelRead()
            if choose == 2:
                return console()
        except ValueError:
            print("")
            print("Nie ma takiej opcji, wybierz ponownie: ")
            print("Wybierz w jaki sposób chcesz dostarczyc punkty do programu \n"
                  "\r1 - Plik \n"
                  "\r2 - Konsola \n")
        else:
            break


def excelRead():
    print("Aby pobrac punkty z Excela współrzędne X proszę podać w pierwszej linii odzielone spacją.\n"
          "Punkty Y proszę podać w kolejnej linii\n"
          "Jeżeli są to liczby zmiennoprzecinkowe proszę wstawić kropkę")
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    filename = askopenfilename()
    print("Opening : " + str(filename))
    with open(filename) as file:
        lines = loadtxt(file, dtype=str, comments="#", delimiter=",", unpack=False)
        print(lines)
    newArray = []
    newArray = np.array(np.split(lines, floor(len(lines))))
    middleIndex = int(floor(len(newArray) / 2))
    firstHalf = numpy.loadtxt(lines[:middleIndex])
    secondHalf = numpy.loadtxt(lines[middleIndex:])
    print(firstHalf)
    print(secondHalf)
    return firstHalf, secondHalf

    while True:
        try:
            print("")
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


def printMenu():
    print("Menu")
    print(" Wcisnij 1 - Interpolacja \n"
          " Wcisnij 2 - Aproksymacja \n"
          " Wcisnij 3 - Aby wyświetlić ponownie \n"
          " Wcisnij 5 - Zakończ ")
    while True:
        try:
            print("")
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
            print(" Wcisnij 1 - Interpolacja \n"
                  " Wcisnij 2 - Aproksymacja \n"
                  " Wcisnij 3 - Aby wyświetlić ponownie \n"
                  " Wcisnij 5 - Zakończ ")
        else:
            break


def menu(status):
    if status == 1:
        return interpolation()
    if status == 2:
        return approximationMethod()
    if status == 3:
        return printMenu()
    if status == 4:
        return chooseReading()
    if status == 5:
        quit()
        return "Błąd"


def approximationMethod():
    x, y = chooseReading()
    Approximation.Approximation.approximationMethod(x, y)

    while True:
        try:
            print("")
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


def console():
    mainArray = []
    n = int(input("Wprowadz ilość par współrzędnych punktów : "))
    for i in range(n):
        res = list(map(float, input("\nPodaj współrzędne punktów " + (i + 1).__str__() + " : ").strip().split()))[:n]
        print(res)
        mainArray.append(res)
    splittedArrayOfPoints = np.array(mainArray)
    print(mainArray)
    x = splittedArrayOfPoints[:, 0]
    print("Punkty x :" + str(x))
    y = splittedArrayOfPoints[:, 1]
    print("Punkty y :" + str(y))
    return x, y


def interpolation():
    x, y = chooseReading()
    Interpolation.Interpolation.interpolationMethod(x, y)

    while True:
        try:
            print("")
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


print("Menu")
print(" Wcisnij 1 - Interpolacja \n"
      " Wcisnij 2 - Aproksymacja \n"
      " Wcisnij 3 - Aby wyświetlić ponownie \n"
      " Wcisnij 5 - Zakończ ")

while True:
    try:
        print("")
        n = int(input("Wybierz z menu: "))
        menu(n)
    except ValueError:
        print("Nie ma takiej opcji, wybierz ponownie: ")
    else:
        break
