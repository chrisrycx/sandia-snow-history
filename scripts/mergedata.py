'''
Combine all 4km SWE years into one subset of northern NM
'''

import xarray as xr

#Open the first array and subset
data82 = xr.open_dataset('data/RawNetCDF/4km_SWE_Depth_WY1982_v01.nc')
data = data82[['SWE','DEPTH']].sel(lat=slice(34, 37), lon=slice(-107,-104))

#Iterate through data to create merged
for year in range(1983,2022,1):
    print(f'Merging year {year}')
    with xr.open_dataset(f'data/RawNetCDF/4km_SWE_Depth_WY{year}_v01.nc') as ds:
        subset = ds[['SWE','DEPTH']].sel(lat=slice(34, 37), lon=slice(-107,-104))
        data = xr.concat([data,subset],dim='time')

print(data)

#Save to file
data.to_netcdf('data/4km_SWE_Depth_NM.nc')

