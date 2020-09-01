# my_number = 5

# value  = float(input("What numbner am I thinking of? "))

# while(value != my_number):
#     if(type(value) != float):
#         print("Wrong type")
#         break
#     if(value > my_number):
#         print("Too high!")
#     else:
#         print("Too low!")
#     value = float(input("Nope! Try again... "))

# if( (type(value) == float) and (value == my_number)):
#     print("Yes!")

# while(True):
#     line = input("Type something: ")
#     if(line.lower() =="q"):
#         break
#     print(f"You typed: {line}")

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number * 3)

# chickens = ["Margaret", "Hetty", "Henrietta", "Audrey", "Mabel"]

# for chicken in chickens:
#     print(chicken)

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

for chicken in chickens:
    print(f'{chicken["name"]} is {chicken["age"]}')

for chicken in chickens:
    if chicken["eggs"] > 0:
        print("Woo! Eggs")

total_eggs = 0

for chicken in chickens:
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0

print(f"{total_eggs} eggs collected")


