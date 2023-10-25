class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью ручки {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью карандаша {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью маркера {self.title}")

# Создаем экземпляры классов и вызываем метод draw()

pen = Pen("голубая")
pen.draw()

pencil = Pencil("черный")
pencil.draw()

handle = Handle("оранжевый")
handle.draw()