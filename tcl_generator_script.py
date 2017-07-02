# This is a script to automatically print Trajectory Cell Lists
# initialization declarations for Nusmv.

# this import can be commented. It is used for 'mypy', a tool
# for static type checking in Python.
# from typing import List, Dict

paths_dict2 = {} #type: Dict[str, List[int]]
paths_dict2['2_BOTTOM_BOTTOM'] = [0,0,0]
paths_dict2['2_TOP_TOP'] = [0,0,0]
paths_dict2['2_RIGHT_RIGHT'] = [0,0,0]
paths_dict2['2_LEFT_LEFT'] = [0,0,0]
paths_dict2['2_BOTTOM_TOP'] = [4, 2, 0]
paths_dict2['2_BOTTOM_RIGHT'] = [4, 0, 0]
paths_dict2['2_BOTTOM_LEFT'] = [4,2,1]
paths_dict2['2_TOP_BOTTOM'] =  [1,3,0]
paths_dict2['2_TOP_LEFT']  =   [1,0,0]
paths_dict2['2_TOP_RIGHT']  = [1,3,4]
paths_dict2['2_RIGHT_LEFT'] = [2,1,0]
paths_dict2['2_RIGHT_TOP'] = [2,0,0]
paths_dict2['2_RIGHT_BOTTOM'] = [2,1,3]
paths_dict2['2_LEFT_RIGHT'] = [3,4,0]
paths_dict2['2_LEFT_BOTTOM'] = [3,0,0]
paths_dict2['2_LEFT_TOP'] = [3,4,2]


paths_dict4 = {} #type: Dict[str, List[int]]
paths_dict4['4_BOTTOM_BOTTOM'] = [0,0,0,0,0]
paths_dict4['4_TOP_TOP'] =       [0,0,0,0,0]
paths_dict4['4_RIGHT_RIGHT'] =   [0,0,0,0,0]
paths_dict4['4_LEFT_LEFT'] =     [0,0,0,0,0]
paths_dict4['4_BOTTOM_TOP'] =    [16,12,8,4,0]
paths_dict4['4_BOTTOM_RIGHT'] =  [16,0,0,0,0]
paths_dict4['4_BOTTOM_LEFT'] =   [15,11,7,6,5]
paths_dict4['4_TOP_BOTTOM'] =    [1,5,9,13,0]
paths_dict4['4_TOP_LEFT']  =     [1,0,0,0,0]
paths_dict4['4_TOP_RIGHT']  =    [2,6,10,11,12]
paths_dict4['4_RIGHT_LEFT'] =    [4,3,2,1,0]
paths_dict4['4_RIGHT_TOP'] =     [4,0,0,0,0]
paths_dict4['4_RIGHT_BOTTOM'] =  [8,7,6,10,14]
paths_dict4['4_LEFT_RIGHT'] =    [13,14,15,16,0]
paths_dict4['4_LEFT_BOTTOM'] =   [13,0,0,0,0]
paths_dict4['4_LEFT_TOP'] =      [9,19,11,7,3]

def print_tcl_initialization_2x2():
    for i in range(0,3):
        init = 'init(tcl['+str(i)+']) := case'
        print(init)
        for name,path in paths_dict2.items():
            lanes,from_symbol, to_symbol = name.split('_')
            print('\tfrom = '+from_symbol+' & '+'to = '+ to_symbol+' : '+str(path[i])+';')
        print('esac;')


def print_tcl_initialization_4x4():
    for i in range(0,5):
        init = 'init(tcl['+str(i)+']) := case'
        print(init)
        for name,path in paths_dict4.items():
            lanes,from_symbol, to_symbol = name.split('_')
            print('\tfrom = '+from_symbol+' & '+'to = '+ to_symbol+' : '+str(path[i])+';')
        print('esac;')


print_tcl_initialization_4x4()

 
'''
- 2x2 intersection cells:

         top

        1   2
  left          right
        3   4
     
        bottom




- 4x4 intersection cells:

             top

        1   2   3   4

        5   6   7   8
left                    right
        9  10  11  12

        13 14  15  16

            bottom


'''





