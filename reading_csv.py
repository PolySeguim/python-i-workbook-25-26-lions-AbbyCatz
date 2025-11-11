import tkinter as tk
from tkinter import filedialog
import csv

def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def read_file(file_path):
    if file_path:
        with open(file_path, mode="r", newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    else:
        print("No file selected")
        
file_path = choose_file()
read_file(file_path)