#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Frame, Label, Button


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_lbl = Label(self, text='hello world!')
        self.hello_lbl.pack()
        self.quit_btn = Button(self, text='quit', command=self.quit)
        self.quit_btn.pack()


def main():
    app = Application()
    app.master.title('hello world')
    app.mainloop()


if __name__ == '__main__':
    # main()
    app = Application()
    app.master.title('hello world')
    app.mainloop()
