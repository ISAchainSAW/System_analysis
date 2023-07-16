import matplotlib.pyplot as plt
from func import invert, peak
from Scrap import pay as data
from Scrap import pay_len


def end(data):
    flag = True
    c = []  # Высокочастотная функция
    r = []  # Остаток -> новые данные
    data2 = invert(data)  # Отрицательные значения
    h, xx = peak(data, pay_len, data2, False)  # xx -> Дельта h - приближение
    if xx < 0.1:  # Эпсилон
        c = h.copy()
    # print(xx)
    while flag:
        data2 = invert(h)
        h, xx = peak(h, pay_len, data2, False)
        # print(xx)
        if xx < 0.1:  # Эпсилон
            c = h.copy()
            flag = False

    # Вычисление функции r -> новых данных
    for i in range(len(data)):
        r.append(data[i] - c[i])

    plt.subplot(211)
    plt.title('c(t)')
    plt.plot(c, color="red")  # high frquency
    plt.grid()
    plt.subplot(212)
    plt.title('r(t)')
    plt.plot(r, color="black")  # low frquency
    plt.grid()
    plt.show()
    return r, c


tmp = []  # Собрать исходную функцию
a1, c1 = end(data)
a2, c2 = end(a1)
a3, c3 = end(a2)
a4, c4 = end(a3)

plt.plot(data, color='Black')
plt.plot(a1, color='red')
plt.plot(a2, color='brown')
plt.plot(a3, color='blue')
plt.plot(a4, color='orange')
plt.legend(['data', 'r1', 'r2', 'r3', 'r4'])
plt.grid()
plt.show()

for i in range(len(data)):
    tmp.append(c1[i] + c2[i] + c3[i] + c4[i] + a4[i])

plt.plot(data, color='Black')
plt.plot(tmp, color='blue', linestyle='--')
plt.legend(['data', 'recover_data'])
plt.grid()
plt.show()

plt.subplot(511)
plt.title('data(t)')
plt.grid()
plt.plot(data, color='Black')
plt.subplot(512)
plt.title('c1(t)')
plt.grid()
plt.plot(a1, color='red')
plt.subplot(513)
plt.title('c2(t)')
plt.grid()
plt.plot(a2, color='brown')
plt.subplot(514)
plt.title('c3(t)')
plt.grid()
plt.plot(a3, color='blue')
plt.subplot(515)
plt.title('r4(t)')
plt.plot(c4, color='orange')
plt.grid()
plt.show()
