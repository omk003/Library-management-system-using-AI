import tkinter as tk
from tkinter import font
import csv
import sys

person_name = sys.argv[1]

Name = ''
PRN = ''
ADD = ''
NO = ''
Book = ''
Date = ''


def read_csv_file(file_name, name1):
    with open(file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == name1:
                return row
    return None


row1 = read_csv_file('data.csv', person_name)


def create_gui(row: list):
    if row is None:
        row = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]  # Default values if data is missing

    def exit_program(event=None):
        window.destroy()

    window = tk.Tk()
    window.title("Library Management system")
    window.geometry("400x240")
    window.bind('<q>', exit_program)  # Bind 'q' key press event to exit_program function

    custom_font = font.Font(family="Arial", size=12, weight="bold")

    student_label = tk.Label(window, text="Student Details", justify="center", font=custom_font)
    student_label.pack(anchor="center")

    name_label = tk.Label(window, text=f"Name: {row[0]}", justify="left")
    name_label.pack(anchor="w")

    prn_label = tk.Label(window, text=f"PRN Number: {row[1]}", justify="left")
    prn_label.pack(anchor="w")

    address_label = tk.Label(window, text=f"Address: {row[2]}", justify="left")
    address_label.pack(anchor="w")

    phone_label = tk.Label(window, text=f"Phone Number: {row[3]}", justify="left")
    phone_label.pack(anchor="w")

    book_label = tk.Label(window, text="Book Details", justify="left")
    book_label.pack(anchor="w")

    book_taken_label = tk.Label(window, text=f"Book Taken: {row[4]}", justify="left")
    book_taken_label.pack(anchor="w")

    renewal_date_label = tk.Label(window, text=f"Renewal Date: {row[5]}", justify="left")
    renewal_date_label.pack(anchor="w")

    window.mainloop()


create_gui(row1)
