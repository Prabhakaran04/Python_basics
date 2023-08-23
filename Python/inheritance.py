class Employe():
    def __init__(self, name, role):
        self.name = name
        self.role = role
        print(self.name, 'is in the role of', self.role)

    def Status_now(self):
        print('Currently working as an employee')


class Student(Employe):
    def __init__(self, school_name, loc):
        self.school_name = school_name
        self.loc = loc
        super().__init__('Prabhakaran', 'Python Developer')
        print('Completed studies from', self.school_name, 'in', self.loc)

    def Status_then(self):
        print('Have completed schooling')


idata = Student('PWS', 'Sion')
idata.Status_now()
idata.Status_then()
