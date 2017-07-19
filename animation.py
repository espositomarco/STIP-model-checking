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




def animate_log(log_filename = 'log.txt') -> str:
    # size = 100
    # win = GraphWin("My Circle", size, size, autoflush=False)
    # for i in positions:
    #     c = Circle(xy_position_index(0, 100), 10)
    #     win.addItem(c)
    positions = [None] * 4
    speeds = [None] * 4
    positions[0] = 5

    output = ''

    with open(log_filename) as log:
        text = log.read()

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



if __name__ == '__main__':
    print(animate_log())

