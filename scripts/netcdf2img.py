'''
Convert a netCDF file to a GeoTiff
See: https://nsidc.org/data/user-resources/help-center/how-extract-daily-swe-and-snow-depth-values-and-convert-them-geotiffs
'''

from osgeo import gdal

ds = gdal.Open('data/4km_SWE_DEPTH_NM.nc')

#Subset data
ds.GetSubDatasets()

ds_sub = ('NETCDF:"data/4km_SWE_DEPTH_NM.nc":SWE')
trans = gdal.Translate('data/4km_SWE_NM_day246.tif',ds_sub,bandList=[246],outputSRS='EPSG:4326')