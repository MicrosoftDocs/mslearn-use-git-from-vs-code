from datetime import date


print('Hello, World!')
print("show this in the console")
sum = 1 + 2 # 3
product = sum * 2
print("The value of product is " + str(product))
print(product)


# slide Data Types
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

type(distance_to_alpha_centauri) ## <class 'float'>
print(type(distance_to_alpha_centauri)) ## <class 'float'>


date.today()
print(date.today())
print("Today's date is: " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears" )


