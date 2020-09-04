import matplotlib.pyplot as plt
import math


#   p1 = 1 - math.sqrt(s/n)
#   p2 = 1 - s/n
#   p3 = (1 - s/n)*0.5


def readSimulationDataAndComputeP1(filename):
    with open(filename, "r") as f:
        column = []
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            temp += float(wordlist[0])
            if index % 32 == 0 and index != 0:
                out = 1 - math.sqrt(temp * 1.0 / index)
                column.append(out)
            index += 1
            if index == 8192:
                break
    f.close()
    return column


def readSimulationDataAndComputeP2(filename):
    with open(filename, "r") as f:
        column = []
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            temp += float(wordlist[0])
            if index % 32 == 0 and index != 0:
                out = 1 - (temp * 1.0 / index)
                column.append(out)
            index += 1
            if index == 8192:
                break
    f.close()
    return column


def readSimulationDataAndComputeP3(filename):
    with open(filename, "r") as f:
        column = []
        index = 0
        temp = 0
        for line in f:
            wordlist = line.split()
            temp += float(wordlist[0])
            if index % 32 == 0 and index != 0:
                out = 0.5 * (1 - (temp * 1.0 / index))
                column.append(out)
            index += 1
            if index == 8192:
                break
    f.close()
    return column


def readRealLoss():
    real = []
    for i in range(256):
        real.append(0.1352)
    return real


def plot(filename):
    real = readRealLoss()
    plt.plot(real, label="theoretical value", linewidth=1)
    loss = readSimulationDataAndComputeP1(filename)
    plt.plot(loss, label="1-math.sqrt(s/n)", linewidth=1)
    lossv1 = readSimulationDataAndComputeP2(filename)
    plt.plot(lossv1, label="1-s/n", linewidth=1)
    lossv2 = readSimulationDataAndComputeP3(filename)
    plt.plot(lossv2, label="0.5x(1-s/n)", linewidth=1)
    plt.xlabel("Each scale represents 32 packets", fontsize=15)
    plt.ylabel("Packet Loss Rate", fontsize=15)
    plt.tick_params(axis='both', labelsize=10)
    plt.legend()
    plt.savefig("./compare.png")
    plt.show()


if __name__ == '__main__':
    plot("simple.txt")
