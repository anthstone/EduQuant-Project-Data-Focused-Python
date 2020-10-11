# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:29:23 2020

@author: antho
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 

root = tk.Tk()

root.title("EduQuant--A Trading Simulator")

root.geometry('1200x750')

class MainPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        graph = Figure(figsize=(10,10), dpi=100)
        subplot = graph.add_subplot(111)
        subplot.plot([1,2,3,4,5,6,7,8],[1,3,2,6,4,12,8,16]) # Insert Stock Data Here
        #graph_labelframe = tk.LabelFrame(root, text="Stock Graphs")
        graph_canvas = FigureCanvasTkAgg(graph, self)
        graph_canvas.show()
        graph_canvas.get_tk_widget().pack(expand=True)
        #graph_labelframe.pack()
        














root.mainloop()