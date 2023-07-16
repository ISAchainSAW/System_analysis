from scipy.interpolate import splev, splrep
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt


def invert(data):
    dat2 = []
    for i in data:
        dat2.append(i * -1)
    return dat2

def peak(data, data_len ,data2, flag):
    # Найти пики
    p = find_peaks(data)
    up_point = [[i for i in p[0]], [data[i] for i in p[0]]]  # 1 - y , 2 - x
    p2 = find_peaks(data2)
    down_point = [[i for i in p2[0]], [data[i] for i in p2[0]]]
    #Устранение кольцевого эффекта
    if data[0] < up_point[1][0] and data[0] < down_point[1][0]:
        down_point[1].insert(0, data[0])
        down_point[0].insert(0, data_len[0])
        up_point[1].insert(0, up_point[1][0])
        up_point[0].insert(0, data_len[0])

    elif data[0] > up_point[1][0] and data[0] > down_point[1][0]:
        down_point[1].insert(0, down_point[1][0])
        down_point[0].insert(0, data_len[0])
        up_point[1].insert(0, data[0])
        up_point[0].insert(0, data_len[0])

    elif down_point[1][0] < data[0] < up_point[1][0]:
        down_point[1].insert(0, down_point[1][0])
        down_point[0].insert(0, data_len[0])
        up_point[1].insert(0, up_point[1][0])
        up_point[0].insert(0, data_len[0])

    if data[-1] < up_point[1][-1] and data[-1] < down_point[1][-1]:
        down_point[1].append(data[-1])
        down_point[0].append(data_len[-1])
        up_point[1].append(up_point[1][-1])
        up_point[0].append(data_len[-1])

    elif data[-1] > up_point[1][-1] and data[-1] > down_point[1][-1]:
        down_point[1].append(down_point[1][-1])
        down_point[0].append(data_len[-1])
        up_point[1].append(data[-1])
        up_point[0].append(data_len[-1])

    elif down_point[1][-1] < data[-1] < up_point[1][-1]:
        down_point[1].append(down_point[1][-1])
        down_point[0].append(data_len[-1])
        up_point[1].append(up_point[1][-1])
        up_point[0].append(data_len[-1])


    # Сплайны
    spl = splrep(up_point[0], up_point[1])
    spl2 = splrep(down_point[0], down_point[1])
    x = np.linspace(0, max(data_len)+1, max(data_len)+1)
    y1 = splev(x, spl)
    y2 = splev(x, spl2)

    # Линия тренда
    m = []  # Средняя
    for i, j in zip(y1, y2):
        m.append((i + j) / 2)
    last_avg =m[-1]

    # m, x, y1, y2 = m[:-1], x[:-1], y1[:-1], y2[:-1]

    # Приближение
    h1 = []  # Приближение
    for i in range(len(data)):
        h1.append(data[i] - m[i])

    if flag:
        # Строим график
        plt.plot(data, color="red")  # data
        plt.plot(x, m, color="blue", )  # avg
        plt.plot(x, y1, color='black', )  # spline
        plt.plot(x, y2, color='black', )  # spline
        plt.plot([up_point[0]], [up_point[1]], color='blue', marker='o')  # max
        plt.plot([down_point[0]], [down_point[1]], color='orange', marker='o')  # min
        plt.legend(['data', 'avg', 'spline_up', 'spline_down', 'max_peak', 'min_peak'])
        plt.grid()
        plt.show()


    tmp = 0  # Дельта
    for i in range(len(data)):
        tmp += (abs(h1[i] - data[i]) ** 2 / data[i] ** 2)
    return h1, tmp
