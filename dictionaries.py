# meals = ['yoghurt', 'roll', 'steak']

# meals_dict = {'breakfast' : 'yoghurt', 'lunch' : 'roll', 'dinner' : 'steak'}

# my_first_empty_dict = {}
# my_second_empty_dict = dict()

# meals = {'breakfast': 'yoghurt', 'lunch': 'roll', 'dinner': 'steak'}
# print(meals)

# silly_things = {1: "2", 2: "3", 4:False}
# print(meals['breakfast'])

# meals['dinner'] = "pasta"
# print(meals)

# del(meals['breakfast'])
# print(meals)

# meals['Elevenses'] = 'Cake'
# print(meals)

# print(list(meals))

# print(meals.keys())
# print(meals.values())

countries = {
    'uk': {
        'capital': 'London', 'popu;ation': 1000
    },
    'germany': {
        'capital': 'Berlin', 'population': 5
    }
}
print(countries)

print(countries['germany']['population'])

avengers = {
    'Iron Man': {
        'name': 'Tony Stark', 
        'moves': {
            'punch': 10, 
            'kick': 100
        }
    }, 'Hulk': {
        'name': 'Bruce Banner', 
        'moves': {
            'smash': 1000, 
            'roll': 500
        }
    }
}
print(avengers['Hulk']['moves']['smash'])