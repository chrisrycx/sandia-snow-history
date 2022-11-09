'''
Play around with xarray and netcdf

'''

import xarray as xr

data = xr.open_dataset('data/4km_SWE_Depth_WY1982_v01.nc')

subset = data.sel(lat=slice(33, 37), lon=slice(-109,-103))

#Extract data array
swe = subset['SWE']

