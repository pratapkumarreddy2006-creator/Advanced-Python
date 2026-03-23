class Book:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "removed")