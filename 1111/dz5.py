class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name
    def display_greeting(self):
        print(f"Hello! I am {self.name}, one of the best programming languages!")
    def printing(self):
        print(f"Я вітаюся через:")
class Python(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Python")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")
class Java(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Java")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")
class CPlusPlus(ProgrammingLanguage):
    def __init__(self):
        super().__init__("C++")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")
if __name__ == "__main__":
    python = Python()
    java = Java()
    cpp = CPlusPlus()

    python.display_greeting()
    python.hello_world()
    java.display_greeting()
    cpp.display_greeting()