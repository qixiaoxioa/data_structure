class Student:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def study(self):
        print('%s在学习'%(self.name))
p = Student('zs','女','18')
p.study()