import matplotlib.pyplot as plt
'''
plt.plot([1, 2, 3, 4])
plt.show()
'''

'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
'''

'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
'''


import numpy as np

'''
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
'''

'''
plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], 'r')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], 'g')
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], 'b')
plt.xlabel('X-Axis')
plt.xlabel('Y-Axis')

plt.show()
'''

# graph 채우기
'''
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y[1:3], alpha=0.5)

plt.show()
'''

# 두 그래프 사이 영역 채우기
'''
x = [1, 2, 3, 4]
y1 = [2, 3, 5, 10]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y1[1:3], y2[1:3], color='lightgray', alpha=0.5)

plt.show()
'''


# 투명도와 컬러맵 설정
'''
np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30* np.random.rand(n))**2
colors = np.random.rand(n)

plt.scatter(x, y, s = area, c = colors, alpha = 0.5, cmap = 'Spectral')
plt.colorbar()
plt.show()
'''

# 3차원 산점도 그리기

from mpl_toolkits.mplot3d import Axes3D

n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
cmin, cmax = 0, 2

xs = np.array([(xmax - xmin) * np.random.random_sample() + xmin for i in range(n)])
ys = np.array([(ymax - ymin) * np.random.random_sample() + ymin for i in range(n)])
zs = np.array([(zmax - zmin) * np.random.random_sample() + zmin for i in range(n)])
color = np.array([(cmax - cmin) * np.random.random_sample() + cmin for i in range(n)])

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection= "3d")
ax.scatter(xs, ys, zs, c=color, marker='o', s=15, cmap='Greens')

plt.show()