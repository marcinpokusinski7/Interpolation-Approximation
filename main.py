from sklearn.metrics import mean_squared_error, mean_absolute_error

import Interpolation
import numpy as np

import Approximation


def printMenu():
    print("Menu")
    print(" Wcisnij 1 - Interpolacja \n"
          " Wcisnij 2 - Aproksymacja \n"
          " Wcisnij 3 - Aby wyświetlić ponownie \n"
          " Wcisnij 4 - Zakończ ")
    while True:
        try:
            n = int(input("Wybierz z menu: "))
            Menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


def Menu(status):
    if status == 1:
        return interpolation()
    if status == 2:
        return approximationMethod()
    if status == 3:
        return printMenu()
    if status == 4:
        exit()
    else:
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
            Menu(n)
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

    z = int(input("Wielomian stopnia : "))

    splittedArrayOfPoints = np.array(mainArray)
    print(mainArray)
    x = splittedArrayOfPoints[:, 0]
    print("Punkty x :" + str(x))
    y = splittedArrayOfPoints[:, 1]
    print("Punkty y :" + str(y))
    Interpolation.Interpolation.interpolationMethod(x, y, z)

    while True:
        try:
            n = int(input("Wybierz z menu: "))
            Menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break


print("Menu")
print(" Wcisnij 1 - Interpolacja \n"
      " Wcisnij 2 - Aproksymacja \n"
      " Wcisnij 3 - Aby wyświetlić ponownie \n"
      " Wcisnij 4 - Zakończ ")

while True:
    try:
        n = int(input("Wybierz z menu: "))
        Menu(n)
    except ValueError:
        print("Nie ma takiej opcji, wybierz ponownie: ")
    else:
        break
