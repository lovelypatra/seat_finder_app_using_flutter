import tkinter as tk
from tkinter import messagebox

class SeatFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seat Finder App")

        # Dictionary to map seat numbers to berth types
        self.berth_types = {
            1: "Lower",
            2: "Middle",
            3: "Upper",
            4: "Side Lower",
            5: "Side Upper"
        }

        # Create UI components
        self.create_ui()

    def create_ui(self):
        # Label for seat number input
        self.label = tk.Label(self.root, text="Enter seat number (1-72):", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Entry field for seat number input
        self.seat_number_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.seat_number_entry.pack()

        # Button to find berth type
        self.find_button = tk.Button(self.root, text="Find Berth", command=self.find_berth)
        self.find_button.pack(pady=10)

        # Label to display the result
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12), wraplength=300)
        self.result_label.pack()

    def find_berth(self):
        # Get seat number input from the entry field
        seat_number = self.seat_number_entry.get()

        try:
            # Convert seat number input to an integer
            seat_number = int(seat_number)

            # Check if seat number is within the valid range
            if 1 <= seat_number <= 72:
                # Calculate berth type based on seat number
                berth_type = self.berth_types[seat_number % 8]
                self.result_label.config(text=f"Seat number {seat_number} is a {berth_type} berth.")
            else:
                self.result_label.config(text="Seat number should be between 1 and 72.")
        except ValueError:
            # Handle invalid input (non-numeric)
            self.result_label.config(text="Invalid input. Please enter a valid seat number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SeatFinderApp(root)
    root.mainloop()
