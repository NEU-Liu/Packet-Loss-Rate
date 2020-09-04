import matplotlib.pyplot as plt
import math


#   p1 = 1 - math.sqrt(s/n)
#   p2 = 1 - s/n
#   p3 = (1 - s/n)*0.5


def readSimulationDataAndComputeP1(filename):
    with open(filename, "r") as f:
        column = []
        times = []
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            temp += float(wordlist[0])
            if index % 1000 == 999:
                out = 1 - math.sqrt(temp * 1.0 / 1000)
                column.append(out)
                times.append((index + 1) / 1000)
                temp = 0
            index += 1
            if index == 100000:
                break
    f.close()
    print(times)
    return column, times


def readSimulationDataAndComputeP2(filename):
    with open(filename, "r") as f:
        column = []
        times = []
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            temp += float(wordlist[0])
            if index % 1000 == 999:
                out = 1 - (temp / 1000)
                column.append(out)
                times.append((index + 1) / 1000)
                temp = 0
            index += 1
            if index == 100000:
                break
    f.close()
    print(times)
    return column, times


def readSimulationDataAndComputeP3(filename):
    with open(filename, "r") as f:
        column = []
        times = []
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            temp += float(wordlist[0])
            if index % 1000 == 999:
                out = 0.5 * (1 - (temp / 1000))
                column.append(out)
                times.append((index + 1) / 1000)
                temp = 0
            index += 1
            if index == 100000:
                break
    f.close()
    print(times)
    return column, times


def readRealLoss(filename):
    with open(filename, "r") as f:
        loss = []
        time = []
        start = 0
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            loss.append(float(wordlist[0]))
            start += float(wordlist[1])
            time.append(start)
            index += 1
            if index == 35:
                break
    f.close()
    return loss, time


def plot0(filename1, filename2):
    loss, time = readRealLoss(filename1)
    plt.plot(time, loss, label="theoretical value", linewidth=2)
    closs, time = readSimulationDataAndComputeP1(filename2)
    plt.plot(time, closs, label="1-math.sqrt(s/n)", linewidth=2)
    plt.xlabel("Second", fontsize=15)
    plt.ylabel("Packet Loss Rate", fontsize=15)
    plt.tick_params(axis='both', labelsize=10)
    plt.legend()
    plt.savefig("./sqrt.png")
    plt.show()


def plot1(filename1, filename2):
    loss, time = readRealLoss(filename1)
    plt.plot(time, loss, label="theoretical value", linewidth=2)
    closs, time = readSimulationDataAndComputeP1(filename2)
    plt.plot(time, closs, label="1-math.sqrt(s/n)", linewidth=2)
    closs1, time1 = readSimulationDataAndComputeP2(filename2)
    plt.plot(time1, closs1, label="1-s/n", linewidth=2)
    closs2, time2 = readSimulationDataAndComputeP3(filename2)
    plt.plot(time2, closs2, label="0.5x(1-s/n)", linewidth=2)
    plt.xlabel("Second", fontsize=15)
    plt.ylabel("Packet Loss Rate", fontsize=15)
    plt.tick_params(axis='both', labelsize=10)
    plt.legend()
    plt.savefig("./compare.png")
    plt.show()


if __name__ == '__main__':
    plot0("./loss.txt", "./runoob.txt")
    plot1("./loss.txt", "./runoob.txt")
