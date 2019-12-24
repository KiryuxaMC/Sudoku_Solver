from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import Solver as S

def read_file():
    try:
        file_name = fd.askopenfilename()
        with open(file_name, "r") as rf:
            content = rf.readlines()
            for i in range(9):
                newMass = list(content[i].split(' '))
                for j in range(9):
                    fields[i][j].delete(0, END)
                    fields[i][j].insert(0, newMass[j])
    except:
        mb.showwarning("Warning", "I can't open the file")
        return 0

def solve_sudoku():
    for i in range(9):
        for j in range(9):
            if fields[i][j].get().isalpha() or len(fields[i][j].get()) > 1:
                mb.showerror("Error", "Invalid data in cell "+str(i+1)+":"+str(j+1))
                return 0

            if fields[i][j].get().isdigit():
                sudoku[i][j] = int(fields[i][j].get())
                
            if fields[i][j].get() == "0" or fields[i][j].get() == '':
                fields[i][j].config(bg="#a6c4f5")
                continue

    solution = S.SudokuSolver.solve( sudoku )
    if solution:
        for i in range(9):
            for j in range(9):
                fields[i][j].delete(0, END)
                fields[i][j].insert(0, str(solution[i][j]))
    else:
        mb.showinfo("Information","I can't solve this Sudoku :(")
        return 0
    

def delete_data():
    for i in range(9):
        for j in range(9):
            fields[i][j].delete(0, END)
            fields[i][j].config(bg="white")

def exit_app():
    exit()

root = Tk()
root.title("Sudoku Solver")
mainmenu = Menu(root)
root.configure(menu=mainmenu)

mainmenu.add_command(label="Read file", command=read_file)
mainmenu.add_command(label="Solve", command=solve_sudoku)
mainmenu.add_command(label="Delete Data", command=delete_data)
mainmenu.add_command(label="Exit", command=exit_app)


fields = []
frame_rows = []
sudoku = []

for i in range(9):
    if i%3 == 0:
        Frame(width=27, height=6).pack()
    fields.append([])
    sudoku.append([])
    frame_rows.append(Frame())
    frame_rows[i].pack()
    for j in range(9):
        if j%3 == 0:
            Frame(frame_rows[i], width=6, height=27).pack(side=LEFT)
        fields[i].append(Entry(frame_rows[i], width=3, justify=CENTER))
        sudoku[i].append(0)
        fields[i][j].pack(side=LEFT)



root.mainloop()