import math
sqrt = []
for n in range(0, 3000):
	sqrt.append(int(math.sqrt(n)))
# print(sqrt)

acc = -1
speed = 15
progress = 0
p = progress
v = speed
max_speed = 20
t_max_speed = (max_speed - speed ) // acc
CELL = 3
	
for T in range(1,100):
	if (T < t_max_speed and acc * T * (T+1) / 2 + speed * T + progress >  CELL * 100 ):
		print('ecco', T)
		break
	if (T >= t_max_speed and acc * t_max_speed * (t_max_speed+1) / 2 + speed * t_max_speed + (T-t_max_speed) * max_speed + progress >  CELL * 100):
		print('ecco', T)
		break

for T in range(1,100):
	v = max(min(v + acc, max_speed), 0)
	p += v
	print('sim:',T, v, p)

	# car0.timeAt_5 = 63
	# car0.timeAt_4 = 51
	# car0.timeAt_3 = 38
	# car0.timeAt_2 = 26
	# car0.timeAt_1 = 13


	# car0.timeAt_5 = 63
	# car0.timeAt_4 = 50
	# car0.timeAt_3 = 38
	# car0.timeAt_2 = 25
	# car0.timeAt_1 = 13

	# x = acc*(t*t+t)//2 + speed * t
	# print('anl:', x)

# 0 = acc*t*(t+1)/2 + speed * t

# for X in range(4):
# 	print('sqrt', 4*speed*speed + acc*acc + 4*speed*acc + 8*acc*( X*100 - progress ))
# 	v = (sqrt[ 4*speed*speed + acc*acc + 4*speed*acc + 8*acc*( X*100 - progress ) ] - (2 * speed + acc) ) / (2*acc)
# 	print(v)
	# print('init(sqrt['+str(n)+']) :=', int(math.sqrt(n)),';')
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