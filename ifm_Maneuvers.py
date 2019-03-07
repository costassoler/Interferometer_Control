
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
def observation_run(Ra,Dec,dur,inter,data_file_name):
    '''
    Arguments:
    Ra is your object's right ascension in degrees
    Dec is your object's declination in degrees
    dur is the duration of your capture run in seconds
    inter is the interval between data samples (in seconds)
    data_file_name is your data file's name :o
    
    Returns:
    a data file, 'data_file_name.npz' containing the data 
    from your observation run.
    '''
    
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
        try:
            i+=1
            AltAz = ugradio.coord.get_altaz(Ra,Dec)
            alt = AltAz[0]
            az = AltAz[1]
            ifm.point(alt,az) 
            if i%10 == 0:
                intermediate_data = hpm.get_recording_data()
                np.savez(data_file_name + str(i) + '.npz', volts = intermediate_data[0], time = intermediate_data[1]) 
            if(i*60>dur):
                hpm.end_recording()
                data = hpm.get_recording_data()
                np.savez(data_file_name+'.npz',volts = data[0], time = data[1])
                ifm.stow()
                break
            time.sleep(60)
        except:
            hpm.end_recording()
            data = hpm.get_recording_data()
            np.savez(data_file_name+'.npz',data=data)
            ifm.stow()
            print('an error occurred but at least your data was saved!')
 







