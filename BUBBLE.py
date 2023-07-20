import random
from tkinter import *



def display(bars,j,sort_limit):
    canvas.delete("all")
    padd = 10
    x = 1010
    y = 600
    for i in range(1,len(bars)+1):
        if i>sort_limit:
            bar_color = "white"
        elif i==j:
            bar_color = "white"
        else:
            bar_color = "red"

        canvas.create_line(i*10,y+padd,i*10,y+padd-bars[i-1],fill = bar_color,width = 7)
    root.update()

def bubble_sort(bars):
    comparisions = 0
    swaps = 0
    for i in range(len(bars)):
        for j in range(1,len(bars)-i):
            if bars[j]<bars[j-1]:
                bars[j],bars[j-1] = bars[j-1],bars[j]
                swaps+=1
                swaps_label.config(text = "No. of swaps: "+str(swaps))
            comparisions+=1
            no_of_comparisions.config(text="No. of comparisions: "+str(comparisions))
            display(bars,j+1,len(bars)-i)
            root.after(delay)

def decrease_speed():
    global delay
    delay+=5
    if delay>0:
        increase_button.config(state="normal")

def increase_speed():
    global delay
    if delay>0:
        delay-=1
    if delay==0:
        increase_button.config(state="disabled")


root = Tk()
root.title("Bubble Sort")

n = 100
bars = [random.randint(10,600) for i in range(n)]

canvas = Canvas(width = 1010,height = 650,bg = "black")
canvas.pack()

no_of_elements = Label(root,text="No. of elements: "+str(n),fg = "yellow",bg = "black")
no_of_comparisions = Label(root,text="No. of comparisions: 0",fg="yellow",bg="black")
swaps_label = Label(root,text = "No. of swaps: 0",fg="yellow",bg="black")
no_of_elements.place(x=4,y=3)
no_of_comparisions.place(x=4,y=23)
swaps_label.place(x=4,y=43)


decrease_button = Button(root,text="Decrease Speed", command=decrease_speed)
increase_button = Button(root,text="Increase Speed", command=increase_speed)
decrease_button.place(x=1010//2-150,y=620)
increase_button.place(x=1010//2+65,y=620)
delay = 100

bubble_sort(bars)

root.mainloop()