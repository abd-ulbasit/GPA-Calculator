import tkinter
root = tkinter.Tk()
root.geometry("400x430")
root.title("GPA Calculator")
root.config(bg="#000066")
root.maxsize(400, 900)
root.minsize(400, 400)
grad = tkinter.StringVar()
crad = tkinter.StringVar()
grades = []
credits = []
totalweigh = []


def reset():
    global grades, credits, totalweigh
    grades = []
    credits = []
    totalweigh = []
    tkinter.Label(root, text="", bg="#000066", fg="white").place(
        x=(25), y=(140), width=175, height=660)  # to hide previous credits and grades
    tkinter.Label(root, text="", bg="#000066", fg='White').place(
        x=250, y=340, width=130, height=30)  # to hide previous Calculted GPA when Reset button is pressed
    tkinter.Label(root, text="", bg="#000066", fg='White').place(
        x=200, y=285, width=80, height=22)  # to hide calculate GPA button When reset is pressed
    tkinter.Label(root, text="", bg="#000066", fg='White').place(
        x=319, y=74, width=80, height=20)  # to hide reset button when reset button is pressed


def add():
    global grades, credits, data
    grade = grad.get().lower()
    credit = crad.get()
    if grade not in ['a', 'b+', 'b', 'c+', 'c', 'd', 'd+', 'f', 'xf'] or not credit.isnumeric() or int(credit) > 6:
        grad.set("")
        crad.set("")
        return
    else:
        grades.append(grade)
        credits.append(credit)
    grad.set("")
    crad.set("")
    for i in range(len(grades)):
        # Showing the Grades and Credits provided by user
        data = f"Credit Hours  :  {credits[i]} \t  Grade  : {grades[i].upper()}"
        tkinter.Label(root, text=data, anchor='w', bg="#000066", fg='White').place(
            x=(30), y=(150+22*i), width=160, height=20)
    tkinter.Button(root, text="Calculate GPA", command=calc).place(
        x=200, y=285, width=80, height=22)
    tkinter.Button(root, text="Reset", command=reset).place(
        x=329, y=74, width=70, height=20)


def calc():
    global gpa, grades, credits, totalweigh
    totalweigh = []
    for i in range(len(grades)):
        grades[i] = grades[i].lower()
    for i in range(len(credits)):
        credits[i] = int(credits[i])
    for i in range(len(grades)):
        if grades[i] == "a":
            totalweigh.append(4*int(credits[i]))
        elif grades[i] == "b+":
            totalweigh.append(3.5*int(credits[i]))
        elif grades[i] == "b":
            totalweigh.append(3*int(credits[i]))
        elif grades[i] == "c+":
            totalweigh.append(2.5*int(credits[i]))
        elif grades[i] == "c":
            totalweigh.append(2*int(credits[i]))
        elif grades[i] == "d+":
            totalweigh.append(1.5*int(credits[i]))
        elif grades[i] == "d":
            totalweigh.append(1*int(credits[i]))
        else:
            totalweigh.append(0)
    gpa = round(sum(totalweigh)/sum(credits), 4)

    tkinter.Label(root, text="GPA  =   "+str(gpa), bg="#000066", fg='White', font="30").place(
        x=250, y=340, width=130, height=30)
    # for i in range(2):
    # print("HEllo World")


tkinter.Label(root, text="Calculate Your GPA", bg="black", font="3",
              fg='White').place(x=1, y=1, width=398, height=72)
tkinter.Label(root, text="Credit Hours", bg="#000066", font=26,
              fg='White').place(x=30, y=80, width=100, height=20)
tkinter.Label(root, text="Grade", bg="#000066", font=26, fg='White').place(
    x=135, y=80, width=50, height=20)
tkinter.Entry(root, textvariable=crad).place(x=60, y=110, width=50, height=20)
tkinter.Entry(root, textvariable=grad).place(x=140, y=110, width=40, height=20)
tkinter.Button(root, text="ADD Course", command=add,).place(
    x=200, y=110, width=80, height=22)

tkinter.mainloop()
