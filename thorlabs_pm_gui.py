"""
Author: Brian Lee (brian.lee@lyte.ai)
"""
import tkinter as tk
from tkinter import ttk
import pm100usb as pm

class ThorlabsPMWindow(tk.Tk):

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.initialize()

    def initialize(self):
        self.title("Thorlabs Power Meter")
        self.geometry("1000x500+1500+500")
        self.minsize(1000,500)
        
        # setup left frame for settings and control and right frame for main power reading
        frameLeft = tk.Frame(master=self, width=100)
        frameLeft.grid(row=0,column=0, padx=5, pady=5)

        frameRight = tk.Frame(master=self, width=800)
        frameRight.grid(row=0,column=1, padx=5, pady=5)

        # setup frame containing SN entry and button for initializing PM
        frameConnect = tk.Frame(master=frameLeft, width=100 , height=20)
        frameConnect.pack(side='top')
        labelSN = ttk.Label(master=frameConnect, text='SN:')
        labelSN.grid(row=0, column=0)

        intvarSN = tk.IntVar()
        entrySN = ttk.Entry(master=frameConnect, textvariable=intvarSN)
        entrySN.grid(row=0, column=1)
        
        buttonInit = ttk.Button(master=frameConnect, text="Connect", state=tk.DISABLED, command=self.connectPM())
        buttonInit.grid(row=1, column=0, columnspan=2)

        # setup frame for outputting PM usb info.
        
        # setup frame for outputting sensor information


    def connectPM(self):
        pass


def main():
    app = ThorlabsPMWindow()
    app.mainloop()




if __name__ == "__main__":
    main()