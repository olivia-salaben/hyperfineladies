import numpy as np
import ugradio
import astropy.coordinates
import astropy.time
import time
from astropy.time import Time

# recording object
spec = ugradio.leusch.Spectrometer()

# telescope object
dish = ugradio.leusch.LeuschTelescope()

# set frequency and amplitude
lo = ugradio.agilent.SynthDirect()
lo.set_frequency(635, 'MHz')

# start with noise on
noise = ugradio.leusch.LeuschNoise()

# create grid of pointing coordinates
galactic_1d_grid = []
galactic_latitude_array = np.arange(49, 50, 2)
galactic_longitude_array = np.arange(113, 160, 2)

leusch_lat = ugradio.leo.lat
leusch_lon = ugradio.leo.lon
leusch_alt = ugradio.leo.alt
leusch = astropy.coordinates.EarthLocation(lat=leusch_lat, lon=leusch_lon, height=leusch_alt)

for lat in galactic_latitude_array:
    for long in galactic_longitude_array:
        galactic_1d_grid.append((lat, long))

galactic_1d_grid = np.array(galactic_1d_grid)
pointings = astropy.coordinates.SkyCoord(galactic_1d_grid[:,1], galactic_1d_grid[:,0], frame='galactic', unit='deg')

# iterate through points
i = 0
for pointing in pointings:
    obs_time = Time(time.time(), format='unix', location=leusch)
    pointings_altaz = astropy.coordinates.AltAz(location=leusch, obstime=obs_time)
    final_pointings_altaz = pointing.transform_to(pointings_altaz)
    alt = final_pointings_altaz.alt.deg
    az = final_pointings_altaz.az.deg
    if alt < 85 and alt > 15 and az > 5 and az < 350:
        dish.point(final_pointings_altaz.alt.deg, final_pointings_altaz.az.deg)

        # noise on
        noise.on()
        spec.read_spec('../Data/celestial_pole-noiseon_' + str(galactic_1d_grid[i][0]) + str(galactic_1d_grid[i][1]) + '.fits', 2, (galactic_1d_grid[i][0], galactic_1d_grid[i][1]))

        # noise off
        noise.off()
        spec.read_spec('../Data/celestial_pole-noiseoff_' + str(galactic_1d_grid[i][0]) + str(galactic_1d_grid[i][1]) + '.fits', 20, (galactic_1d_grid[i][0], galactic_1d_grid[i][1]))

        print(str(final_pointings_altaz.alt.deg), str(final_pointings_altaz.az.deg), str(i))
        i += 1
    else:
        print('Pointing Error at ' + str(galactic_1d_grid[i][0])+ ',' + str(galactic_1d_grid[i][1]))

dish.stow()
print("THE RECORDING HAS ENDED AND THE DISH HAS BEEN STOWED")
print("HAVE A NICE DAY")
# alt az is not in degrees
# test on jupyter notebook
# stow?
# save to new repo and old repo
# save to "Data" folder that u create
