class Employee:
    def __init__(self, ID, salary, deparment):
        self.ID = ID
        self.salary = salary
        self.deparment = deparment

Alej = Employee(1019082943,1200000,"CCE")

print("El ID es:", Alej.ID)
print("El salario es:", Alej.salary)
print("El departamento es", Alej.deparment)
