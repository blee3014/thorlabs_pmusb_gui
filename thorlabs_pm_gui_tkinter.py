"""
Author: Brian Lee (brian.lee@lyte.ai)
"""
import tkinter as tk
from tkinter import ttk
import pm100usb as pm

class ThorlabsPMWindow(tk.Tk):

    def __init__(self, SN: int | None = 0, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.SN = SN
        self.SN_text = tk.StringVar()
        self.SN_text.set(str(self.SN))
        self.initialize()

    def initialize(self):
        self.title("Thorlabs Power Meter PM100USB")
        default_win_width, default_win_height = 1000, 600
        self.geometry(f"{default_win_width}x{default_win_height}+1500+500")
        self.minsize(default_win_width,default_win_height)
        
        leftFrameWidthDefault = 250
        # setup left frame for settings and control and right frame for main power reading
        frameLeft = tk.Frame(master=self, width=leftFrameWidthDefault)
        frameLeft.grid(row=0,column=0, padx=5, pady=5, sticky='nsew')
        frameLeft.grid_rowconfigure(0, weight=1)
        frameLeft.grid_columnconfigure(0, weight=0)

        frameRight = tk.Frame(master=self, width=default_win_width-leftFrameWidthDefault)
        frameRight.grid(row=0,column=1, padx=5, pady=5, sticky='nsew')
        frameRight.grid_rowconfigure(0, weight=1)
        frameRight.grid_columnconfigure(0, weight=2)

        # setup right frame with large power numbers and unit.
        self.power = tk.DoubleVar()
        self.power.set('--')
        self.powerDisplay = ttk.Label(master=frameRight, textvariable=self.power,
                                      font='Helvetica, 150', anchor='e', justify='left')
        self.powerUnits = tk.StringVar()
        self.powerUnitsDisplay = ttk.Label(master=frameRight,textvariable=self.powerUnits,
                                           font="Helvetica, 50")

        self.powerUnitsDisplay.place(relx=0.85, y=default_win_height*0.45)
        self.powerDisplay.place(relx=0.2, y=default_win_height*0.275)

        # setup frame containing SN entry and button for initializing PM
        frameConnect = tk.Frame(master=frameLeft, width=leftFrameWidthDefault)
        frameConnect.pack(side='top')
        labelSN = ttk.Label(master=frameConnect, text='SN:')
        labelSN.grid(row=0, column=0, padx=3)

        self.entrySN = ttk.Entry(master=frameConnect, textvariable=self.SN_text)
        self.entrySN.grid(row=0, column=1)
        
        self.buttonInit = ttk.Button(master=frameConnect, text="Connect", command=self.connectPM)
        self.buttonInit.grid(row=1, column=0, columnspan=2)

        self.labelConnectionMsg = ttk.Label(master=frameConnect, anchor='center',text="Enter SN and press Connect", font="Helvetica, 10")
        self.labelConnectionMsg.grid(row=2,column=0,columnspan=2,pady=2)


        # setup frame for outputting sensor info.
        labelFrameSensor = ttk.LabelFrame(frameLeft, text="Sensor")
        labelFrameSensor.pack(fill=tk.BOTH, pady=10)

        # setup labels for sensor info within labelFrameSensor
        labelSensorName = ttk.Label(master=labelFrameSensor, text='Model:')
        self.labelSensorNameDisplay = ttk.Label(master=labelFrameSensor, text='', width=15)

        labelSensorSN = ttk.Label(master=labelFrameSensor, text='SN:')
        self.labelSensorSNDisplay = ttk.Label(master=labelFrameSensor, text='', width=15)

        labelSensorCalmsg = ttk.Label(master=labelFrameSensor, text='Cal msg:')
        self.labelSensorCalmsgDisplay = ttk.Label(master=labelFrameSensor, text='', width=15)

        labelSensorType = ttk.Label(master=labelFrameSensor, text='Type:')
        self.labelSensorTypeDisplay = ttk.Label(master=labelFrameSensor, text='', width=15)

        labelSensorSubType = ttk.Label(master=labelFrameSensor, text='Subtype:')
        self.labelSensorSubTypeDisplay = ttk.Label(master=labelFrameSensor, text='', width=15)

        labelSensorFlags = ttk.Label(master=labelFrameSensor, text='Flags:')
        self.labelSensorFlagsDisplay = ttk.Label(master=labelFrameSensor, text='', width=15)

        for i, label in enumerate([labelSensorName, labelSensorSN, labelSensorCalmsg, labelSensorType,
                                   labelSensorSubType, labelSensorFlags]):
            label.grid(row=i, column=0, padx=3, sticky='e')
        
        for i, labeldisplay in enumerate([self.labelSensorNameDisplay, self.labelSensorSNDisplay,
                                          self.labelSensorCalmsgDisplay, self.labelSensorTypeDisplay,
                                          self.labelSensorSubTypeDisplay, self.labelSensorFlagsDisplay]):
            labeldisplay.grid(row=i, column=1, sticky='ew')

        # setup frame for device settings like wavelength, LPF, averaging, units selection, zeroing/zero_value
        # disable this at first and only enable once PM100USB is connected
        labelFrameDevice = ttk.LabelFrame(frameLeft, text="Device", width=leftFrameWidthDefault)
        labelFrameDevice.pack(fill=tk.BOTH,pady=10, expand=True)

        labelWavelength = ttk.Label(labelFrameDevice, text="Wavelength")
        labelWavelength.grid(row=0,column=0,columnspan=3)

        self.wavelength = tk.IntVar()
        self.wavelength.set(1280)
        self.entryWavelength = ttk.Entry(labelFrameDevice, textvariable=self.wavelength, justify='right')
        self.entryWavelength.bind('<Return>', self.updateWavelength)
        self.entryWavelength['state'] = tk.DISABLED
        self.entryWavelength.grid(row=1,column=0)
        labelWavelengthUnit = ttk.Label(labelFrameDevice, text=' nm')
        labelWavelengthUnit.grid(row=1,column=1)

        labelAvg = ttk.Label(labelFrameDevice, text="Averaging")
        labelAvg.grid(row=2,column=0,columnspan=3)

        self.avg = tk.IntVar()
        self.avg.set(1)
        self.entryAvg = ttk.Spinbox(labelFrameDevice, textvariable=self.avg, from_=1.0, to=1000, justify='right')
        self.entryAvg.bind('<Return>', self.updateAvg)
        self.entryAvg['state'] = tk.DISABLED
        self.entryAvg.grid(row=3,column=0,columnspan=3)

        self.lpf = tk.IntVar()
        self.checkbuttonLPF = ttk.Checkbutton(labelFrameDevice, text='Low Pass Filter',
                                              variable=self.lpf, onvalue=1, offvalue=0, command=self.updateLPF)
        self.checkbuttonLPF.grid(row=4,column=0,columnspan=2, sticky='e')
        self.checkbuttonLPF['state'] = tk.DISABLED

        self.autorange = tk.IntVar()
        self.checkbuttonAutoRange = ttk.Checkbutton(labelFrameDevice, text='Auto Range',
                                                    variable=self.autorange, onvalue=1, offvalue=0,
                                                    command=self.updateAutoRange)
        self.checkbuttonAutoRange.grid(row=5,column=0,columnspan=2, sticky='e')
        self.checkbuttonAutoRange['state'] = tk.DISABLED

        labelUnits = ttk.Label(labelFrameDevice, text="Power Units")
        labelUnits.grid(row=6,column=0,columnspan=3)

        self.comboBoxUnits = ttk.Combobox(labelFrameDevice, textvariable=self.powerUnits, justify='right')
        self.comboBoxUnits.bind('<<ComboboxSelected>>', self.updateUnits)
        self.comboBoxUnits['values'] = ('W', 'dBm')
        self.comboBoxUnits.current(0)
        self.comboBoxUnits.state(["readonly"])
        self.comboBoxUnits.grid(row=6,column=0,columnspan=2, sticky='e')
        self.comboBoxUnits.option_add('*TCombobox*Listbox.Justify', 'right')
        self.comboBoxUnits['state'] = tk.DISABLED

        labelZero = ttk.Label(labelFrameDevice, text="Zero Adjust")
        labelZero.grid(row=7,column=0,columnspan=3)
        self.buttonZero = ttk.Button(labelFrameDevice, text="Zero", command=self.updateZero)
        self.buttonZero.grid(row=8, column=0)
        self.buttonZero['state'] = tk.DISABLED

        # self.zeroValue = tk.DoubleVar()
        # self.zeroValue.set(0)
        # labelZeroValue = ttk.Label(labelFrameDevice, textvariable=self.zeroValue)
        self.labelZeroValue = ttk.Label(labelFrameDevice, text='0')
        self.labelZeroValue.grid(row=8,column=1)

        labelZeroValueUnit = ttk.Label(labelFrameDevice, text="W")
        labelZeroValueUnit.grid(row=8,column=2)


    def connectPM(self):
        self.SN = self.entrySN.get()
        try:
            assert len(self.SN) == 7
            pmSN = int(self.SN)
            self.dev = pm.PM100usb(pmSN)
            if self.dev.init_res == -1:
                self.labelConnectionMsg['text'] = "Connection failed. Device not found."
            else:
                sensor_info = self.dev.sensor
                label_list = [self.labelSensorNameDisplay, self.labelSensorSNDisplay,
                            self.labelSensorCalmsgDisplay, self.labelSensorTypeDisplay,
                            self.labelSensorSubTypeDisplay, self.labelSensorFlagsDisplay]
                for i, key in enumerate(sensor_info.keys()):
                    label_list[i]['text'] = sensor_info[key]
                self.labelConnectionMsg['text'] = f"{self.dev.idn_msg}"

                self.entrySN['state'] = tk.DISABLED
                self.buttonInit['state']= tk.DISABLED

                self.entryWavelength['state'] = tk.ACTIVE
                self.entryAvg['state'] = tk.ACTIVE
                self.checkbuttonLPF['state'] = tk.ACTIVE
                self.checkbuttonAutoRange['state'] = tk.ACTIVE
                self.comboBoxUnits['state'] = tk.ACTIVE
                self.buttonZero['state'] = tk.ACTIVE

        except:
            self.labelConnectionMsg['text'] = "SN must be 7 digit number"

    def updateWavelength(self, event):
        wavelength = self.entryWavelength.get()
        self.wavelength.set(wavelength)
        self.dev.set_wavelength(wavelength)
        print(f"updating wavelength to {wavelength} nm")
        print(self.dev.get_error())

    def updateAvg(self, *args):
        avg = self.entryAvg.get()
        self.avg.set(avg)
        self.dev.set_average(avg)
        print(f"updating averaging to {avg} samples")
        print(self.dev.get_error())

    def updateLPF(self, *args):
        lpf = self.lpf.get()
        self.dev.set_lowpass_filter(lpf)
        print(f"LPF {self.lpf.get()}")
        print(self.dev.get_lowpass_filter())
        print(self.dev.get_error())

    def updateAutoRange(self, *args):
        ar = self.autorange.get()
        self.dev.set_autorange(ar)
        print(f"Auto range {self.autorange.get()}")
        print(self.dev.get_autorange())
        print(self.dev.get_error())

    def updateUnits(self, *args):
        units = self.powerUnits.get()
        self.dev.set_units(units.lower())
        print(f"Units {units}")
        print(self.dev.get_units())
        print(self.dev.get_error())
    
    def updateZero(self, *args):
        # do something with self.zeroValue, which you need to get from self.dev.zero()
        zero = self.dev.zero()
        # self.zeroValue.set(zero)
        self.labelZeroValue['text'] = zero
        print(f"new Zero {zero} W")
        print(self.dev.get_error())
        

def main():
    SN = 1924380
    app = ThorlabsPMWindow(SN)
    app.mainloop()




if __name__ == "__main__":
    main()