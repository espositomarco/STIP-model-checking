import math

for n in range(0, 3000):
	print('init(sqrt['+str(n)+']) :=', int(math.sqrt(n)),';')
# acc = 3
# max_vel = 8
# v = 10
# p = 0
# cell = 0
# for t in range(0, 30):
# 	v += acc
# 	p += v
# 	# print(t, p, cell)
# 	if cell != p // 100:
# 		cell = p // 100
# 		print(t, p, cell)

#( sqrt[ 4*speed*speed + acc*acc + 4*speed*acc + 8*acc*x ] - (2 * speed + acc) ) / (2*acc)