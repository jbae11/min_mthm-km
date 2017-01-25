##Optimization of MTHM*km by Havershine Formula

import numpy as np
import scipy as sc
import math

np.set_printoptions(threshold=np.inf)
#issues: stuff gets cut off (words)


data=np.array(['Reactor Name','Lat_degrees','Long_degrees','# assemblies','MTHM'])
temp=np.array(['Reactor Name','Lat_degrees','Long_degrees','# assemblies','MTHM'])
ref=np.array(['my house','40','90'])

#import csv and create 2d array of form
# name/lat(N)/long(W)/#of assemblies/MTHM
#saved as array 'data'.
import csv
with open('reactors_real.csv', 'rt') as csvfile:
    file = csv.reader(csvfile, delimiter= ',')
    for row in file:

    	temp[0]=row[0]
    	temp[1]=row[1]
    	temp[2]=row[2]
    	temp[3]=row[3]
    	temp[4]=row[4]
    	data=np.vstack((data,temp))



#function to get distance between two points (havershine formula_)
def getdistance(lat,long):

	# set values to zero.
	km=0
	mthmkm=0

	#in km, the earth's radius
	r=6371

	#compare the coordinate with all the reactor coordinates to get tot. distance and MTHM*km.
	for row in data[1:]:
		dlat=math.radians(float(row[1]))-math.radians(float(lat))
		dlong=math.radians(float(row[2]))-math.radians(float(long))
		a=(math.sin(dlat/2))**2+math.cos(math.radians(float(row[1])))*math.cos(math.radians(float(lat)))*(math.sin(dlong/2))**2
		c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
		d=r*c
		km=km+d
		mthmkm=mthmkm+d*float(row[4])
	
	#print('total distance from all the reactors to the reference point is: {} km'.format(km))
	#print('total MTHM*km from all the reactors to the reference point is: {} MTHM*km'.format(mthmkm))
	return mthmkm




#opimization part


#From border to border coordinates in the U.S.
latitude=np.linspace(25,50,50)
longitude=np.linspace(65,125,50)
#latitude/longitude/mthmkm
poop_array=np.zeros(3)
mthmkm_array=np.array([0,0,0])


#for every point in the US (from border to border), find all MTHM*km values
for i in latitude:
	for j in longitude:
		poop_array=np.array([i,j,getdistance(i,j)])
		mthmkm_array=np.vstack((mthmkm_array,poop_array))

#delete trivial first layer with value [0,0,0]
mthmkm_array=np.delete(mthmkm_array, (0), axis=0)


#convert strings to numbers
for k in range (len(mthmkm_array)):
	for l in range(len(mthmkm_array[k])):
		mthmkm_array[k][l]=float(mthmkm_array[k][l])

# give mimimum value array as x. 
x= mthmkm_array[np.argmin(mthmkm_array[:,2]),:]


#print results
print('The Optimized Coordinate with the Least Amount of MTHM*km is: \n {}N, {}W'.format(x[0],x[1]))
print('With MTHM*km value of: \n {} MTHM*km.'.format(x[2]))


