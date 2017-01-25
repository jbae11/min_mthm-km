# min_mthm-km
Finds the coordinate that has the least amount of mthm*km.

Metric Ton Heavy Metal (MTHM) is a unit of Spent Nuclear Fuel (SNF)
which are currently stored on-site in commercial nuclear power plants.
A simple python code is written to analyse the most optimal point
(solely on distance) to site a repository.

The distance is calculated by using the havershine formula,
and assessed all the coordinate points in the continental U.S.
to find the coordinate with the minimum MTHM*km value.

The current resolution is 50X50 (Continental U.S. divided into 2500 sectors
for evaluation). The resolution can be modified by changing the 
third term in line 63 and 64.

### optimizing_MTHM_km.py
Python code run to find the coordinate with the minimum mthm*km value.

### reactors_real.csv
This csv file is created parsing wikipedia data and Curie Map data
(curie.ornl.gov/map). The columns are as follows: Reactor name, latitude,
longitude, #of assemblies, MTHM. The coordinates are from Wikipedia
and the # of assemblies and MTHM data is from the Curie Map. 
When modified, the csv file needs to follow its format to work properly.


