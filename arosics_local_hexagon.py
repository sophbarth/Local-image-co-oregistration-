# -*- coding: utf-8 -*-
"""
Created on Fri May 14 10:39:02 2021

@author: sbarth
"""

from arosics import COREG_LOCAL



im_reference = r'N:/response/GIS_RS_projects/Sophia_Barth_SHK/Hexagon_georectify/owv01_20190831_mosaic_clip.tif'
im_target    = r'N:/response/GIS_RS_projects/Sophia_Barth_SHK/Hexagon_georectify/D3C1203-200197A009_c_new_clip.tif'
kwargs = {
    'grid_res'     : 500,
    'window_size'  : (25,25),
    'path_out'     : 'auto',
    'fmt_out'      : 'GTIFF',
    'max_shift'    : 40,
}


CRL = COREG_LOCAL(im_reference,im_target,**kwargs)


CRL.correct_shifts()

