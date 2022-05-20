import sklearn.neighbors
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from Errors import Errors


class Approximation:
    @classmethod
    def approximationMethod(self, z, y):
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

        polynomialCalculated = np.polyfit(xdata, fit_y, 2)
        poly = np.poly1d(polynomialCalculated)
        print(poly)

        Errors.errors(xdata, fit_y)
        plt.savefig("line.jpg")
        img = Image.open('line.jpg')
        img.show()
        plt.legend()
        plt.show()
