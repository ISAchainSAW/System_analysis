import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [5.30, 5.80, 5.60, 5.40, 5.20, 4.80, 4.80, 5.10, 4.70, 4.60, 4.80, 4.50, 4.10, 4.10]

def ma(y, window_size, predict_window):
    """Функция скользящего среднего"""
    output_arr = []
    tmp = 0
    pw_tmp=predict_window
    yy = y[-predict_window:]
    for i in range(window_size - 1, len(y)):
        for j in range(window_size):
            tmp += y[i - j]
        tmp = tmp / window_size
        output_arr.append(tmp)
        tmp = 0
        if i == len(y) - 1:
            predict_window = predict_window - 1
            yy.append(output_arr[-1])
    for i in range(predict_window):
        for j in range(window_size):
            tmp += yy[len(yy) - 1 - j]
        tmp = tmp / window_size
        yy.append(tmp)
        output_arr.append(tmp)
        tmp = 0
    xx = [i for i in range(window_size, len(output_arr) + window_size)]
    plt.plot(x, y)
    plt.plot(xx, output_arr)
    plt.scatter(x, y)
    plt.scatter(xx, output_arr)
    plt.legend(['original', 'MA'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    for i in range(pw_tmp,0,-1):
        print(output_arr[-i])

    f = open(ma.__name__ + ".txt", 'w')
    for i in output_arr:
        f.write((str(i) + '\n'))
    f.close()


def trend(x, y, predict_window):
    """Функция линейного тренда"""
    x_sum = sum(x)
    y_sum = sum(y)
    xy = [i[0] * i[1] for i in zip(x, y)]
    xx = [i ** 2 for i in x]
    xx_sum = sum(xx)
    xy_sum = sum(xy)
    a0 = (y_sum * xx_sum - x_sum * xy_sum) / (len(x) * xx_sum - x_sum ** 2)
    a1 = (len(x) * xy_sum - x_sum * y_sum) / (len(x) * xx_sum - x_sum ** 2)
    print("a0 = ", a0)
    print("a1 = ", a1)
    yy = [a0 + i * a1 for i in range(1, len(x) + 1 + predict_window)]
    xx = [i for i in range(len(yy))]
    # for i in range(len(x)):
    #     print(x[i], yy[i])

    """Вывод на консоль предсказанных значений"""
    for i in range(predict_window, 0, -1):
        print(yy.index(yy[-i]), "= ", yy[-i])

    plt.plot(x, y)
    plt.plot(xx, yy)
    plt.scatter(x, y)
    plt.scatter(xx, yy)
    plt.legend(['Original', trend.__name__])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    f = open(trend.__name__ + ".txt", 'w')
    for i in yy:
        f.write((str(i) + '\n'))
    f.close()


def autoregression(x, y, predict_window):
    """Функция авторегрессии 1-го порядка"""
    tmp_x = y[:-1]
    tmp_y = y[1:]
    x_sum = sum(tmp_x)
    y_sum = sum(tmp_y)
    xy = [i[0] * i[1] for i in zip(tmp_x, tmp_y)]
    xx = [i ** 2 for i in tmp_x]
    xx_sum = sum(xx)
    xy_sum = sum(xy)
    a0 = (y_sum * xx_sum - x_sum * xy_sum) / (len(tmp_x) * xx_sum - x_sum ** 2)
    a1 = (len(tmp_x) * xy_sum - x_sum * y_sum) / (len(tmp_x) * xx_sum - x_sum ** 2)
    print("a0 = ", a0)
    print("a1 = ", a1)

    yy = [a0 + a1 * i for i in y]  # Calculated new array of y
    """Заполняем предсказанные значения"""
    for i in range(1, predict_window):
        yy.append(a0 + a1 * yy[-1])
    xx = [i for i in range(1, len(yy) + 1)]

    # print("x,y,y*")
    # for i in range(len(x)):
    #     print(x[i], y[i], yy[i])
    """Вывод на консоль предсказанных значений"""
    for i in range(predict_window, 0, -1):
        print(yy[-i])
    plt.plot(x, y)
    plt.plot(xx, yy)
    plt.scatter(x, y)
    plt.scatter(xx, yy)
    plt.legend(['Original', autoregression.__name__])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    f = open(autoregression.__name__ + ".txt", 'w')
    for i in yy:
        f.write((str(i) + '\n'))
    f.close()



