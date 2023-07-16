from scrap import data as y
import matplotlib.pyplot as plt
import numpy as np

def kernel_reg(y, h):
    sse = 10000
    approximated_y = []
    while sse > 1000:
        for i in range(len(y)):
            w = [(1 / np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * (((i + 1) - j) / h) ** 2) for j in range(1, len(y))]
            approximated_y.append(sum(list(map(lambda w_value, y_value: w_value * y_value, w, y))) / sum(w))
        sse = sum([(y[i] - approximated_y[i]) ** 2 for i in range(len(y))])
        print(sse)
        y = approximated_y[:]
        approximated_y = []
    return y


if __name__ == '__main__':
    windows = [1, 3, 7]
    x = [i for i in range(len(y))]
    y = [i + (0.3 * np.random.normal()) for i in y]
    result = [kernel_reg(y, window) for window in windows]

    fig, ax = plt.subplots()
    ax.set_title('SBER')
    ax.set_xlabel('x')
    ax.set_ylabel('Rub')
    ax.grid()
    ax.plot(x, y)
    ax.plot(x, result[0])
    ax.plot(x, result[1])
    ax.plot(x, result[2])
    ax.legend(('original+noise',
               f'h1 = {windows[0]}',
               f'h2 = {windows[1]}',
               f'h3 = {windows[2]}'))
    plt.show()
