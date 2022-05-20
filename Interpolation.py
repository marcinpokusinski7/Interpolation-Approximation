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
        X = np.linspace(0, 14, 100)
        plt.plot(X, np.polyval(L, X))
        plt.savefig("line.jpg")
        plt.grid(True)
        img = Image.open('line.jpg')
        img.show()
        Errors.errors(x, y)

         #new_x = np.linspace(x[0], x[-1])
         #new_y = poly(new_x)

        # plt.plot(x, y, "o", new_x, new_y)
        # plt.xlim([x[0] - 1, x[-1] + 1])
        #
        #
        # plt.show()
