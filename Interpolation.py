from PIL import Image
import sklearn.neighbors
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.interpolate import lagrange

from Errors import Errors


class Interpolation:
    @classmethod
    def interpolationMethod(self, x, y):
        # polynomialCalculated = np.polyfit(x, y, z)
        # poly = np.poly1d(polynomialCalculated)
        # print("------ Wielomian : ------\n" + str(poly))  # Generate and plot the points

        plt.plot(x, y, 'o')

        #  Calculate the polynomial coefficients
        LagrangeCalculated = lagrange(x, y)
        L = Polynomial(LagrangeCalculated).coef
        print("Współczynniki wielomianu: " + str(L))
        new_y = np.poly1d(L)
        print("Wielomian :" + str(new_y))
        #  plot the polynomial
        Errors.errors(x, y)
        X = np.linspace(x[0], x[-1])

        # Preparing a plot with values from polyval
        plt.plot(X, np.polyval(L, X))
        plt.savefig("line.jpg")
        plt.grid(True)
        img = Image.open('line.jpg')
        img.show()
