# class Car:
#     def __init__(self, max_speed, doors, colour, horse_power):
#         self.max_speed = max_speed
#         self.doors = doors
#         self.colour = colour
#         self.horse_power = horse_power
#
#
# class SportCar(Car):
#     pass
#
# class OldCar(Car):
#     pass
# A = Car("300 km/h" ,"4 doors", "black", "540 H.P")
# B = SportCar("450 km/h" ,"2 doors", "red", "920 H.P")
# C = OldCar("180 km/h" ,"4 doors", "blue", "80 H.P")
# print(A.max_speed, A.doors, A.colour, A.horse_power)
# print(B.max_speed, B.doors, B.colour, B.horse_power)
# print(C.max_speed, C.doors, C.colour, C.horse_power)

class MyClass1:
    def __init__(self, filename):
        self.my_class = open(filename, 'w')
        self.my_class_name = filename

    def add(self, fname, lname):
        self.my_class.write(fname + " " + lname + '\n')

    def delete(self, fname, lname):
        self.my_class = open(self.my_class_name, 'r')
        lines = self.my_class.readlines()
        self.my_class.close()
        self.my_class = open(self.my_class_name, 'w')
        for line in lines:
            if line != f"{fname} {lname}" + "\n": self.my_class.write(line)
        self.my_class.close()

    def lines(self):
        self.my_class = open(self.my_class_name, 'r')
        lines = self.my_class.readlines()
        print(len(lines))
    def read(self):
        self.my_class = open(self.my_class_name, 'r')
        read = self.my_class.readlines()
        print(read)

class MyClass2(MyClass1):
    pass
class MyClass3(MyClass1):
    pass
class MyClass4(MyClass1):
    pass

print("Добро пожаловать в интерактивный журнал!"


A1 = MyClass1('class1.txt')
A1.add("Ruslan","Sharipov ")
A1.add("Yusuf", "Zayniev")
# A1.delete("Yusuf", "Zayniev")
# A1.lines()
A1.read()

A2 = MyClass1('class2.txt')
A2.add("Ruslan","Pepsi ")
A2.add("Yusuf", "Cola")
# A2.delete("Yusuf", "Zayniev")
# A2.lines()
A2.read()

A3 = MyClass1('class3.txt')
A3.add("Lionel","Pepsi ")
A3.add("Neymar", "Junior ")
# A3.delete()
# A3.lines()
A3.read()

A4 = MyClass1('class4.txt')
A4.add("Ruslan","Zayniev")
A4.add("Yusuf", "Sharipov")
# A4.delete("Yusuf", "Zayniev")
# A4.lines()
A4.read()


