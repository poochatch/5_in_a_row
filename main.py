import sys
import os
import board
import Tkinter as tk
from random import uniform, randint
from operator import itemgetter
from cpu_player import CPUPlayer
from human_player import HumanPlayer

s = 15
n = 5
b = board.Board(s,n)
btn =  [[0 for x in xrange(s)] for x in xrange(s)]
plrs = [HumanPlayer(b, n, 1), CPUPlayer(b, n, -1)]
tv = []
sliders = []

def play(x,y):

    if b.get(x,y) == 0:
        for plr in plrs:
            plr.play(x,y)
            action()
            if b.is_end() or b.is_full(): 
                    b.clear()
                    plr.won()
                    action()
                    tv[0].set('Score: ' + str(plrs[0].get_score()) + ' : ' + str(plrs[0].get_score()))
                    break

def action():

    for x in range(s):
        for y in range(s):
            if b.board[x][y] == 1:
                btn[x][y].config(bg="red")
            elif b.board[x][y] == -1:
                btn[x][y].config(bg="blue")
            else :
                btn[x][y].config(bg="white")


def gui():
    root = tk.Tk()
    title = 'Score: ' + str(plrs[0].get_score()) + ' : ' + str(plrs[0].get_score())
    root.title('Gomoku')
    frame=tk.Frame(root)
    frame.grid(row=0,column=0)
    tv.append(tk.StringVar())
    tk.Label(root, textvariable = tv[0]).grid(row = s)
     
    for x in range(s):
         for y in range(s):
            btn[x][y] = tk.Button(frame, command= lambda (i,j) = (x,y): play(i,j))
            btn[x][y].grid(column=y, row=x)

    action()
    root.mainloop()

def gui_start():
    root = tk.Tk()
    root.title('Gomoku')
    sliders.append(tk.Scale(root, from_=3, to=25))
    sliders.append(tk.Scale(root, from_=3, to=25))
    sliders[0].set(12)
    sliders[1].set(5)
    sliders[0].pack()
    sliders[1].pack()
    b = tk.Button(root, command= lambda: set_params())
    b.pack()
    root.mainloop()

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def simulation_array():
    ls = [[0.0] for x in range(400)]
    for a in ls:
        for i in range(5):
            a.append(uniform(0.0,10.0))
    return ls

def bot_choice():
    return(randint(0,399),randint(0,399))

def simulator(x):
    global count
    count += 1
    if count > 1000: 
        ls = sorted(simu_arr, key=itemgetter(0))
        st = ''
        for t in ls:
            st += str(t) + '\n'
        f1=open('./testfile', 'w+')
        f1.write(st)
        print(st)
        exit()
    global bots
    global simu_arr
    if x != -1:
        simu_arr[bots[x]][0] += 1.0
        simu_arr[bots[1 if x == 0 else 0]][0] -= 1.0
    bots = bot_choice()
    p = simu_arr[bots[0]][1:] + simu_arr[bots[0]][1:]
    for k in simu_arr:
        print(k)  
    play(1,1)

def set_params():
    s = sliders[0].get()
    n = sliders[1].get()
    print('totototot')
    print(s)
    print(n)
    gui()
        
def test():
    b.put(0,0,1)
    b.put(0,1,1)
    b.put(0,2,1)
    b.put(0,3,1)
    b.put(1,0,1)
    b.put(2,1,1)
    b.put(3,2,1)
    b.put(3,3,1)
    b.put(1,3,1)
    b.put(2,3,1)
    b.put(3,3,1)
    b.put(3,3,1)
 #   print(b.list_of_points(1))
#    print(b.lines_horizontal(b.list_of_points(1)))
 #   print(b.lines_vertical(b.list_of_points(1)))
 #   print(b.lines_slanted1(b.list_of_points(1)))
  #  print(b.lines_slanted2(b.list_of_points(1)))
    b.show()
   # print(b.max_len_of_line(1))
    print(b.best_move(1))
    action()


gui_start()
        
        
        
