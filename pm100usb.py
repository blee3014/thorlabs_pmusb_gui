import pyvisa as visa
import sys
import time
import pdb


class PM100usb():
    def __init__(self, sn) -> None:
        self.sn = sn
        self._rm = visa.ResourceManager()
        self.dev = None
        self.zero_value = None
        self.write_delay = 0.1

        self.init_res = self._init_dev()
        if self.init_res == -1:
            self.sensor = None
        else:
            self.idn_msg = self.idn(1)
            self.reset()
            self.sensor = self.get_sensor()

    def _init_dev(self):
        for dev in self._rm.list_resources():
            if str(self.sn) in dev.split("::"):
                self.dev = self._rm.open_resource(dev)
                return 0

        print(f"PM100USB with SN {self.sn} Not found.")
        return -1

    def reset(self):
        self.dev.write("*RST")
        time.sleep(self.write_delay)
        self.dev.write("*CLS")
        time.sleep(self.write_delay)
        self.dev.write("conf:pow")
        time.sleep(self.write_delay)

    def idn(self, verbose=0):
        msg = self.dev.query("*IDN?")
        time.sleep(self.write_delay)
        if verbose:
            print(msg)
        return msg

    def zero(self):
        self.dev.query("corr:coll:zero:stat?")
        zero_value = self.dev.query_ascii_values("corr:coll:zero:magn?")[0]
        for i in range(3):
            self.dev.write("corr:coll:zero")
            time.sleep(self.write_delay*5)
            self.dev.query("corr:coll:zero:stat?")

        zero_value = self.dev.query_ascii_values("corr:coll:zero:magn?")[0]
        time.sleep(self.write_delay)
        self.zero_value = zero_value
        return zero_value

    def get_error(self, verbose=0):
        msg = self.dev.query("syst:err?")
        time.sleep(self.write_delay)
        if verbose:
            print(msg)
        return msg

    def get_sensor(self):
        sensor_info = self.dev.query("syst:sens:idn?")[:-1]
        time.sleep(self.write_delay)
        parsed_info = sensor_info.split(',')
        sensor_key = ["name", "sn", "cal_msg", "type", "subtype", "flags"]
        sensor_dict = {key: value for key, value in zip(sensor_key, parsed_info)}
        return sensor_dict

    def get_average(self):
        return self.dev.query_ascii_values("aver?")[0]

    def get_wavelength(self):
        return self.dev.query_ascii_values("corr:wav?")[0]

    def get_autorange(self):
        return self.dev.query_ascii_values("pow:rang:auto?")[0]

    def get_responsivity(self):
        return self.dev.query_ascii_values("corr:pow?")[0]

    def get_units(self):
        return self.dev.query("pow:unit?")

    def get_lowpass_filter(self):
        return self.dev.query_ascii_values("inp:filt?")[0]

    def set_average(self, average):
        self.dev.write(f"aver {average}")
        time.sleep(self.write_delay)

    def set_wavelength(self, wavelength):
        self.dev.write(f"corr:wav {wavelength}")
        time.sleep(self.write_delay)

    def set_autorange(self, autorange=True):
        self.dev.write(f"pow:rang:auto {int(autorange)}")
        time.sleep(self.write_delay)

    def set_units(self, units='dbm'):
        if units.lower() not in ['dbm', 'w']:
            print("units must be 'w' or 'dbm'.")
            return -1
        else:
            self.dev.write(f"pow:unit {units}")
            time.sleep(self.write_delay)

    def set_lowpass_filter(self, lowpass=False):
        self.dev.write(f"inp:filt {int(lowpass)}")
        time.sleep(self.write_delay)

    def meas_power(self):
        res = self.dev.query_ascii_values("read?")[0]
        time.sleep(self.write_delay)
        return res


def main():
    sn = 1924380

    # todo: zero() seems to have a bug. on script it doesn't zero but on debug / interactive mode it works.
    global pm
    pm = PM100usb(sn)
    pm.zero()
    print(pm.zero_value)

    pm.set_units('w')
    pm.set_average(1)
    pm.set_lowpass_filter(True)

    while 1:
        print(pm.meas_power())

if __name__ == "__main__":
    main()
