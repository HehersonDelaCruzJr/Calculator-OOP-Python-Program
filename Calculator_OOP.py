class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


calculator = Calculator(0, 0)

selector = 1
while selector != 0:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    selector = float(input("Enter your choice: "))

    if selector == 1:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        calculator.num1 = num1
        calculator.num2 = num2
        print("Result: ", calculator.addition())

    elif selector == 2:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        calculator.num1 = num1
        calculator.num2 = num2
        print("Result: ", calculator.subtraction())

    elif selector == 3:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        calculator.num1 = num1
        calculator.num2 = num2
        print("Result: ", calculator.multiplication())

    elif selector == 4:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        calculator.num1 = num1
        calculator.num2 = num2
        print("Result: ", calculator.division())

    elif selector == 5:
        print("Exit")
        break

    else:
        print("Invalid choice!")

    print()
    print("=========================================")
    print()

print("Exiting!")

