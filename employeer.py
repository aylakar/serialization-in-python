from json import JSONEncoder

class Employeer:
    def __init__(self, name, age, office) -> None:
        self.name = name
        self.age = age
        self.office = office

class EmployeerJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__