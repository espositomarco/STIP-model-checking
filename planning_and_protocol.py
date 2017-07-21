import preprocess
import animation
from preprocess import Settings

lanes = 2
max_tcl_index = lanes + 2
max_speed = 8
speed = [8, 4, 7]
num_cars = 3
from_dir = (['RIGHT', 'BOTTOM', 'TOP'])
to_dir   = (['BOTTOM', 'LEFT', 'BOTTOM'])
acc_param = 1
dec_param = -1
max_time = 50
cell_progress = 30;


settings = Settings(lanes, max_tcl_index, speed, num_cars, max_speed, from_dir, to_dir, acc_param, dec_param, max_time, cell_progress)


model = 'protocol'
outname = preprocess.write_processed_model(model, settings)
print('\n\n-------	PROTOCOL ---------\n')
preprocess.compile_NuSMV(outname)
print(animation.animate_logfile('log.txt'))

model = 'planning'
print('\n\n-------	PLANNING ---------\n')
outname = preprocess.write_processed_model(model, settings)
preprocess.compile_NuSMV(outname)
print(animation.animate_logfile('log.txt'))


