# 0: [0, 0, 0, None] [8, 4, 7, None]
# 1: [0, 0, 0, None] [7, 5, 6, None]
# 2: [0, 0, 0, None] [6, 6, 6, None]
# 3: [0, 0, 0, None] [5, 7, 7, None]
# 4: [0, 0, 0, None] [6, 8, 7, None]
# 5: [2, 4, 3, None] [7, 8, 8, None]
# 6: [2, 4, 3, None] [8, 8, 8, None]
# 9: [1, 2, 4, None] [8, 8, 8, None]
# 13: [3, 1, 2, None] [8, 8, 7, None]
# 15: [3, 1, 2, None] [8, 7, 6, None]
# 16: [3, 1, 2, None] [8, 6, 6, None]
# 17: [5, 5, 5, None] [7, 5, 7, None]

import preprocess
import animation
from preprocess import Settings

lanes = 2
max_tcl_index = lanes + 2
max_speed = 8
speed = [8, 4,7]
num_cars = 3
from_dir = (['RIGHT', 'BOTTOM', 'LEFT'])
to_dir   = (['BOTTOM', 'LEFT', 'TOP'])
acc_param = 1
dec_param = -1
max_time = 50
cell_progress = 30;


settings = Settings(lanes, max_tcl_index, speed, num_cars, max_speed, from_dir, to_dir, acc_param, dec_param, max_time, cell_progress)

model = 'planning'
outname = preprocess.write_processed_model(model, settings)
preprocess.compile_NuSMV(outname)
print(animation.animate_logfile('log.txt'))



