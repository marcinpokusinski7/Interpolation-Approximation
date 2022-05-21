import sklearn.neighbors
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from scipy.optimize import curve_fit
from numpy.polynomial import Polynomial
from Errors import Errors


class Approximation:
    @classmethod
    def approximationMethod(self, z, y, c):
        # gauss method
        xdata = np.asarray(z)
        ydata = np.asarray(y)
        plt.plot(xdata, ydata, 'o')

        # Define the Gaussian function
        def Gauss(x, A, B):
            y = A * np.exp(-1 * B * x ** 2)
            return y

        parameters, covariance = curve_fit(Gauss, xdata, ydata)

        fit_A = parameters[0]
        fit_B = parameters[1]

        fit_y = Gauss(xdata, fit_A, fit_B)
        print(fit_y)
        plt.plot(xdata, ydata, 'o', label='data')
        plt.plot(xdata, fit_y, '-', label='fit')

        LagrangeCalculated = lagrange(z, y)
        L = Polynomial(LagrangeCalculated).coef
        print("Wielomian: " + str(L))

        Errors.errors(xdata, ydata)
        plt.savefig("line.jpg")
        plt.legend()
        img = Image.open('line.jpg')
        img.show()


