# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:29:23 2020

@author: antho
"""

import tkinter as tk
from tkinter.ttk import Style, Frame
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 

root = tk.Tk()

root.title("EduQuant--A Trading Simulator")

root.geometry('1200x750')

Stock_Name = "APPL"

#
Style().configure("TFrame", background="#333")

#Create Frame for Stock Listings
stock_list_lf = tk.LabelFrame(root, height = 500, width = 200, text="Stock List")
#stock_list_lf.place(x=10, y=10)
stock_list_lf.pack(side="left", anchor="nw")
stock_list_label = tk.Label(stock_list_lf, text="Insert Stock List Here")
stock_list_label.pack(fill="both")

#Create Frame for Stock Graph
graph_labelframe = tk.LabelFrame(root, height=100, width = 500, text = "Stock Price Data")
#graph_labelframe.place(x=250, y=10)
graph_labelframe.pack(side="left", anchor="n")
label = tk.Label(graph_labelframe, text=Stock_Name)
label.pack()

#Graph
graph = Figure(figsize=(6,3), dpi=100)
subplot = graph.add_subplot(111)
subplot.plot([1,2,3,4,5,6,7,8],[1,3,2,6,4,12,8,16]) # Insert Stock Data Here

#canvas for graph
graph_canvas = FigureCanvasTkAgg(graph, master = graph_labelframe)
graph_canvas.draw()
graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)













root.mainloop()