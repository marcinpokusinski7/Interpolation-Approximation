import warnings
from tkinter import *
from tkinter.filedialog import askopenfilename
import Interpolation
import numpy as np
import Approximation

warnings.filterwarnings('ignore')


def chooseReading():
    print("Wybierz w jaki sposób chcesz dostarczy punkty do programu \n"
          "\r1 - Excel \n"
          "\r2 - Konsola \n"
          "\r5 - Zakończ ")

    while True:
        try:
            choose = int(input("Wybierz z menu: "))
            if choose == 1:
                return excelRead()
            if choose == 2:
                return printMenu()
            if choose == 5:
                quit()
                return "Błąd"
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
            print("Wybierz w jaki sposób chcesz dostarczy punkty do programu \n"
                  "\r1 - Excel \n"
                  "\r2 - Konsola \n"
                  "\r5 - Zakończ ")
            chooseReading()
        else:
            break


def excelRead():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)

    printMenu()


def printMenu():
    print("Menu")
    print(" Wcisnij 1 - Interpolacja \n"
          " Wcisnij 2 - Aproksymacja \n"
          " Wcisnij 3 - Aby wyświetlić ponownie \n"
          " Wcisnij 4 - Wróć do wyboru excel/konsola\n"
          " Wcisnij 5 - Zakończ ")
    while True:
        try:
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
            print(" Wcisnij 1 - Interpolacja \n"
                  " Wcisnij 2 - Aproksymacja \n"
                  " Wcisnij 3 - Aby wyświetlić ponownie \n"
                  " Wcisnij 4 - Wróć do wyboru excel/konsola\n"
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
    Approximation.Approximation.approximationMethod(x, y)

    while True:
        try:
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


def interpolation():
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
    Interpolation.Interpolation.interpolationMethod(x, y)

    while True:
        try:
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


chooseReading()

while True:
    try:
        print(" Wcisnij 1 - Interpolacja \n"
              " Wcisnij 2 - Aproksymacja \n"
              " Wcisnij 3 - Aby wyświetlić ponownie \n"
              " Wcisnij 4 - Wróć do wyboru excel/konsola\n"
              " Wcisnij 5 - Zakończ ")
        n = int(input("Wybierz z menu: "))
        menu(n)
    except ValueError:
        print("Nie ma takiej opcji, wybierz ponownie: ")
    else:
        break
