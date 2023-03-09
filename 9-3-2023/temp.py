class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name: str = name
        self.surname: str = surname

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def fullName(self):
        return f"{self.name} {self.surname}"

    def __str__(self) -> str:
        return self.fullName()

    def __eq__(self, __o: any) -> bool:
        return self.getName() == __o.getName() and self.getSurname() == __o.getSurname()
