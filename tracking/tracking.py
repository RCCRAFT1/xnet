import math
import xnet
import os

import http

lookup = xnet.object.tle(http.link("https://celestrak.org/"))

async def track(xnet, tle, object, coordinate):
    coordinates = xnet.track.coordinate()

    