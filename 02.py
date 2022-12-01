f = open("01\input.txt", "r")
tCalories = []
sumCalories  = 0
for line in f:
    if(line != "\n"):
        sumCalories += int(line)
    else:
        tCalories.append(sumCalories)
        sumCalories = 0
f.close()
tCalories.sort(reverse=True)
sumCalories = tCalories[0] + tCalories[1] + tCalories [2]
print(sumCalories)
