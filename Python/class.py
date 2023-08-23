# import datetime


# class details:
#     def __init__(self, name, age, company) -> None:
#         self.name = name
#         self.age = age
#         self.company = company

#     def officestart(self):
#         print('Office starts at 11 A.M.')

#     def officeend(self):
#         print('Office Ends at 8:15 P.M.')


# class clgdetails(details):
#     name = 'Prabhakaran Vettum Perumal'
#     poy = 2023
#     Course = 'Bscit'


# class bankdetails(clgdetails):
#     name = 'Prabhakaran Vettum Perumal'
#     AC = 232132132132132132
#     IFSC = 'ha3j4j2j31'


# class homeadd(bankdetails):
#     chawl = 'Palkar chawl'
#     street = '90 Feet'
#     Loc = "Dharavi"

#     def area(self):
#         print('I live in Dharavi')


# idata = homeadd('Prabhakaran', 21, 'OSP Labs')
# print('My name is', idata.name)
# print('My age is', idata.age)
# print('I workd at', idata.company)
# print('My name in my clg details is', idata.name)
# print('I passed out in the year', idata.poy)
# print("I have completed my degree of", idata.Course)
# print('Account holder name is', idata.name)
# print('My ac no. is', idata.AC)
# print('IFSC code is', idata.IFSC)
# print('My chawl name is', idata.chawl)
# print('The street where i live is', idata.street)
# print('the location of my street is', idata.Loc)
# idata.area()
# idata.officestart()
# idata.officeend()
# print(datetime.datetime.now())


# super
class Animal(object):
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)


class Mammal(Animal):
    def __init__(self):
        super().__init__('Lion')
        print('Mammals give birth directly')


dog = Mammal()
