#!usr/bin/python3.6

import os
import sys
import subprocess
import re
import argparse

# Read Time information #
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-y", "--year", action="store", type=int)
parser.add_argument("-m", "--month", action="store", type=int)
parser.add_argument("-d", "--day", action="store", type=int)
args = parser.parse_args()

year = args.year
month = args.month
day = args.day
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
subprocess.call("cp /data/kagra/home/kihyun.jung/Omicron/hveto_v2/{0}/logs/hveto.out ./".format(date),shell=True)

f = open('hveto.out','r')

line_num = 1
line = f.readline()
ch_list = []
get_nul = []
nu_rw = 0
duration = 4
main_ch = 'K1:DAC-STRAIN_C20'
while line:
 line = line.strip('\n')

 if '     channel' in line:
  get_nul.append(line_num)
  nu_rw += 1
 if 'winner :' in line:
  if not 'events' or not 'hveto' in line:
   ch = line.strip('winner :')
   ch = ch.strip(' ')
   ch_list.append(ch)
 line = f.readline()
 line_num += 1
f.close()

k = 0
tmp = [0,0,0,0,0,0,0,0,0,0,0]
f = open('hveto.out','r')
lines = f.readlines()

for i in range(0,nu_rw):
 try:
  for j in range(1,11):
   ovt = 1
   tmp[j-1] = re.findall('\d+',lines[get_nul[i]+j])[0]
   subprocess.call("python3.6 Qtransform-DAC.py -y {0} -m {1} -d {2} -t {3} -ch '{4}' -dur {5} -r 0".format(year,month,day,tmp[j-1],main_ch,duration),shell=True)
   subprocess.call("python3.6 Qtransform.py -y {0} -m {1} -d {2} -t {3} -ch '{4}' -dur {5} -r {6}".format(year,month,day,tmp[j-1],ch_list[i],duration,i+1),shell=True)
   tmp_c = int(tmp[j-1])
   k += 1
 except:
  continue
 tmp = [0,0,0,0,0,0,0,0,0,0,0]
print('{0} omega scans are generated'.format(k))
