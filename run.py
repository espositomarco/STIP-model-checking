import preprocess
import animation
from preprocess import Settings

lanes = 2
max_speed = 8
speed = [5, 6, 7]
progress = [0, 0, 0]
num_cars = 2
from_dir = ['RIGHT', 'BOTTOM', 'TOP']
to_dir   = ['BOTTOM', 'LEFT', 'BOTTOM']
acc_param = 1
dec_param = -1
max_time = 50
cell_progress = 30;

directions = ['TOP', 'RIGHT', 'BOTTOM', 'LEFT']

global_settings = Settings(lanes, speed, progress, num_cars, max_speed, from_dir, to_dir, acc_param, dec_param, max_time, cell_progress)



def run_model(model: str, settings, out: str = None, append = 'w'):
    print('\n\n------- '+model.upper()+' ---------\n')
    outname = preprocess.write_processed_model(model, settings)
    preprocess.compile_NuSMV(outname)
    anim = animation.animate_logfile('log.txt', settings)
    if out == None:
        print(anim)
    else:
        with open(out, append) as file:
            file.write(anim)


def run_protocol(settings = global_settings, out: str = None, append = 'w'):
    run_model('protocol', settings, out, append)


def run_planning(settings = global_settings, out: str = None, append = 'w'):
    run_model('planning', settings, out, append)

def run_planning_2cars_configurations():
    # 3*3*4*4*2*2 = 9 * 16 4 * < 160 * 4 = 640 
    from0 = 'BOTTOM' # in order to break symmetries.
    for to0 in directions:
        if from0 == to0 : continue
        for from1 in ['TOP', 'BOTTOM', 'LEFT']:
            for to1 in directions:
                if from1 == to1 : continue
                for speed0 in range(5,9):
                    for speed1 in range(5,9):
                        for progress0 in [0,15]:
                            for progress1 in [0,15]:
                                from_dir = [from0, from1]
                                to_dir = [to0, to1]
                                speed = [speed0, speed1]
                                progress = [progress0, progress1]
                                settings = Settings(lanes, speed, progress, num_cars, max_speed, from_dir, to_dir, acc_param, dec_param, max_time, cell_progress)

                                run_planning(settings, 'planning_results.txt', append = 'a')

# run_planning()
run_protocol()
# run_planning_all_configurations()


