import numpy as np
import ugradio
import astropy.coordinates
import astropy.time
import time

dish = ugradio.leusch.leuschTelescope()
# galactic coordinates
# l = 120 #degrees
# b = 0 #degrees

# use RA and dec of galactic north pole initially
# ra = 12 hr 54.1 min
# dec = 27 7 arcmin
ra = 193.5  # degrees
dec = 27.1167  # degrees

# set frequency and amplitude
lo = ugradio.agilent.SynthDirect()
lo.set_frequency(635, 'MHz')

print("LO is: " + str(lo.get_frequency()))
# start with noise on
noise = ugradio.leusch.LeuschNoise()
noise.on()

# point telescope for 1 hour
sleep_time = 7
observation_time_h = 1
observation_time_s = observation_time_h * 60 * 60
loop_count = round(observation_time_s / sleep_time)

for i in range(0, round(loop_count/4)):
    # convert to alt and az
    #jd = ugradio.timing.julian_date(time.time())
    #alt, az = ugradio.coord.get_altaz(ra, dec, jd)
    alt, az = (37, 5) #(alt, az)
    dish.point(alt, az)
    
for i in range(0, round(loop_count/4)):
    # convert to alt and az
    #jd = ugradio.timing.julian_date(time.time())
    #alt, az = ugradio.coord.get_altaz(ra, dec, jd)
    alt, az = (32, 0) #(alt, az)
    dish.point(alt, az)

for i in range(0, round(loop_count/4)):
    # convert to alt and az
    #jd = ugradio.timing.julian_date(time.time())
    #alt, az = ugradio.coord.get_altaz(ra, dec, jd)
    alt, az = (37, -5) #(alt, az)
    dish.point(alt, az)
    
for i in range(0, round(loop_count/4)):
    # convert to alt and az
    #jd = ugradio.timing.julian_date(time.time())
    #alt, az = ugradio.coord.get_altaz(ra, dec, jd)
    alt, az = (42, 0) #(alt, az)
    dish.point(alt, az)
