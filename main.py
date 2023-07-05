import json
from employeer import Employeer, EmployeerJSONEncoder

# intance python objects

emp1 = Employeer(name="Ayla", age=20, office="Estag")
emp2 = Employeer(name="Pedro", age=22, office="Estag")

# create list with employees
emp_list = [emp1, emp2]

# serialize
serializer = json.dumps(emp_list, cls=EmployeerJSONEncoder) # Re: [{"name": "Ayla", "age": 20, "office": "Estag"}, {"name": "Pedro", "age": 22, "office": "Estag"}]

# deserialize
deserializer = json.loads(serializer)

#! all its ok with the serialize, but not how i want
#! I want that return was object list, how the fisrt version
#! with the help of the chatgpt i can fix this
#! We iterate over the list and create the "employeer" class

employeers = []

for item in deserializer:
    employeer = Employeer(**item)
    employeers.append(employeer)

# When debug code we have:
# employeers -> [<employeer.Employeer...28CA0E1D0>, <employeer.Employeer...28CA0E1A0>] back to first version
# employeers[0].name -> 'Ayla' We got the result we wanted







