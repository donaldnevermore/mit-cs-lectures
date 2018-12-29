class Person:
    """面向对象编程"""

    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name

    def __str__(self):
        return '<Person: %s %s>' % (self.first_name, self.family_name)

    def say(self, to_whom, something):
        return self.first_name + ' ' + self.family_name + ' says to ' + to_whom.first_name + ' ' + \
               to_whom.family_name + ': ' + something

    def sing(self, to_whom, something):
        return self.say(to_whom, something + ' tra la la')


class MITPerson(Person):
    id_num: int
    next_id_num = 0

    def __init__(self, family_name, first_name):
        super().__init__(family_name, first_name)
        self.id_num = MITPerson.next_id_num
        MITPerson.next_id_num += 1

    def get_id_num(self):
        return self.id_num

    def __str__(self):
        return '<MITPerson: %s %s>' % (self.first_name, self.family_name)


m1 = MITPerson('smith', 'Fred')
p1 = Person('foobar', 'Jane')
m2 = MITPerson('william', 'King')
m3 = MITPerson('stupid', 'Fool')
print(m1.get_id_num())
print(m2.get_id_num())
print(m3.get_id_num())
print(m1.sing(m2, 'what do you want?'))
