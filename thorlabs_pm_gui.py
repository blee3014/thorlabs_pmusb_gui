"""
Author: Brian Lee (brian.lee@lyte.ai)
Date: 08/18/2024
"""
from PySide6.QtCore import Qt
from UI.thorlabs_pm_gui_ui import Ui_wMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

import pm100usb as pm
from math import log10


# Todo:
# After connecting to PM, Need to start measuring optical power. This should be done in another thread so that 
# PM parameters such as wavelength, avg, low pass, autorange can be changed and applied.
# 


class Window(QMainWindow, Ui_wMainWindow):

    def __init__(self, SN=0):
        super().__init__()

        self.setupUi(self)

         ### attributes ###
        self.SN = SN                                        # Serial number of PM
        self.wavelength = self.entryWavelength.text()       # wavelength
        self.avg = self.entryAvg.text()                     # averaging
        self.lpf = self.checkbuttonLPF.checkState()         # Low pass filter
        self.ar = self.checkbuttonAutoRange.checkState()    # auto range
        self.units = self.comboBoxUnits.currentText()       # units
        self.zero = 0                                       # zero measurement

        ### Connect Signals ###
        self.buttonInit.clicked.connect(self.connectPM)
        self.entryWavelength.returnPressed.connect(self.updateWavelength)
        self.entryAvg.valueChanged.connect(self.updateAvg)
        self.checkbuttonLPF.checkStateChanged.connect(self.updateLPF)
        self.checkbuttonAutoRange.checkStateChanged.connect(self.updateAutoRange)
        self.comboBoxUnits.currentIndexChanged.connect(self.updateUnits)
        self.buttonZero.clicked.connect(self.updateZero)


    def connectPM(self):
        print('Connect button pressed!')
        self.SN = self.entrySN.text()
        print(f'SN: {self.SN}')
        try:
            assert len(self.SN) == 7
            pmSN = int(self.SN)
            self.dev = pm.PM100usb(pmSN)
            if self.dev.init_res == -1:
                self.labelConnectionMsg.setText("Connection failed. Device not found.")
            else:
                sensor_info = self.dev.sensor
                label_list = [self.labelSensorModel, self.labelSensorSN,
                            self.labelSensorCalmsg, self.labelSensorType,
                            self.labelSensorSubtype, self.labelSensorFlag]
                for i, key in enumerate(sensor_info.keys()):
                    label_list[i].setText(sensor_info[key])
                self.labelConnectionMsg.setText(f"{self.dev.idn_msg}")

                self.zero = self.dev.zero()

                self.entrySN.setEnabled(False)
                self.buttonInit.setEnabled(False)

                self.entryWavelength.setEnabled(True)
                self.entryAvg.setEnabled(True)
                self.checkbuttonLPF.setEnabled(True)
                self.checkbuttonAutoRange.setEnabled(True)
                self.comboBoxUnits.setEnabled(True)
                self.buttonZero.setEnabled(True)

        except:
            self.labelConnectionMsg.setText("SN must be 7 digit number")

    def updateWavelength(self):
        self.wavelength = float(self.entryWavelength.text())
        print(self.wavelength)
        print(type(self.wavelength))
        self.dev.set_wavelength(self.wavelength)
        print(f"updating wavelength to {self.wavelength} nm")
        print(self.dev.get_error())

    def updateAvg(self):
        self.avg = int(self.entryAvg.text())
        print(self.avg)
        print(type(self.avg))
        self.dev.set_average(self.avg)
        print(f"updating averaging to {self.avg} samples")
        print(self.dev.get_error())

    def updateLPF(self):
        self.lpf = self.checkbuttonLPF.checkState()
        if self.lpf.value == 2:
            lpf = True
        else:
            lpf = False
        self.dev.set_lowpass_filter(lpf)
        print(f"LPF {lpf}")
        print(self.dev.get_lowpass_filter())
        print(self.dev.get_error())

    def updateAutoRange(self):
        self.ar = self.checkbuttonAutoRange.checkState()
        if self.ar.value == 2:
            ar = True
        else:
            ar = False
        self.dev.set_autorange(ar)
        print(f"Auto range {ar}")
        print(self.dev.get_autorange())
        print(self.dev.get_error())

    def updateUnits(self):
        self.units = self.comboBoxUnits.currentText()
        self.dev.set_units(self.units.lower())
        print(f"Units {self.units}")
        print(self.dev.get_units())
        print(self.dev.get_error())

    def updateZero(self):
        # do something with self.zeroValue, which you need to get from self.dev.zero()
        print("Zeroing...")
        self.zero = self.dev.zero()
        displayUnit, unitScale = Window._getUnit(self.zero)

        self.labelZeroValue.setText(f"{self.zero/unitScale:.4f}")
        self.labelZeroUnit.setText(displayUnit)
        print(f"new Zero {self.zero/unitScale:.4f} {displayUnit}")
        print(self.dev.get_error())

    @staticmethod
    def _getUnit(value):
        exponent = log10(abs(value))
        # if < 500 nW, use nW
        if (exponent < log10(500e-9)):
            return 'nW', 1e-9
        # if < 500 uW, use uW
        elif (log10(500e-9) <= exponent < -log10(500e-6)):
            return 'uW', 1e-6
        # if < 500 mW, use mW
        elif (log10(500e-6) <= exponent < -log10(500e-3)):
            return 'mW', 1e-3
        else:
            return 'W', 1



if __name__ == "__main__":
    SN = 1924380

    app = QApplication([])
    window = Window(SN=SN)

    window.show()
    app.exec()
