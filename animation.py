# from graphics import *



# cars = [Circle] * 4
# colors = [str] * 4
# colors[0] = color_rgb(255,0,0)
# colors[1] = color_rgb(255,0,0)
# colors[2] = color_rgb(0,255,0)
# colors[3] = color_rgb(0,0,255)



# def xy_position_index(i: int, size: int) -> Point:
#     l = size // 4
#     if i == 1 : return Point(l, l)
#     if i == 2 : return Point(3*l, l)
#     if i == 3 : return Point(l, 3*l)
#     if i == 4 : return Point(3*l, 3*l)
#     return Point(-100, -100)





def animate_string(text : str) -> str:
    positions = [None] * 4
    speeds = [None] * 4
    positions[0] = 5

    output = ''
    states = text.split('State:')
    states = states[1:]
    for i,state in enumerate(states):
        lines = state.splitlines()
        something_changed = False
        for line in lines:
            if 'crash = TRUE' in line:
                output += 'crash : ' + line.strip() + '\n'
            if '.position' in line:
                something_changed = True
                car, pos = line.strip().split('=')
                name, _ = car.split('.')
                positions[eval(name[3:])] = eval(pos)
            if '.speed' in line:
                something_changed = True
                car, speed = line.strip().split('=')
                name, _ = car.split('.')
                speeds[eval(name[3:])] = eval(speed)
        
        if something_changed:
            output += str(i) + ': ' + str(positions) + ' ' + str(speeds) + '\n'

    return output + '\n'


def animate_logfile(log_filename = 'log.txt') -> str:
    # size = 100
    # win = GraphWin("My Circle", size, size, autoflush=False)
    # for i in positions:
    #     c = Circle(xy_position_index(0, 100), 10)
    #     win.addItem(c)

    with open(log_filename) as log:
        text = log.read()

    return animate_string(text)

