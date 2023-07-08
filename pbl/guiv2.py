import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import subprocess

person_name = sys.argv[1]


def read_csv_file(file_name, name1):
    with open(file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == name1:
                return row
    return None


# function for updating barcode
def update_csv_file(file_name, name, barcode):
    rows = []
    found = False

    # Read the CSV file and search for the name
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == name:
                row[7] = barcode  # Update the barcode in the row
                found = True
            rows.append(row)

    if not found:
        print(f"Name '{name}' not found in the CSV file.")
        return

    # Write the updated data back to the CSV file
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)


row1 = read_csv_file('data.csv', person_name)


class LibraryManagementSystem(QMainWindow):
    def __init__(self, row):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.setGeometry(200, 200, 600, 400)

        self.label_font = QFont("Arial", 16, QFont.Bold)
        self.name_font = QFont("Arial", 11)

        self.create_gui(row)

    def create_gui(self, row):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        student_label = QLabel("Student Details")
        student_label.setFont(self.label_font)

        student_details = QVBoxLayout()
        student_details.addWidget(student_label)

        name_label = QLabel(f"Name: {row[0]}")
        name_label.setAlignment(Qt.AlignLeft)
        name_label.setFont(self.name_font)
        student_details.addWidget(name_label)

        prn_label = QLabel(f"PRN Number: {row[1]}")
        prn_label.setAlignment(Qt.AlignLeft)
        prn_label.setFont(self.name_font)
        student_details.addWidget(prn_label)

        address_label = QLabel(f"Address: {row[2]}")
        address_label.setAlignment(Qt.AlignLeft)
        address_label.setFont(self.name_font)
        student_details.addWidget(address_label)

        phone_label = QLabel(f"Phone Number: {row[3]}")
        phone_label.setAlignment(Qt.AlignLeft)
        phone_label.setFont(self.name_font)
        student_details.addWidget(phone_label)

        book_label = QLabel("Book Details")
        book_label.setFont(self.label_font)
        student_details.addWidget(book_label)

        book_taken_label = QLabel(f"Book Taken: {row[4]}")
        book_taken_label.setAlignment(Qt.AlignLeft)
        book_taken_label.setFont(self.name_font)
        student_details.addWidget(book_taken_label)

        renewal_date_label = QLabel(f"Issued Date: {row[5]}")
        renewal_date_label.setAlignment(Qt.AlignLeft)
        renewal_date_label.setFont(self.name_font)
        student_details.addWidget(renewal_date_label)

        renewal_date_label = QLabel(f"Renewal Date: {row[6]}")
        renewal_date_label.setAlignment(Qt.AlignLeft)
        renewal_date_label.setFont(self.name_font)
        student_details.addWidget(renewal_date_label)

        main_layout.addLayout(student_details)

        enter_button = QPushButton("Enter")
        enter_button.clicked.connect(self.enter_button_clicked)
        main_layout.addWidget(enter_button)

        scan_button = QPushButton("Scan a book")
        scan_button.clicked.connect(self.scan_button_clicked)
        main_layout.addWidget(scan_button)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def enter_button_clicked(self):
        # Add the code to execute when the Enter button is clicked
        self.close()
        subprocess.call(["python", "guiv.py"])

    def scan_button_clicked(self):
        # Add the code to handle barcode scanning from the mobile app
        # Receive the scanned barcode from the mobile app and update the CSV file

        # Simulating the scanned barcode from the mobile app
        value = input("Enter the scanned barcode: ")  # Prompt the user for the barcode input
        barcode = value

        update_csv_file("data.csv", row1[0], barcode)
        print(f"Barcode '{barcode}' added to the CSV file.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryManagementSystem(row1)
    window.show()
    sys.exit(app.exec_())
