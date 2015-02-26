# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

"code available at https://github.com/ohnorobo/massedu"
#%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# <codecell>

ap_participation = pd.read_csv("./MassEduDataChallenge/assessment/ap_participation_state_district_school_2007_2013.csv", sep='\t')
ap_performance = pd.read_csv("./MassEduDataChallenge/assessment/ap_performance_state_district_school_2007_2013.csv", sep='\t')
sats = pd.read_csv("./MassEduDataChallenge/assessment/sat_performance_report_state_district_school_2005_2013.csv", sep='\t')

# <codecell>

sats[:5]

# <codecell>

ap_performance[:5]

# <codecell>

boundaries = (-73.508142, -73.508142, 41.187053, 42.88679)
north, south, east, west = boundaries
b = Basemap(projection="lcc", 
            llcrnrlon=west,
            llcrnrlat=south,
            urcrnrlon=east,
            urcrnrlat=north,
            lat_0=(south+north)/2,
            lon_0=(east+west)/2)
info = b.readshapefile("./shapefiles/tl_2013_25_unsd/tl_2013_25_unsd", "districts")
#plt.show()
info

# <codecell>


# <codecell>


