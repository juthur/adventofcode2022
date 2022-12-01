f = open("01\input.txt", "r")
maxCalories = 0
sumCalories  = 0
for line in f:
    if(line != "\n"):
        sumCalories += int(line)
    else:
        if(sumCalories >= maxCalories):
            maxCalories = sumCalories
        sumCalories = 0
f.close()
print(maxCalories)
