import Tkinter as tk


def gui(s):
    root = tk.Tk()
    frame=tk.Frame(root)
    frame.grid(row=0,column=0)

    btn =  [[0 for x in xrange(s)] for x in xrange(s)] 
    for x in range(s):
         for y in range(s):
            btn[x][y] = tk.Button(frame, command= lambda: main.action(x,y))
            btn[x][y].grid(column=x, row=y)

    root.mainloop()


    


