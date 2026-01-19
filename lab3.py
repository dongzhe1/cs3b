
"""
What is Polymorphism?
Inheritance defines a relationship that a subclass is derived from a parent class.
By default, the subclass inherits the behaviors (methods) of the parent class.
Polymorphism allows the subclass behaves differently from the parent class by overriding the methods.
A reference of the parent type might point to either a parent instance or a child instance.
Polymorphism ensures the specific functions being processed when the same method is called depending on the instances.
"""

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self, sales_amount = 0):
        """calculate_pay is defined in parent class"""
        return self.base_salary


class SalesPerson(Employee):
    def __init__(self, name, base_salary, commission_rate):
        super().__init__(name, base_salary)
        self.commission_rate = commission_rate

    def calculate_pay(self, sales_amount = 0):
        """Polymorphism occurs here. If we don't override, sales will get only base_salary (same behavior with non-sales employee)"""
        commission = sales_amount * self.commission_rate
        return self.base_salary + commission


if __name__ == "__main__":
    # --- Polymorphism Demonstration ---
    # employee Bob
    bob = Employee("Bob", 5000)
    # sales Alice
    alice = SalesPerson("Alice", 3000, 0.10)

    company_staff = [alice, bob]
    print("--- Payroll Report ---")
    for staff in company_staff:
        # make sure all instances are of Employee
        if not isinstance(staff, Employee):
            print(f"{staff} is not an employee, skip")
            continue
        pay = staff.calculate_pay(sales_amount=50000)
        print(f"{staff.name} ({type(staff).__name__}): ${pay:.2f}")
