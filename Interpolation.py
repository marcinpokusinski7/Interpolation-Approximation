from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import max_error

from Errors import Errors


class Interpolation:
    @classmethod
    def interpolationMethod(self, x, y, z):
        polynomialCalculated = np.polyfit(x, y, z)
        poly = np.poly1d(polynomialCalculated)
        print("------ Wielomian : ------\n" + str(poly))

        Errors.errors(x, y)

        new_x = np.linspace(x[0], x[-1])
        new_y = poly(new_x)

        plt.plot(x, y, "o", new_x, new_y)
        plt.xlim([x[0] - 1, x[-1] + 1])
        plt.savefig("line.jpg")
        open('line.jpg')
        plt.show()
