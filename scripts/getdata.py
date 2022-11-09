'''
A script to pull files from NSIDC
'''
import requests
from requests.auth import HTTPBasicAuth
from io import BytesIO
import xarray as xr

#NSIDC parameters
user = "chrisrycx"
pw = "72kCh@kpkL4P"
nsidc_url = "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0719_SWE_Snow_Depth_v1/SWE_Mask_v01.nc"

#Request 
r = requests.get(nsidc_url, auth=(user,pw))
print(r.status_code)

#Try opening using xarray
data = xr.open_dataset(BytesIO(r.content),engine='h5netcdf')

print(data)