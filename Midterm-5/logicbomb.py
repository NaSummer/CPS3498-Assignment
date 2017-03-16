#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
from tkinter import *

count = 0
is_same = 0
date = int(time.strftime('%Y%m%d', time.localtime(time.time())))

class LogicBomb_GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text=('It is your lucky day!\nThe count is: ' + str(count)))
        self.helloLabel.pack()
        self.quitButton = Button(self, text='OK', command=self.quit)
        self.quitButton.pack()

while (not is_same):
    count += 1
    num = random.randint(10000000, 99999999)
    if (date == num):
        is_same = True

app = LogicBomb_GUI()
app.master.title('Lucky!')
app.mainloop()