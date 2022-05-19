from sklearn.metrics import mean_squared_error, mean_absolute_error, max_error


class Errors:
    @classmethod
    def errors(cls, fit_y, xdata):
        MSE = mean_squared_error(xdata, fit_y)
        MAE = mean_absolute_error(xdata, fit_y)
        print("------ Błędy średnie ------")
        print("MSE : " + MSE.__str__())
        print("MAE : " + MAE.__str__())
        print("------ Błąd maksymalny ------")
        print("Max error: " + max_error(xdata, fit_y).__str__())
