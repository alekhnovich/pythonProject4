class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self, num1, num2):
        return num1 + num2

    def minus(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2


def input_data():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1, num2


math_ops = Calculator(4, 4)
choice = int(input(
    "Меню:\n"
    "1. +\n"
    "2. -\n"
    "3. *\n"
    "4. /\n"
    "5. Завершить работу\n"
    "Ваш выбор: "))
print("------------------")
while True:
    if choice == 1:
        result = math_ops.plus(4,4)
        print(f"Результат сложения: {result}")
        choice = int(input("Ваш выбор: "))
        print("------------------")
    elif choice == 2:
        result = math_ops.minus(4,4)
        print(f"Результат вычитания: {result}")
        choice = int(input("Ваш выбор: "))
        print("------------------")
    elif choice == 3:
        result = math_ops.multiply(4,4)
        print(f"Результат умножения: {result}")
        choice = int(input("Ваш выбор: "))
        print("------------------")
    elif choice == 4:
        result = math_ops.divide(4,4)
        print(f"Результат деления: {result}")
        choice = int(input("Ваш выбор: "))
        print("------------------")
    elif choice == 5:
        print("До свидания!")
        break
    else:
        print("неверное значение")
        choice = int(input("Ваш выбор: "))
