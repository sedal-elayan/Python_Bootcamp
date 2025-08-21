fruit = ["Berry", "Strawberry", "Melon", "Peach", "Grape"]
print("Fruits list:", fruit)
print("First fruit:", fruit[0])
print("Last fruit:", fruit[-1])
fruit[1] = "Mango"
print("After changing second :", fruit)
fruit.insert(2, "Watermelon")
print("After inserting Watermelon:", fruit)
infruit = input("Enter a fruit to check: ")
if infruit in fruit:
    print(f"{infruit} is in the list!")
else:
    print(f"{infruit} is not in the list.")
fruit.sort()
print("Sorted fruit:", fruit)
