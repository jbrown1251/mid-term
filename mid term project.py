import tkinter as tk

def calculate_points():
    try:
        books = int(entry_books.get())
        if books < 0:
            result_label.config(text="Please enter a valid number of books.")
            return

        if books == 0:
            points = 0
        elif books == 2:
            points = 5
        elif books == 4:
            points = 15
        elif books == 6:
            points = 30
        elif books >= 8:
            points = 60
        else:
            points = 0  # For cases like 1, 3, 5, 7 (optional rule)

        result_label.config(text=f"You earned {points} points this month!")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create main window
window = tk.Tk()
window.title("Serendipity Booksellers - Book Club Points")

# Instruction label
label_instruction = tk.Label(window, text="Enter the number of books purchased this month:")
label_instruction.pack(pady=5)

# Entry widget for user input
entry_books = tk.Entry(window, width=10)
entry_books.pack(pady=5)

# Compute button
compute_button = tk.Button(window, text="Compute Points", command=calculate_points)
compute_button.pack(pady=5)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the application
window.mainloop()