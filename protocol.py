# 0: [0, 0, 0, None] [8, 4, 7, None]
# 1: [0, 0, 0, None] [8, 5, 8, None]
# 2: [0, 0, 0, None] [8, 4, 8, None]
# 3: [0, 0, 0, None] [8, 3, 8, None]
# 4: [2, 0, 3, None] [8, 2, 8, None]
# 5: [2, 0, 3, None] [8, 1, 8, None]
# 6: [2, 0, 3, None] [8, 0, 8, None]
# 8: [1, 0, 4, None] [8, 0, 8, None]
# 10: [1, 0, 4, None] [8, 1, 8, None]
# 11: [1, 0, 4, None] [8, 2, 8, None]
# 12: [3, 0, 2, None] [8, 3, 8, None]
# 13: [3, 0, 2, None] [8, 4, 8, None]
# 14: [3, 4, 2, None] [8, 5, 8, None]
# 15: [5, 4, 5, None] [8, 6, 8, None]
# 16: [5, 4, 5, None] [8, 7, 8, None]
# 17: [5, 4, 5, None] [8, 8, 8, None]
# 19: [5, 2, 5, None] [8, 8, 8, None]
# 22: [5, 1, 5, None] [8, 8, 8, None]
# 26: [5, 5, 5, None] [8, 8, 8, None]

import preprocess
import animation
from preprocess import Settings

lanes = 2
max_tcl_index = lanes + 2
max_speed = 8
speed = [8, 4,7]
num_cars = 3
from_dir = (['RIGHT', 'BOTTOM', 'LEFT'])
to_dir   = (['BOTTOM'   , 'LEFT', 'TOP'])
acc_param = 1
dec_param = -1
max_time = 50
cell_progress = 30;

settings = Settings(lanes, max_tcl_index, speed, num_cars, max_speed, from_dir, to_dir, acc_param, dec_param, max_time, cell_progress)

model = 'protocol'
outname = preprocess.write_processed_model(model, settings)
preprocess.compile_NuSMV(outname)
print(animation.animate_logfile('log.txt'))