if __name__ == '__main__':
    print(animate_logfile())

    log = '''Trace Description: CTL Counterexample 
Trace Type: Counterexample 
  -> State: 1.1 <-
    car0.id = 0
    car0.tcl[0] = 0
    car0.tcl[1] = 2
    car0.tcl[2] = 1
    car0.tcl[3] = 5
    car0.tcl[4] = 5
    car0.from = 1
    car0.to = 3
    car0.priority = 46
    car1.id = 1
    car1.tcl[0] = 0
    car1.tcl[1] = 4
    car1.tcl[2] = 2
    car1.tcl[3] = 1
    car1.tcl[4] = 5
    car1.from = 2
    car1.to = 3
    car1.priority = 45
    car0.speed = 8
    car0.progress = 0
    car0.decision[0] = 1
    car0.decision[1] = 1
    car1.speed = 4
    car1.progress = 0
    car1.decision[0] = 1
    car1.decision[1] = 1
    conflict[0][0][0][0] = 0
    conflict[0][0][0][1] = 0
    conflict[0][0][0][2] = 0
    conflict[0][0][0][3] = 0
    conflict[0][0][1][0] = 0
    conflict[0][0][1][1] = 0
    conflict[0][0][1][2] = 0
    conflict[0][0][1][3] = 0
    conflict[0][0][2][0] = 0
    conflict[0][0][2][1] = 0
    conflict[0][0][2][2] = 0
    conflict[0][0][2][3] = 0
    conflict[0][0][3][0] = 0
    conflict[0][0][3][1] = 0
    conflict[0][0][3][2] = 0
    conflict[0][0][3][3] = 0
    conflict[0][1][0][0] = 0
    conflict[0][1][0][1] = 1
    conflict[0][1][0][2] = 1
    conflict[0][1][0][3] = 1
    conflict[0][1][1][0] = 0
    conflict[0][1][1][1] = 0
    conflict[0][1][1][2] = 1
    conflict[0][1][1][3] = 1
    conflict[0][1][2][0] = 3
    conflict[0][1][2][1] = 3
    conflict[0][1][2][2] = 0
    conflict[0][1][2][3] = 1
    conflict[0][1][3][0] = 2
    conflict[0][1][3][1] = 2
    conflict[0][1][3][2] = 2
    conflict[0][1][3][3] = 0
    conflict[0][2][0][0] = 0
    conflict[0][2][0][1] = 1
    conflict[0][2][0][2] = 1
    conflict[0][2][0][3] = 1
    conflict[0][2][1][0] = 0
    conflict[0][2][1][1] = 0
    conflict[0][2][1][2] = 1
    conflict[0][2][1][3] = 1
    conflict[0][2][2][0] = 0
    conflict[0][2][2][1] = 0
    conflict[0][2][2][2] = 0
    conflict[0][2][2][3] = 1
    conflict[0][2][3][0] = 2
    conflict[0][2][3][1] = 2
    conflict[0][2][3][2] = 2
    conflict[0][2][3][3] = 0
    conflict[0][3][0][0] = 0
    conflict[0][3][0][1] = 1
    conflict[0][3][0][2] = 1
    conflict[0][3][0][3] = 1
    conflict[0][3][1][0] = 0
    conflict[0][3][1][1] = 0
    conflict[0][3][1][2] = 1
    conflict[0][3][1][3] = 1
    conflict[0][3][2][0] = 0
    conflict[0][3][2][1] = 0
    conflict[0][3][2][2] = 0
    conflict[0][3][2][3] = 1
    conflict[0][3][3][0] = 0
    conflict[0][3][3][1] = 0
    conflict[0][3][3][2] = 0
    conflict[0][3][3][3] = 0
    conflict[1][0][0][0] = 0
    conflict[1][0][0][1] = 0
    conflict[1][0][0][2] = 0
    conflict[1][0][0][3] = 0
    conflict[1][0][1][0] = 1
    conflict[1][0][1][1] = 0
    conflict[1][0][1][2] = 1
    conflict[1][0][1][3] = 1
    conflict[1][0][2][0] = 1
    conflict[1][0][2][1] = 0
    conflict[1][0][2][2] = 0
    conflict[1][0][2][3] = 1
    conflict[1][0][3][0] = 1
    conflict[1][0][3][1] = 0
    conflict[1][0][3][2] = 0
    conflict[1][0][3][3] = 0
    conflict[1][1][0][0] = 0
    conflict[1][1][0][1] = 0
    conflict[1][1][0][2] = 0
    conflict[1][1][0][3] = 0
    conflict[1][1][1][0] = 0
    conflict[1][1][1][1] = 0
    conflict[1][1][1][2] = 0
    conflict[1][1][1][3] = 0
    conflict[1][1][2][0] = 0
    conflict[1][1][2][1] = 0
    conflict[1][1][2][2] = 0
    conflict[1][1][2][3] = 0
    conflict[1][1][3][0] = 0
    conflict[1][1][3][1] = 0
    conflict[1][1][3][2] = 0
    conflict[1][1][3][3] = 0
    conflict[1][2][0][0] = 0
    conflict[1][2][0][1] = 2
    conflict[1][2][0][2] = 2
    conflict[1][2][0][3] = 2
    conflict[1][2][1][0] = 1
    conflict[1][2][1][1] = 0
    conflict[1][2][1][2] = 1
    conflict[1][2][1][3] = 1
    conflict[1][2][2][0] = 1
    conflict[1][2][2][1] = 0
    conflict[1][2][2][2] = 0
    conflict[1][2][2][3] = 1
    conflict[1][2][3][0] = 1
    conflict[1][2][3][1] = 3
    conflict[1][2][3][2] = 3
    conflict[1][2][3][3] = 0
    conflict[1][3][0][0] = 0
    conflict[1][3][0][1] = 2
    conflict[1][3][0][2] = 2
    conflict[1][3][0][3] = 2
    conflict[1][3][1][0] = 1
    conflict[1][3][1][1] = 0
    conflict[1][3][1][2] = 1
    conflict[1][3][1][3] = 1
    conflict[1][3][2][0] = 1
    conflict[1][3][2][1] = 0
    conflict[1][3][2][2] = 0
    conflict[1][3][2][3] = 1
    conflict[1][3][3][0] = 1
    conflict[1][3][3][1] = 0
    conflict[1][3][3][2] = 0
    conflict[1][3][3][3] = 0
    conflict[2][0][0][0] = 0
    conflict[2][0][0][1] = 1
    conflict[2][0][0][2] = 0
    conflict[2][0][0][3] = 0
    conflict[2][0][1][0] = 2
    conflict[2][0][1][1] = 0
    conflict[2][0][1][2] = 2
    conflict[2][0][1][3] = 2
    conflict[2][0][2][0] = 1
    conflict[2][0][2][1] = 1
    conflict[2][0][2][2] = 0
    conflict[2][0][2][3] = 1
    conflict[2][0][3][0] = 1
    conflict[2][0][3][1] = 1
    conflict[2][0][3][2] = 0
    conflict[2][0][3][3] = 0
    conflict[2][1][0][0] = 0
    conflict[2][1][0][1] = 1
    conflict[2][1][0][2] = 0
    conflict[2][1][0][3] = 0
    conflict[2][1][1][0] = 0
    conflict[2][1][1][1] = 0
    conflict[2][1][1][2] = 0
    conflict[2][1][1][3] = 0
    conflict[2][1][2][0] = 1
    conflict[2][1][2][1] = 1
    conflict[2][1][2][2] = 0
    conflict[2][1][2][3] = 1
    conflict[2][1][3][0] = 1
    conflict[2][1][3][1] = 1
    conflict[2][1][3][2] = 0
    conflict[2][1][3][3] = 0
    conflict[2][2][0][0] = 0
    conflict[2][2][0][1] = 0
    conflict[2][2][0][2] = 0
    conflict[2][2][0][3] = 0
    conflict[2][2][1][0] = 0
    conflict[2][2][1][1] = 0
    conflict[2][2][1][2] = 0
    conflict[2][2][1][3] = 0
    conflict[2][2][2][0] = 0
    conflict[2][2][2][1] = 0
    conflict[2][2][2][2] = 0
    conflict[2][2][2][3] = 0
    conflict[2][2][3][0] = 0
    conflict[2][2][3][1] = 0
    conflict[2][2][3][2] = 0
    conflict[2][2][3][3] = 0
    conflict[2][3][0][0] = 0
    conflict[2][3][0][1] = 1
    conflict[2][3][0][2] = 3
    conflict[2][3][0][3] = 3
    conflict[2][3][1][0] = 2
    conflict[2][3][1][1] = 0
    conflict[2][3][1][2] = 2
    conflict[2][3][1][3] = 2
    conflict[2][3][2][0] = 1
    conflict[2][3][2][1] = 1
    conflict[2][3][2][2] = 0
    conflict[2][3][2][3] = 1
    conflict[2][3][3][0] = 1
    conflict[2][3][3][1] = 1
    conflict[2][3][3][2] = 0
    conflict[2][3][3][3] = 0
    conflict[3][0][0][0] = 0
    conflict[3][0][0][1] = 1
    conflict[3][0][0][2] = 1
    conflict[3][0][0][3] = 0
    conflict[3][0][1][0] = 3
    conflict[3][0][1][1] = 0
    conflict[3][0][1][2] = 1
    conflict[3][0][1][3] = 3
    conflict[3][0][2][0] = 2
    conflict[3][0][2][1] = 2
    conflict[3][0][2][2] = 0
    conflict[3][0][2][3] = 2
    conflict[3][0][3][0] = 1
    conflict[3][0][3][1] = 1
    conflict[3][0][3][2] = 1
    conflict[3][0][3][3] = 0
    conflict[3][1][0][0] = 0
    conflict[3][1][0][1] = 1
    conflict[3][1][0][2] = 1
    conflict[3][1][0][3] = 0
    conflict[3][1][1][0] = 0
    conflict[3][1][1][1] = 0
    conflict[3][1][1][2] = 1
    conflict[3][1][1][3] = 0
    conflict[3][1][2][0] = 2
    conflict[3][1][2][1] = 2
    conflict[3][1][2][2] = 0
    conflict[3][1][2][3] = 2
    conflict[3][1][3][0] = 1
    conflict[3][1][3][1] = 1
    conflict[3][1][3][2] = 1
    conflict[3][1][3][3] = 0
    conflict[3][2][0][0] = 0
    conflict[3][2][0][1] = 1
    conflict[3][2][0][2] = 1
    conflict[3][2][0][3] = 0
    conflict[3][2][1][0] = 0
    conflict[3][2][1][1] = 0
    conflict[3][2][1][2] = 1
    conflict[3][2][1][3] = 0
    conflict[3][2][2][0] = 0
    conflict[3][2][2][1] = 0
    conflict[3][2][2][2] = 0
    conflict[3][2][2][3] = 0
    conflict[3][2][3][0] = 1
    conflict[3][2][3][1] = 1
    conflict[3][2][3][2] = 1
    conflict[3][2][3][3] = 0
    conflict[3][3][0][0] = 0
    conflict[3][3][0][1] = 0
    conflict[3][3][0][2] = 0
    conflict[3][3][0][3] = 0
    conflict[3][3][1][0] = 0
    conflict[3][3][1][1] = 0
    conflict[3][3][1][2] = 0
    conflict[3][3][1][3] = 0
    conflict[3][3][2][0] = 0
    conflict[3][3][2][1] = 0
    conflict[3][3][2][2] = 0
    conflict[3][3][2][3] = 0
    conflict[3][3][3][0] = 0
    conflict[3][3][3][1] = 0
    conflict[3][3][3][2] = 0
    conflict[3][3][3][3] = 0
    THETA = 1
    num_cars = 2
    cars_exited = FALSE
    car0car1_crash = FALSE
    car0.EXITING = FALSE
    car0.CROSSING = FALSE
    car0.APPROACHING = TRUE
    car0.accelTimeAt_5 = 19
    car0.accelTimeAt_4 = 15
    car0.accelTimeAt_3 = 12
    car0.accelTimeAt_2 = 8
    car0.accelTimeAt_1 = 4
    car0.timeAt_5 = 19
    car0.timeAt_4 = 15
    car0.timeAt_3 = 12
    car0.timeAt_2 = 8
    car0.timeAt_1 = 4
    car0.dec_param = -1
    car0.acc_param = 1
    car0.acc = 1
    car0.next_speed_acc = 8
    car0.next_speed = 8
    car0.t_max_speed_acc = 0
    car0.t_null_speed = -8
    car0.t_max_speed = 0
    car0.position = 0
    car0.tcl_index = 0
    car0.max_progress = 120
    car0.cell_progress = 30
    car0.max_speed = 8
    car0.max_position = 5
    car0.max_tcl_index = 4
    car0.lanes = 2
    car1.EXITING = FALSE
    car1.CROSSING = FALSE
    car1.APPROACHING = TRUE
    car1.accelTimeAt_5 = 19
    car1.accelTimeAt_4 = 16
    car1.accelTimeAt_3 = 12
    car1.accelTimeAt_2 = 8
    car1.accelTimeAt_1 = 4
    car1.timeAt_5 = 20
    car1.timeAt_4 = 16
    car1.timeAt_3 = 12
    car1.timeAt_2 = 9
    car1.timeAt_1 = 5
    car1.dec_param = -1
    car1.acc_param = 1
    car1.acc = 1
    car1.next_speed_acc = 5
    car1.next_speed = 5
    car1.t_max_speed_acc = 4
    car1.t_null_speed = -4
    car1.t_max_speed = 4
    car1.position = 0
    car1.tcl_index = 0
    car1.max_progress = 120
    car1.cell_progress = 30
    car1.max_speed = 8
    car1.max_position = 5
    car1.max_tcl_index = 4
    car1.lanes = 2'''

    # print(animate_string(log))