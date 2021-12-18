# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"] 
x = cars[0] 
y = len(cars) 
print(cars,x)
print(y)

cars.append("Honda")

cars.pop(1) # removes volvo
for x in cars:
  print(x) 