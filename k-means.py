import sys
import itertools
import math
import random


# distance point1, point2 takes two lists of ordered pairs and calculates
# the distance between them
def distance(point1, point2):
	d = math.sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
	return d

# This function takes the list of points and centroids
# and recalculates the centroids to match the center points of the clusters
def recalculate_centroid(point, centroid):
	for i, c in enumerate(centroid):
		xpos = 0
		ypos = 0
		inc = 1
		for p in point:
			if p[2] == i:
				xpos += p[0]
				ypos += p[1]
				inc += 1
		c[0] = xpos/inc
		c[1] = ypos/inc


# This function takes the point and centroid lists and partitions
# the data into clusters based on distance from each centroid
def partition(point, centroid):
	temp_distance = []
	#Find points that are closest to each centroid
	for i in point:
		for j in centroid:
			temp_distance.append(distance(i,j))
		if len(i) < 3:
			i.append(temp_distance.index(min(temp_distance)))
		else:
			i[2] = temp_distance.index(min(temp_distance))
		temp_distance = []


fin = open("./input.txt", mode='r')
fout = open("./output.txt", mode='w')

# Read data and split it into substrings
data = fin.read()
data = data.split(None, sys.maxint)

# take in k as the command line argument
k = int(sys.argv[1])



#this loop creates a parallel list of xpos and ypos
#also it converts every ypos and xpos to an int
point = []
for i, item in enumerate(data):
	if not(i % 2):
		temp = [int(data[i]), int(data[i+1])]
		point.append(temp)


# keep repeating this loop until k uniqe points have been chosen
centroid = []
i = 0
while i < k:
	insert = point[random.randrange(0, len(point))]
	print insert
	print centroid.count(insert)
	if centroid.count(insert) == 0:
		centroid.append(point[random.randrange(0,len(point))])
		i+=1


for i in range(20):
	partition(point, centroid)
	recalculate_centroid(point, centroid)
	partition(point, centroid)

for i in point:
	line = str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
	fout.write(line)

for i in centroid:
	line = str(i[0]) + " " + str(i[1]) + "\n"
	fout.write(line)


print "Please see output.txt for coordinates and data labels"

fin.close()
fout.close()