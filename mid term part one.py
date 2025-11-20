from tkinter import *

# Function to calculate and display points
def calculate_points():
    try:
        # Get number of books from the entry box
        books = int(entry_books.get())

        # Determine points based on number of books
        if books < 2:
            points = 0
        elif books < 4:
            points = 5
        elif books < 6:
            points = 15
        elif books < 8:
            points = 30
        else:
            points = 60

        # Display the result
        lbl_result.config(text=f"You earned {points} points this month!")

    except ValueError:
        lbl_result.config(text="Please enter a valid number.")

# -------------------------------------------------------------
# GUI Setup
# -------------------------------------------------------------
root = Tk()
root.title("Serendipity Book Club Points")
root.geometry("400x250")
root.resizable(0, 0)
root.configure(bg="light blue")

# Instruction label
lbl_instruction = Label(root, text="Enter the number of books purchased this month:",
                        bg="light blue", font=("Arial", 11))
lbl_instruction.pack(pady=15)

# Entry box for user input
entry_books = Entry(root, width=10, font=("Arial", 12))
entry_books.pack(pady=5)

# Button to calculate points
btn_calculate = Button(root, text="Calculate Points", command=calculate_points,
                       bg="light green", font=("Arial", 11))
btn_calculate.pack(pady=10)

# Label to show result
lbl_result = Label(root, text="", bg="light blue", font=("Arial", 12, "bold"))
lbl_result.pack(pady=15)

# Run the GUI
root.mainloop()