import random

if __name__ == '__main__':
    filename = './file01.txt'
    with open(filename, 'w') as file_object:
        for i in range(100):
            data = random.randint(0, 1)
            print("I:", i, data)
            file_object.write(str(data)+"\n")

    filename = './loss.txt'
    with open(filename, 'w') as file_object:
        for i in range(1024 * 10):
            data = random.random()
            file_object.write(str(data) + "\n")