import numpy as np
import ugradio
import astropy.coordinates
import astropy.time
import time
import matplotlib.pyplot as plt
import scipy
from socket import timeout

dish = ugradio.leusch.LeuschTelescope()

#use RA and dec of galactic north pole initially
# ra = 12 hr 54.1 min
# dec = 27 7 arcmin
ra = 193.5# degrees
dec = 27.1167 # degrees

#set frequency and amplitude
lo = ugradio.agilent.SynthDirect()
lo.set_frequency(635, 'MHz')

#print("LO is: " + str(lo.get_frequency()))
# start with noise on
noise = ugradio.leusch.LeuschNoise()
noise.on()

jd = ugradio.timing.julian_date(time.time())
alt,az = ugradio.coord.get_altaz(ra, dec, jd)
#dish.point(alt,az)

spec = ugradio.leusch.Spectrometer()
spec.read_spec('lab4data1-noiseon.fits', 20, (193.5,27.1167))
print(spec.int_time())

#switch to noise off
noise.off()

#dish.point(alt,az)

spec.read_spec('lab4data1-noiseoff.fits', 20, (193.5,27.1167))
print(spec.int_time())
