"""
mc-goods: `model_catalogs` catalogs for NOAA GOODS.
"""


from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("mc-nwgoa")
except PackageNotFoundError:
    # package is not installed
    pass


import intake
import os
here = os.path.abspath(os.path.dirname(__file__))


# after installation, these will be available as e.g. intake.cat.cbofs, with its sources

cbofs_rgrid = intake.open_catalog(os.path.join(here, 'cbofs-rgrid.yaml'), ttl=None)
cbofs = intake.open_catalog(os.path.join(here, 'cbofs.yaml'), ttl=None)
ciofs_rgrid = intake.open_catalog(os.path.join(here, 'ciofs-rgrid.yaml'), ttl=None)
ciofs = intake.open_catalog(os.path.join(here, 'ciofs.yaml'), ttl=None)
creofs_rgrid = intake.open_catalog(os.path.join(here, 'creofs-rgrid.yaml'), ttl=None)
creofs = intake.open_catalog(os.path.join(here, 'creofs.yaml'), ttl=None)
dbofs_rgrid = intake.open_catalog(os.path.join(here, 'dbofs-rgrid.yaml'), ttl=None)
dbofs = intake.open_catalog(os.path.join(here, 'dbofs.yaml'), ttl=None)
gfs_1_2deg = intake.open_catalog(os.path.join(here, 'gfs-1-2deg.yaml'), ttl=None)
gfs_1_4deg = intake.open_catalog(os.path.join(here, 'gfs-1-4deg.yaml'), ttl=None)
gfs_1deg = intake.open_catalog(os.path.join(here, 'gfs-1deg.yaml'), ttl=None)
gofs = intake.open_catalog(os.path.join(here, 'gofs.yaml'), ttl=None)
gomofs_2ds = intake.open_catalog(os.path.join(here, 'gomofs-2ds.yaml'), ttl=None)
gomofs_rgrid = intake.open_catalog(os.path.join(here, 'gomofs-rgrid.yaml'), ttl=None)
gomofs = intake.open_catalog(os.path.join(here, 'gomofs.yaml'), ttl=None)
leofs_rgrid = intake.open_catalog(os.path.join(here, 'leofs-rgrid.yaml'), ttl=None)
leofs = intake.open_catalog(os.path.join(here, 'leofs.yaml'), ttl=None)
lmhofs_rgrid = intake.open_catalog(os.path.join(here, 'lmhofs-rgrid.yaml'), ttl=None)
lmhofs = intake.open_catalog(os.path.join(here, 'lmhofs.yaml'), ttl=None)
loofs_fvcom = intake.open_catalog(os.path.join(here, 'loofs-fvcom.yaml'), ttl=None)
loofs = intake.open_catalog(os.path.join(here, 'loofs.yaml'), ttl=None)
lsofs_fvcom = intake.open_catalog(os.path.join(here, 'lsofs-fvcom.yaml'), ttl=None)
lsofs = intake.open_catalog(os.path.join(here, 'lsofs.yaml'), ttl=None)
ngofs2_2ds = intake.open_catalog(os.path.join(here, 'ngofs2-2ds.yaml'), ttl=None)
ngofs2_rgrid = intake.open_catalog(os.path.join(here, 'ngofs2-rgrid.yaml'), ttl=None)
ngofs2 = intake.open_catalog(os.path.join(here, 'ngofs2.yaml'), ttl=None)
nyofs = intake.open_catalog(os.path.join(here, 'nyofs.yaml'), ttl=None)
rtofs_2d = intake.open_catalog(os.path.join(here, 'rtofs-2d.yaml'), ttl=None)
rtofs_ak = intake.open_catalog(os.path.join(here, 'rtofs-ak.yaml'), ttl=None)
rtofs_east = intake.open_catalog(os.path.join(here, 'rtofs-east.yaml'), ttl=None)
rtofs_west = intake.open_catalog(os.path.join(here, 'rtofs-west.yaml'), ttl=None)
rtofs = intake.open_catalog(os.path.join(here, 'rtofs.yaml'), ttl=None)
sfbofs_rgrid = intake.open_catalog(os.path.join(here, 'sfbofs-rgrid.yaml'), ttl=None)
sfbofs = intake.open_catalog(os.path.join(here, 'sfbofs.yaml'), ttl=None)
tbofs_rgrid = intake.open_catalog(os.path.join(here, 'tbofs-rgrid.yaml'), ttl=None)
tbofs = intake.open_catalog(os.path.join(here, 'tbofs.yaml'), ttl=None)
wcofs_2ds = intake.open_catalog(os.path.join(here, 'wcofs-2ds.yaml'), ttl=None)
wcofs_rgrid = intake.open_catalog(os.path.join(here, 'wcofs-rgrid.yaml'), ttl=None)
wcofs = intake.open_catalog(os.path.join(here, 'wcofs.yaml'), ttl=None)
