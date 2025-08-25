# تخزين أسعار الفواكه في dictionary
fruit_prices = {
    "Strawberry": 3.5,
    "Blueberry": 4.0,
    "Mango": 2.8,
    "Peach": 2.2,
    "Watermelon": 1.5,
    "Pineapple": 3.0,
    "Cherry": 5.0,
    "Kiwi": 2.7,
    "Orange": 1.8,
    "Banana": 1.2,
    "Apple": 2.3,
    "Grapes": 2.6
}

fruit = input("Enter the fruit name: ")

if fruit in fruit_prices:
    print(f"The price of {fruit} is ${fruit_prices[fruit]}")
else:
    print("Sorry, this fruit is not available.")
