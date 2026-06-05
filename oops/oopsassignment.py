class Students:

    def __init__(self, name, age, email, phonenumber):
        self.name = name
        self.age = age
        self.email = email
        self.phonenumber = phonenumber

    def display_details(self):
        print(self.name)
        print(self.age)
        print(self.email)
        print(self.phonenumber)


class class10admission(Students):

    def __init__(self, name, age, email, phonenumber):
        super().__init__(name, age, email, phonenumber)

        print('Admission Successful')


class class12addmission(Students):

    def __init__(self, name, age, email, phonenumber):
        super().__init__(name, age, email, phonenumber)

        if self.age >= 16:
            print('Admission Successful')
        else:
            print('Admission Failed')


print('Press 1 for class 10th admission')
print('Press 2 for class 12th admission')

choice = int(input('Enter your choice :- '))

name = input('Tell your name :- ')
age = int(input('Tell your age :- '))
email = input('Tell your email :- ')
phonenumber = int(input('Tell your number :- '))


if choice == 1:
    student1 = class10admission(name, age, email, phonenumber)
    student1.display_details()

elif choice == 2:
    student1 = class12addmission(name, age, email, phonenumber)
    student1.display_details()

else:
    print('Invalid Choice')
