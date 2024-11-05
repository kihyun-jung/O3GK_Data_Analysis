#!/usr/bin/env python

import numpy
import sys
import matplotlib
import subprocess
import time
import os
import argparse

from gwpy.timeseries import TimeSeries
from gwpy.time import tconvert
from glue.lal import Cache
from gwpy.segments import Segment
from termcolor import colored
from multiprocessing import Process, Queue

# Read Time information #
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-y", "--year", action="store", type=int)
parser.add_argument("-m", "--month", action="store", type=int)
parser.add_argument("-d", "--day", action="store", type=int)
parser.add_argument("-t", "--time", action="store", type=float)
parser.add_argument("-ch", "--channel", action="store", type=str)
parser.add_argument("-dur", "--duration", action="store", type=int)
parser.add_argument("-r","--roundwinner", action="store", type=int)
args = parser.parse_args()

year = args.year
month = args.month
day = args.day
ch = args.channel
dur = args.duration
time = args.time
rw = args.roundwinner
if month >= 10:
	if day >= 10:
                date=str("{0}-{1}-{2}".format(year,month,day))
	else:
                date=str("{0}-{1}-0{2}".format(year,month,day))

else:
        if day >= 10:
                date=str("{0}-0{1}-{2}".format(year,month,day))
        else:
                date=str("{0}-0{1}-0{2}".format(year,month,day))

matplotlib.use('Agg')
gwf_cache = '/data/kagra/home/kihyun.jung/Omicron/1daymkOmicron/{0}-gwf.lcf'.format(date)
if not os.path.exists('./{0}'.format(date)):
 subprocess.call('mkdir {0}'.format(date),shell=True)
i = int(time/32)
gst = int(i*32)
get = gst+32

with open(gwf_cache, 'r') as fobj:
    cache = Cache.fromfile(fobj)
    data = TimeSeries.read(cache, ch, start=gst, end=get, format='gwf.lalframe')
    ch = ch.strip("K1:")
    try :
        qspecgram = data.q_transform(qrange=(4, 64), frange=(0, 4096), gps=None, search=0.5, tres=0.001, fres=0.5, norm='median', outseg=(time, time+dur), whiten=True, fduration=1, highpass=None)
        q_plot = qspecgram.plot(figsize=[16, 12])
       	qax = q_plot.gca()
       	qax.set_xscale('seconds')
       	qax.set_yscale('log')
       	maxy = float(str(qspecgram.yindex[-1]).split(' ')[0])
       	#qax.set_xlabel('Qtransform-spectrum', fontsize=16)
        qax.set_epoch(time)
       	qax.set_ylim(0, 2048)
       	qax.set_ylabel('Frequency (Hz)', fontsize=16)
        qax.set_xlabel('Time (s)', fontsize=16)
        qax.grid(True, axis='y', which='both')
        #q_plot.add_colorbar(cmap='viridis', label='Normalized energy')
        q_plot.add_colorbar(cmap='viridis', label='Normalized energy', clim=[0,30])
        if rw == 0:
            q_plot.savefig("./{0}/Main-{1}-{2}-{3}.png".format(date, ch, time, dur))
        else:
            q_plot.savefig("./{0}/Round{1}-{2}-{3}-{4}.png".format(date, rw, ch, time, dur))
    except UnboundLocalError as err :
        pass
