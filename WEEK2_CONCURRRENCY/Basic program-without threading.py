class Hello:
    def __init__(self, num):
        self.num = int(num)

    def run(self):
        for i in range(self.num):
            print("Hello")

class Hi:
    def __init__(self, num):
        self.num = int(num)

    def run(self):
        for i in range(self.num):
            print("Hi")


def main():
    num = input("Enter a number: ")

    #create objcects
    obj1 = Hello(num)
    obj2 = Hi(num)

    obj1.run()
    obj2.run()

main()


