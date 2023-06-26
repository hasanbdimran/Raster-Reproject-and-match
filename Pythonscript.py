import rioxarray # for the extension to load
import xarray
## Loading two raster for reproject and match operation
xds = xarray.open_dataarray(os.path.join(file_dir, 'rasterize', 'test.tif'))
xds_match = xarray.open_dataarray(r"/Users/ihasan/Downloads/TAMU/TTI_project/dem_30m_mosaic/TX_NADEP_30m.tif")

xds_repr_match = xds.rio.reproject_match(xds_match, nodata=-1)

## Exporting the processed matched raster to tif file
xds_repr_match.rio.to_raster(os.path.join(file_dir, 'rasterize', 'test1.tif'))
