class Person:
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name

    def __str__(self):
        return f"<Person: {self.first_name} {self.family_name}>"

    def say(self, to_whom, something):
        return f"{self.first_name} {self.family_name} says to {to_whom.first_name} {to_whom.family_name}: {something}"

    def sing(self, to_whom, something):
        return self.say(to_whom, f"{something} tra la la")


class MitPerson(Person):
    id_num: int
    next_id_num = 0

    def __init__(self, family_name, first_name):
        super().__init__(family_name, first_name)
        self.id_num = MitPerson.next_id_num
        MitPerson.next_id_num += 1

    def get_id_num(self):
        return self.id_num

    def __str__(self):
        return "<MITPerson: %s %s>" % (self.first_name, self.family_name)


m1 = MitPerson("smith", "Fred")
p1 = Person("foobar", "Jane")
m2 = MitPerson("william", "King")
m3 = MitPerson("stupid", "Fool")
print(m1.get_id_num())
print(m2.get_id_num())
print(m3.get_id_num())
print(m1.sing(m2, "what do you want?"))
