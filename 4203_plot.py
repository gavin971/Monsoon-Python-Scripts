import os, sys

import cPickle as pickle

import glob

# import itertools
import matplotlib.pyplot as plt
import matplotlib.cm as mpl_cm
import numpy as np

import iris
import iris.coords as coords
#import iris.quickplot as qplt
import iris.plot as iplt
import iris.coord_categorisation

import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

import datetime

def main():

    first_of_year = datetime.date(2011, 01, 01)
    first_ordinal = first_of_year.toordinal()
    
    diagnostic = '4203'
    
    pickle_name = ('pickle_instant_rain_largescale_mean*_%s.p' % diagnostic)
    flist = glob.glob ('/home/pwille/python_scripts/*/%s' % pickle_name)


    for i in flist:

        fname = str(i)

        experiment_id = fname.split('/')[4]
        full_cube = pickle.load( open( fname, "rb" ) )
   

#experiment_id = fname.split('/')[6]
    
    #map_quest_aerial = cimgt.MapQuestOpenAerial()

        for sub_cube in full_cube.slices(['grid_latitude', 'grid_longitude']):
            
#Get date in iso fromat, if needed, for title

            #day=sub_cube_daily.coord('dayyear')
            #day_number = day.points[0]
            #day_number_ordinal=first_ordinal-1 + day_number
            #date_print = datetime.date.fromordinal(day_number_ordinal)
            #date_iso = str(date_print.isoformat())

            #sub_cube_daily.units = 'hPa'
            #sub_cube_daily /= 100

 # Load a Cynthia Brewer palette.
            brewer_cmap = mpl_cm.get_cmap('gist_rainbow')   
        #contour = qplt.contour(sub_cube_daily, brewer_cmap.N, cmap=brewer_cmap)
        
            #sub_cube.coord('grid_latitude').guess_bounds()
            #sub_cube.coord('grid_longitude').guess_bounds()

        # turn the iris Cube data structure into numpy arrays
            #gridlons = sub_cube.coord('grid_longitude').contiguous_bounds()
            #gridlats = sub_cube.coord('grid_latitude').contiguous_bounds()
            #sub_grid = sub_cube.data

            plt.axes(projection=ccrs.PlateCarree() )
        
        #rotated_pole = ccrs.RotatedPole(pole_longitude = 263, pole_latitude = 76) 

            iplt.pcolormesh(sub_cube, cmap=brewer_cmap)
   
            plt.title('Large scale rainfall rate mean: kg/m2/s: %s model run.' % (experiment_id), fontsize=10)
            #plt.title('Large scale rainfall rate mean: kg/m2/s: %s model run. %s' % (experiment_id, date_iso), fontsize=18)
        #plt.gridlines()
        #plt.gca().xlabel('longitude / degrees')
        #plt.ylabel('latitude / degrees')
            dx, dy = 10, 10
           
            # plt.clabel(contour, fmt='%d')
            #plt.gca().stock_img()
            plt.gca().coastlines(resolution='110m', color='black') 
            
          
            gl = plt.gca().gridlines(draw_labels=True,linewidth=1, color='gray', alpha=0.5, linestyle='--')
            gl.xlabels_top = False
            gl.ylabels_right = False
            #gl.xlines = False
            gl.xlocator = mticker.FixedLocator(range(60,105+dx,dx))
            gl.ylocator = mticker.FixedLocator(range(-10,30+dy,dx))
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER


            iplt.pcolormesh(sub_cube, cmap=brewer_cmap)
            #gl.xlabel_style = {'size': 15, 'color': 'gray'}
            #gl.xlabel_style = {'color': 'red', 'weight': 'bold'}
            #plt.savefig('/home/pwille/python_scripts/pngs/%s/msl_daily_mean_%s_%s.png' % (experiment_id, experiment_id, date_iso))
#plt.savefig('/home/pwille/python_scripts/pngs/%s/%s_daily_mean_%s_%s.png' % (experiment_id, diagnostic, experiment_id, date_iso))
#plt.close()

            plt.show()
if __name__ == '__main__':
    main()
