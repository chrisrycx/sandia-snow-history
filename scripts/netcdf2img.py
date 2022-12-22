'''
Convert a netCDF file to a GeoTiff
See: https://nsidc.org/data/user-resources/help-center/how-extract-daily-swe-and-snow-depth-values-and-convert-them-geotiffs
'''

from osgeo import gdal

ds = gdal.Open('data/NMdata/4km_SWE_DEPTH_NM.nc')

#Subset data
ds.GetSubDatasets()

ds_sub = ('NETCDF:"data/NMdata/4km_SWE_DEPTH_NM.nc":SWE')
trans = gdal.Translate('data/NMdata/4km_SWE_NM_20050320.tif',ds_sub,bandList=[8572],outputSRS='EPSG:4326')