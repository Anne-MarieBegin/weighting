#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:25:55 2020

@author: begin
"""

import xarray as xr
import numpy as np
import pandas as pd

data = xr.DataArray(np.random.randn(2, 3), dims=("x", "y"), coords={"x": [10, 20]})
date=xr.DataArray(np.random.randn(2, 3), dims=("x", "y"), coords={"x": [10, 20]})