
from sklearn.metrics import mean_squared_error, mean_absolute_error, max_error
from sklearn.linear_model import LinearRegression

class Errors:
    @classmethod
    def errors(cls, fit_x, fit_y):
        # linear regression
        x = fit_x.reshape(-1, 1)
        regression_model = LinearRegression()
        regression_model.fit(x, fit_y)

        y_pred = regression_model.predict(x)
        MSE = mean_squared_error(fit_y, y_pred, squared=True)
        MAE = mean_absolute_error(fit_y, y_pred)
        print("------ Błędy średnie ------")
        print("MSE : " + MSE.__str__())
        print("MAE : " + MAE.__str__())
        print("------ Błąd maksymalny ------")
        print("Max error: " + max_error(fit_y, y_pred).__str__())
