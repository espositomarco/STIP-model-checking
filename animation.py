# from graphics import *

positions = [None] * 3
speeds = [None] * 3
positions[0] = 5
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



if __name__ == '__main__':
    # size = 100
    # win = GraphWin("My Circle", size, size, autoflush=False)
    # for i in positions:
    #     c = Circle(xy_position_index(0, 100), 10)
    #     win.addItem(c)

    with open('log.txt') as log:
        text = log.read()

    states = text.split('State:')
    states = states[1:]

    print('\n state    positions        speeds' )

    for i,state in enumerate(states):
        lines = state.splitlines()
        something_changed = False
        for line in lines:
            if 'crash = TRUE' in line:
                print('crash : ' + line.strip() )
            if '.position' in line:
                something_changed = True
                car, pos = line.strip().split('=')
                name, _ = car.split('.')
                positions[eval(name[3:]) - 1] = eval(pos)
            if '.speed' in line:
                something_changed = True
                car, speed = line.strip().split('=')
                name, _ = car.split('.')
                speeds[eval(name[3:]) - 1] = eval(speed)
        
        if something_changed:
            print(str(i),':', str(positions) + ' ' + str(speeds) )
                # print(i, '\t'+line.strip())
        
        # if something_changed:
            # for i in range(len(win.items)):
                # print(i, len(win.items))
            #     pos = positions[i]
            #     win.items[i] = Circle(xy_position_index(pos, 100), 10)
            # win.redraw()
            # win.getMouse() # Pause to view result


    # win.close()    # Close window when done



