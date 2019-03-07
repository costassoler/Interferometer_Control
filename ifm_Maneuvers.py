
# coding: utf-8

# In[3]:

import numpy as np
import time
import ugradio
def track(Ra,Dec):
    ifm = ugradio.interf.Interferometer()

    while True:
        AltAz = ugradio.coord.get_altaz(Ra,Dec)
        alt = AltAz[0]
        az = AltAz[1]
        ifm.point(alt,az)
        time.sleep(60)
            
            
            
        
    

def track_collect(Ra,Dec):
    ifm = ugradio.interf.Interferometer()
    hpm = ugradio.hp_multi.HP_Multimeter()
    i = 0
    dt = 1
    
    AltAz = ugradio.coord.get_altaz(Ra,Dec)
    alt = AltAz[0]
    az = AltAz[1]
    ifm.point(alt,az)
    time.sleep(60)
    hpm.start_recording(dt)
    while True:
        i+=1
        AltAz = ugradio.coord.get_altaz(Ra,Dec)
        alt = AltAz[0]
        az = AltAz[1]
        ifm.point(alt,az) 
        if( i == 4):
            hpm.end_recording()
            data = hpm.get_recording_data()
            np.savez('Mars_test.npz',data=data)
            ifm.stow()
            break
        time.sleep(60)
# In[ ]:




# In[ ]:



