import tkinter as tk
from tkinter import font


def create_gui():
    window = tk.Tk()
    window.title("Library Management System")
    window.geometry("400x240")

    # Define custom fonts
    title_font = font.Font(family="Arial", size=16, weight="bold")
    label_font = font.Font(family="Arial", size=12)

    # Create title label
    title_label = tk.Label(window, text="Library Management System", font=title_font)
    title_label.pack(pady=10)

    # Create student details section
    student_frame = tk.Frame(window)
    student_frame.pack(pady=5)

    student_label = tk.Label(student_frame, text="Student Details", font=label_font)
    student_label.pack(side=tk.LEFT)

    name_label = tk.Label(student_frame, text="Name: XYZ", font=label_font)
    name_label.pack(anchor="w")

    prn_label = tk.Label(student_frame, text="PRN Number: 2122000145", font=label_font)
    prn_label.pack(anchor="w")

    address_label = tk.Label(student_frame, text="Address: AB Colony, Aurangabad", font=label_font)
    address_label.pack(anchor="w")

    phone_label = tk.Label(student_frame, text="Phone Number: 9021000142", font=label_font)
    phone_label.pack(anchor="w")

    # Create book details section
    book_frame = tk.Frame(window)
    book_frame.pack(pady=5)

    book_label = tk.Label(book_frame, text="Book Details", font=label_font)
    book_label.pack(side=tk.LEFT)

    book_taken_label = tk.Label(book_frame, text="Book Taken: Book_name", font=label_font)
    book_taken_label.pack(anchor="w")

    renewal_date_label = tk.Label(book_frame, text="Renewal Date: 17/02/2023", font=label_font)
    renewal_date_label.pack(anchor="w")

    window.mainloop()


create_gui()
