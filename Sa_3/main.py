import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from functions import autoregression, trend, ma
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [5.30, 5.80, 5.60, 5.40, 5.20, 4.80, 4.80, 5.10, 4.70, 4.60, 4.80, 4.50, 4.10, 4.10]

res = ARIMA(y, order=(1, 1, 1))
res = res.fit()
# print(res.summary())
z = [i for i in range(17)]
pred = res.predict(start=0, end=16)
plt.title(f"ARMA 1,1,1")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(y, color='red')
plt.plot(pred)
plt.scatter(x, y, color='red')
plt.legend(['Original','Predict'])
plt.scatter(z, pred, color='black')
plt.grid()
plt.show()
arr = list(pred)
f = open("ARIMA_1_1_1.txt", 'w')
for i in arr:
    f.write((str(i) + '\n'))
f.close()

autoregression(x,y,2)
ma(y, 2, 2)
trend(x, y, 2)