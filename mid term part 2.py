
data = pd.read_csv("midterm_exam.csv")

# -------------------------
# Label for displaying results
# -------------------------
lb = Label(main_window, justify="left", bg="white", fg="black", anchor="w",
           font=("Arial", 11), width=55, height=15, wraplength=450)
lb.place(x=70, y=180)

# -------------------------
# Button functions
# -------------------------
def calender():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected.to_string(index=False), bg="white")

def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected = df[~df['Buildings'].isnull()]
    lb.config(text=selected.to_string(index=False), bg="white")

def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected = df[~df['FacultyName'].isnull()]
    lb.config(text=selected.to_string(index=False), bg="white")

def business_school():
    output = """School of Business Departments:
- Accounting
- Finance
- Management & Organization
- Marketing
- Management Information Systems (MIS)
- Business Analytics"""
    lb.config(text=output, bg="#E0FFFF")  # Light cyan background

def mis_department():
    output = """MIS Department Courses:
- Intro to MIS
- Databases Management
- Systems Analysis & Design
- Business Analytics / Data Visualization
- Network and Information Security
- Project Management"""
    lb.config(text=output, bg="#E6E6FA")  # Light lavender background

# -------------------------
# Buttons setup
# -------------------------
button1 = Button(main_window, text='Calendar', command=calender, bg="light green", width=12)
button1.place(x=70, y=130)

button2 = Button(main_window, text='Buildings', command=building, bg="light green", width=12)
button2.place(x=190, y=130)

button3 = Button(main_window, text='Faculty', command=faculty, bg="light green", width=12)
button3.place(x=310, y=130)

button4 = Button(main_window, text='School of Business', command=business_school, bg="light blue", width=15)
button4.place(x=70, y=430)

button5 = Button(main_window, text='MIS Department', command=mis_department, bg="light pink", width=15)
button5.place(x=250, y=430)

# -------------------------
main_window.mainloop()
