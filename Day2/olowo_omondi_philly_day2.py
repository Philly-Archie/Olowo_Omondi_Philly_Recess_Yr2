# Morning Session 

# Control Statements
age = 20

if age <13:
    print("Minor's movie Discount is Shs 1000")

elif age > 13 and age < 18:
    print("Teenager movie discount is Shs 500")

elif age > 18 and age <65:
    print("Adults pay price of Shs 2000")

else:
    print("Senior adults pay of Shs 5000")


# Loops

favorite_colors = ["Yellow", "Blue", "Red", "Green"]

for color in favorite_colors:
    print(color)

x = 10
while x > 1:
    print(f"x is: {x}")
    x -= 1

