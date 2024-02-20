name = "mario"
health = 16
maxhealth = 20
healthDisplay = ""
print("hello i am " + name)
for i in range(maxhealth):
    if i < health:
        healthDisplay += "♥"
    else:
        healthDisplay += "♡"
print("Health: " + str(health) + " " + healthDisplay)

