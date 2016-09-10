import fileinput
from sklearn.cluster import KMeans
from numpy import array

points = []

riders = 0
c = 0

for line in fileinput.input():
    c += 1
    res = line.split(" ")

    if c <= 2:
        if c == 1:
            riders = int(res[0])
        continue

    points.append([float(res[0]), float(res[1])])


if len(points) < riders:
    riders = len(points)

np_points = array(points)
k_means = KMeans(init='k-means++', n_clusters=riders, n_init=10)
k_means.fit(np_points)
labels = k_means.labels_

l = len(labels)
for i in range(0, riders):
    for j in range(0, l):
        if labels[j] == i:
            print j,

    print ''
