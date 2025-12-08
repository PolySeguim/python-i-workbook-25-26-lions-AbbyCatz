import tkinter as tk
from tkinter import filedialog
import csv
import statistics

# Define the lists to store data
restaurants = []
items = []
types = []
serving_sizes = []
calories = []
fats = []
sodiums = []
sugars = []


list_data = []
unique_restaurants = set()

# Read the CSV file and store the data into lists

def choose_file():
    root = tk.Tk()
    root.withdraw()  #Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    #print(file_path)
    return file_path


def read_csv(file_name):
    with open(file_name, newline='', mode='r', encoding='utf=8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            restaurants.append(row['restaurant'])
            items.append(row['item'])
            types.append(row['type'])
            serving_sizes.append(float(row['serving_size']))
            calories.append(int(row['calories']))
            fats.append(float(row['fat']))
            sodiums.append(float(row['sodium']))
            sugars.append(float(row['sugars']))
            
            list_data.append(row)
            unique_restaurants.add(row['restaurant'])
            
            
# Count how many items have a certain calorie value
def filter_calories_count_over(calorie_value):
    count = 0
    for calorie in calories:
        if(calorie >= calorie_value):
            count += 1
    return count

    # Count how many items have a certain calorie value
def filter_calories_count_under(calorie_value):
    count = 0
    for calorie in calories:
        if(calorie < calorie_value):
            count += 1
    return count
            
            
def calculateAverages(list_of_values):
    average = sum(list_of_values)/len(list_of_values)
    return average


def countItems(list_of_values):
    return len(list_of_values)


def max_value(list_of_values):
    return max(list_of_values)
    
    
def min_value(list_of_values):
    return min(list_of_values)


def sugars_per_restaurant(sugars, restaurant_name):
    sugars_per = []
    for i in range(len(restaurants)):
        if(restaurants[i] == restaurant_name):
            sugars_per.append(sugars[i])          
    return sum(sugars_per)


# Finds the sum of sugars per restaurant
def restaurants_sugars_report():
    report = {} # dictionary to hold restaurant:sugar total pairs
    for restaurant in unique_restaurants:
        total_sugars = 0
        for i in range(len(restaurants)):
            if restaurants[i] == restaurant:
                total_sugars += sugars[i]
        report[restaurant] = total_sugars       
        
    return report

# Finds the sum of sugars per restaurant
def restaurants_calories_report():
    report = {}
    for restaurant in unique_restaurants:
        total_calories = 0
        for i in range(len(restaurants)):
            if restaurants[i] == restaurant:
                total_calories += calories[i]
        report[restaurant] = total_calories       
        
    return report

def calculateMean(list_of_values):
    return statistics.mean(list_of_values)

def calc_st_dev(list_of_values):
    return statistics.stdev(list_of_values)

def zscores(list_of_values):
    zScores = []
    mean = calculateMean(list_of_values)
    st_dev = calc_st_dev(list_of_values)
    
    for i in list_of_values:
        z_score = (i - mean)/st_dev
        zScores.append(z_score)
        
        return zScores


def main():
    file_path = choose_file()
    read_csv(file_path)


    average_calories = calculateAverages(calories)
    print("Average calories ", average_calories)


    count_calories = countItems(calories)
    print("Calorie count is ", count_calories)


    max_calories = max_value(calories)
    print("Max Calorie value: ", max_calories)
    

    min_calories = min_value(calories)
    print("Min Calorie value: ", min_calories)
    
    
    # Count how many items have a certain calorie value
    calorie_value = 500
    print("Number of items over or equal to ", calorie_value, " calories are ", filter_calories_count_over(calorie_value))
    print("Number of items under ", calorie_value, " calories are ", filter_calories_count_under(calorie_value))

    print("Sugars for Burger King: " , sugars_per_restaurant(sugars, "Burger King"))
    
    
    
    print("\nList of restaurants and their total sugars :\n")
    report = restaurants_sugars_report()
    for result in report:
        print(result, ": ", report[result])
    print("\n")
    
    print("List of restaurants and their total calories:\n")
    report = restaurants_calories_report()
    for result in report:
        print(result, ": ", report[result])


if __name__ == '__main__':
    main()