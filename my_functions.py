def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name

name_1 = "David"
time_of_day_1 = "afternoon"

greeting = greet(name_1, time_of_day_1)
print(greeting)

name_2 = "Kyle"
time_of_day_2 = "evening"

greeting = greet(name_2, time_of_day_2)
print(greeting)

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

chickens_2 = [
  { "name": "Davinia", "age": 4, "eggs": 3 },
  { "name": "Kylie", "age": 2, "eggs": 6 },
  { "name": "Jo", "age": 2, "eggs": 2 },
  { "name": "Rose", "age": 3, "eggs": 0 },
  { "name": "Agnes", "age": 5, "eggs": 2 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))
print(count_eggs(chickens_2))
for chicken in chickens_2:
    print(chicken["name"])