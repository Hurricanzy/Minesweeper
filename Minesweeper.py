import tkinter as tk
window=tk.Tk()

ROW=5
COLUMNS=3
buttons=[]
for i in range(ROW):
    temp=[]
    for j in range(COLUMNS):
        btn=tk.Button(window, width=5, font= 'Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)
for ROW_btn in buttons:
    print(ROW_btn)

for i in range(ROW):
    for j in range(COLUMNS):
        btn=buttons[i][j]
        btn.grid(row=i,column=j)

window.mainloop()