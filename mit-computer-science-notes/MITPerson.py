# 面向对象
class Person(object):
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name

    def familyName(self):
        return self.family_name

    def firstName(self):
        return self.first_name

    def __str__(self):
        return '<Person: %s %s>' % (self.first_name, self.family_name)

    def say(self, toWhom, something):
        return self.first_name + ' ' + self.family_name + ' says to ' + toWhom.firstName() + ' ' + toWhom.familyName() + ': ' + something

    def sing(self, toWhom, something):
        return self.say(toWhom, something + ' tra la la')


class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, familyName, firstName):
        Person.__init__(self, familyName, firstName)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __str__(self):
        return '<MITPerson: %s %s>' % (self.first_name, self.family_name)


# m1 = MITPerson('smith', 'Fred')
# p1 = Person('foobar', 'Jane')
# m2 = MITPerson('wiliam', 'King')
# m3 = MITPerson('stupid', 'Fool')
# print(m1.getIdNum())
# print(m2.getIdNum())
# print(m3.getIdNum())
# print(m1.sing(m2,'what do you want?'))


