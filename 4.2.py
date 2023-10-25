import string


class Alphabet:
    def __init__(self, lang, letters): #lang - язык, letters - список букв
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f"Алфавит {self.lang}:")
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26  # __ - private

    def __init__(self):
        super().__init__('En', string.ascii_uppercase) # переопределение конструктора

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."


alphabet = Alphabet("Русский", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
alphabet.print()
print(f"Количество букв в алфавите: {alphabet.letters_num()}")

eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(f"Количество букв в алфавите: {eng_alphabet.letters_num()}")
print(f"'A' - это буква английского алфавита? {eng_alphabet.is_en_letter('A')}")
print(f"'Я' - это буква английского алфавита? {eng_alphabet.is_en_letter('Я')}")

print(EngAlphabet.example())
