#Grocery List App with Categories
import math

#Lists
groceryCart = []
toiletry = []
fruitAndVeg = []
meat = []
grain = []
dessert = []
noAlcBev = []
alcBev = []
snack = []
dairyProduct = []
partPrepFood = []
cleaningSupply = []

#Prints out all items and the number with them
def printOut():
    #Toiletry List
    print("Toiletries: \n 1 = Toilet Paper \n 2 = Soap \n 3 = Shampoo \n 4 = Conditioner \n 5 = Lotion \n 6 = Tissues \n 7 = Paper Towels")
    print(" 8 = Toothbrush \n 9 = Toothpaste \n 10 = Deodorant \n 11 = Diapers \n 12 = Face Wash \n")
    
    #Fruits and Veggies List
    print("Fruits and Veggies: \n 13 = Apples \n 14 = Oranges \n 15 = Bananas \n 16 = Strawberries \n 17 = Blueberies \n 18 = Grapes") 
    print(" 19 = Raspberries \n 20 = Tomatoes \n 21 = Lettuce \n 22 = Pickles \n 23 = Cucumbers \n 24 = Peppers \n 25 = Carrots \n 26 = Asparagus \n")
   
    #Meat List
    print("Meats: \n 27 = Lamb Chops \n 28 = Ham \n 29 = Bacon \n 30 = Steak \n 31 = Beef \n 32 = Chicken \n 33 = Turkey \n")

    #Grain List
    print("Grains: \n 34 = Rice \n 35 = Pasta \n 36 = Ramen \n 37 = Bread \n 38 = Cereal \n 39 = Oatmeal \n 40 = Popcorn \n")

    #Dessert List
    print("Desserts: \n 41 = Ice Cream \n 42 = Cake \n 43 = Popsicles \n 44 = Cupcakes \n 45 = Cookies \n 46 = Brownies \n 47 = Ice Cream Cake \n")

    #Non-Alcoholic Beverage List
    print("Non-Alcoholic Beverages: \n 48 = Apple Juice \n 49 = Orange Juice \n 50 = Fruit Punch \n 51 = Sprite \n 52 = Fanta \n 53 = Coke \n 54 = Diet Coke")
    print(" 55 = Root Beer \n 56 = Dr. Pepper \n 57 = Mountain Dew \n 58 = Water \n 59 = Milk \n 60 = Gatorade \n")

    #Alcoholic Beverage List
    print("Alcohol Beverages: \n 61 = Vodka \n 62 = Bourban \n 63 = Beer \n 64 = Wine \n 65 = Gin \n 66 = Brandy \n 67 = Tequila \n 68 = Rum \n")

    #Snacks List
    print("Snacks: \n 69 = Chocolates \n 70 = Chips \n 71 = Crackers \n 72 = Fruit Snacks \n 73 = Gummies \n")

    #Dairy Products List
    print("Dairy Products: \n 74 = Shredded Cheese \n 75 = Yogurt \n 76 = Cheese Sticks \n 77 = Coffee Cream \n 78 = Cream Cheese")
    print(" 79 = Butter \n 80 = Sliced Cheese \n")

    #Pre-Prepped Food List
    print("Pre-Prepped Dishes: \n 81 = Cookie Dough \n 82 = Cake Mix \n 83 = Frozen Pizza \n 84 = Frozen Meals \n 85 = Brownie Mix")
    print(" 86 = Microwaveable Ramen \n 87 = Microwavable Rice \n 88 = Pancake Mix \n 89 = Lunchables \n")

    #Cleaning Supplies
    print("Cleaning Supplies: \n 90 = Laundry Detergent \n 91 = Dish Detergent \n 92 = Window Cleaner \n 93 = Wood Cleaner \n 94 = Metal Shiner")
    print(" 95 = Glass Cleaner \n 96 = Clorox \n 97 = Swiffer \n 98 = Mop \n 99 = Baby Wipes \n 100 = Trash Bags")
printOut()

def fill_cart(item):
    #Putting them in categories
    if item <= 0:
        print(item, "is not a valid input")
        exit     
    elif item <= 12:
        toiletry.append(item)
    elif item <= 26:
        fruitAndVeg.append(item)
    elif item <= 33:
        meat.append(item)
    elif item <= 40:
        grain.append(item)
    elif item <= 47:
        dessert.append(item)
    elif item <= 60:
        noAlcBev.append(item)
    elif item <= 68:
        alcBev.append(item)
    elif item <= 73:
        snack.append(item)
    elif item <= 80:
        dairyProduct.append(item)
    elif item <= 87:
        partPrepFood.append(item)
    elif item <= 100:
        cleaningSupply.append(item)
    else:
        print(item, "is not a valid input")

    groceryCart.append(item)
        
def start():
    items = int(input("How many items do you want? "))
    if items >= 0:
        for i in range(items):
            item = int(input("What item do you want? "))
            fill_cart(item)
        else:
            (items, "is an invalid input") 
        
    print("Your grocery cart contains: ")
    print("All items: ", groceryCart)
    print("Toiletries - Aisle 1: ", toiletry)
    print("Fruits and vegetables - Aisle 2: ", fruitAndVeg)
    print("Meats - Aisle 3: ", meat)
    print("Grains - Aisle 4: ", grain)
    print("Desserts - Aisle 5: ", dessert)
    print("Non-Alcoholic Beverages - Aisle 6: ", noAlcBev)
    print("Alcoholic Beverages - Aisle 7: ", alcBev)
    print("Snacks - Aisle 8: ", snack)
    print("Dairy Products - Aisle 9: ", dairyProduct)
    print("Pre-Prepped Dishes - Aisle 10: ",  partPrepFood)
    print("Cleaning Supplies - Aisle 11: ", cleaningSupply)

start()       

#Tells user to show ID if they order alcohol
def alcohol():
    if(len(alcBev) >= 1):
        print(" \nYou need to show ID")
alcohol()

