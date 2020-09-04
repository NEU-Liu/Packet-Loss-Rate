import matplotlib.pyplot as plt


def plot():
    y1 = [10, 13, 5, 40, 30, 60, 70, 12, 55, 25]
    x1 = range(0, 10)
    x2 = [2, 4, 6, 8, 9, 10, 11, 12, 13, 14]
    y2 = [5, 8, 0, 30, 20, 40, 50, 10, 40, 15]
    plt.plot(x1, y1, label='Theoretical Value', linewidth=3, color='r', markerfacecolor='blue', markersize=12)
    plt.plot(x2, y2, label='Calculated Value', linewidth=3, color='b', markerfacecolor='red', markersize=12)
    plt.xlabel('Second')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    plot()
