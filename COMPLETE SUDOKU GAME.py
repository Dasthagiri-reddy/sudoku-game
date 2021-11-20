from tkinter import *
root =Tk()
from tkinter import messagebox
import random
root.title("Sudoku Game")
root.geometry("324x550")

label=Label(root,text="SUDOKU GAME").grid(row=0,column=1,columnspan=10)

errlabel= Label(root,text="",fg="red")
errlabel.grid(row=15,column=1,columnspan=10,pady=5)
solvedlabel= Label(root,text="",fg="green")
solvedlabel.grid(row=15,column=1,columnspan=10,pady=5)

N=9

def isSafe(sudoku,row,col,num):
    for i in range(9):
        if sudoku[row][i]==num:
            return False
    for i in range(9):
        if sudoku[i][col]==num:
            return False
    
    startrow=row-row%3
    startcol=col-col%3
    for i in range(3):
        for j in range(3):
            if sudoku[startrow+i][startcol+j]==num:
                return False
    return True

def solvesudoku(sudoku,row,col):
    if row==N-1 and col==N:
        return True
    if col==N:
        row+=1
        col=0
    if sudoku[row][col]>0:
        return solvesudoku(sudoku,row,col+1)
    for num in range(1,N+1):
        if isSafe(sudoku,row,col,num):
            sudoku[row][col]=num
            if solvesudoku(sudoku,row,col+1):
                return True
        sudoku[row][col]=0
    return False

def solver(sudoku):
    if solvesudoku(sudoku,0,0):
        return sudoku
    else:
        return "no"
        

cells={}
def ValidateNumber(P):
    out=(P.isdigit()or P =="" and len(P)<2)
    return out
reg = root.register(ValidateNumber)
  
def draw3x3grid(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e= Entry(root, width=5,bg=bgcolor,justify="center",validate="key",validatecommand=(reg,"%P"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[row+i+1,column+j+1]=e
        
def draw9x9grid():
    color="#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3grid(rowNo,colNo,color)
            if(color=="#D0ffff"):
                color="#ffffd0"
            else:
                color="#D0ffff"
                        
def clearValues():
    errlabel.configure(text="")
    solvedlabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10): 
            cell=cells[(row,col)]
            cell.delete(0,"end")
    messagebox.showinfo("sudoku Game","create your own puzzle")

def getValues():
    board=[]
    errlabel.configure(text="")
    solvedlabel.configure(text="")   
    for row in range(2,11):
        rows=[]
        for col in range(1,10):
            val=cells[(row,col)].get()
            if(val==""):
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

def updateValues(sudoku):
    sol=solver(sudoku)
    if sol!="no":
        for rows in range (2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
    else:
        errlabel.cofigure(text="No olution exists for this sudoku")
        
def insertValues():
    errlabel.configure(text="")
    solvedlabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10): 
            cell=cells[(row,col)]
            cell.delete(0,"end")
    cells[(1+1,2)].insert(0,random.randint(1,9))
    cells[(6+1,1)].insert(0,random.randint(1,9))
    cells[(9+1,3)].insert(0,random.randint(1,9))
    cells[(2+1,5)].insert(0,random.randint(1,9))
    cells[(3+1,8)].insert(0,random.randint(1,9))
    cells[(5+1,6)].insert(0,random.randint(1,9))
    cells[(4+1,9)].insert(0,random.randint(1,9)) 
    cells[(7+1,4)].insert(0,random.randint(1,9))   
    cells[(8+1,7)].insert(0,random.randint(1,9))

    
    
            
    
buton=Button(root,command=insertValues,text="Start",width=10)
buton.grid(row=20,column=0,columnspan=5,pady=20)
btn=Button(root,command=getValues,text="Solve",width=10)
btn.grid(row=20,column=3,columnspan=5,pady=20)
btn1=Button(root,command=clearValues,text="Clear",width=10)
btn1.grid(row=20,column=6,columnspan=5,pady=20)



draw9x9grid()
root.mainloop()
                    
                    