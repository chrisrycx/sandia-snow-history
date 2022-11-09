'''
A function for extracting data from NM 4km snow dataset
Uses: 4km_SWE_Depth_NM.nc

'''

import xarray as xr
import pandas as pd

def getdata(location,snowtype='SWE'):
    '''
    Get a timeseries from the dataset at a location
    location - tuple (lat,long)
    snowtype - string 'SWE' or 'DEPTH'
    
    Returns - pandas series with data
    '''
    #Check that lat/long in bounds
    if location[0] < 34 or location[1] > -104:
        return pd.Series()

    if location[0] > 37 or location[1] < -107:
        return pd.Series()

    #Check snowtype
    if snowtype != 'SWE' and snowtype != 'DEPTH':
        raise ValueError('snowtype must be SWE or DEPTH')

    #Extract data
    with xr.open_dataset('data/4km_SWE_Depth_NM.nc') as ds:
        data = ds[snowtype].sel(lat=location[0],lon=location[1],method='nearest').to_pandas()

    return data
