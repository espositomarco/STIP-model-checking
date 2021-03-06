# This is a script to automatically print Trajectory Cell Lists
# initialization declarations for Nusmv.

# this import can be commented. It is used for 'mypy', a tool
# for static type checking in Python.
from typing import List, Dict
import numpy as np
 
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
 left                   right
        9  10  11  12

        13 14  15  16

            bottom


'''


paths_dict2 = {} #type: Dict[str, List[int]]
paths_dict2_int = {} #type: Dict[str, List[int]]
paths_dict2['2_BOTTOM_BOTTOM'] = [0,0,0,0,5]
paths_dict2['2_TOP_TOP'] = [0,0,0,0,5]
paths_dict2['2_RIGHT_RIGHT'] = [0,0,0,0,5]
paths_dict2['2_LEFT_LEFT'] = [0,0,0,0,5]
paths_dict2['2_BOTTOM_TOP'] = [0,4, 2, 5,5]
paths_dict2['2_BOTTOM_RIGHT'] = [0,4, 5, 5,5]
paths_dict2['2_BOTTOM_LEFT'] = [0,4,2,1,5]
paths_dict2['2_TOP_BOTTOM'] =  [0,1,3,5,5]
paths_dict2['2_TOP_LEFT']  =   [0,1,5,5,5]
paths_dict2['2_TOP_RIGHT']  = [0,1,3,4,5]
paths_dict2['2_RIGHT_LEFT'] = [0,2,1,5,5]
paths_dict2['2_RIGHT_TOP'] = [0,2,5,5,5]
paths_dict2['2_RIGHT_BOTTOM'] = [0,2,1,3,5]
paths_dict2['2_LEFT_RIGHT'] = [0,3,4,5,5]
paths_dict2['2_LEFT_BOTTOM'] = [0,3,5,5,5]
paths_dict2['2_LEFT_TOP'] = [0,3,4,2,5]

paths_dict2_int['[3][3]'] = [0,0,0,0,5]
paths_dict2_int['[1][1]'] = [0,0,0,0,5]
paths_dict2_int['[2][2]'] = [0,0,0,0,5]
paths_dict2_int['[4][4]'] = [0,0,0,0,5]
paths_dict2_int['[3][1]'] = [0,4, 2, 5,5]
paths_dict2_int['[3][2]'] = [0,4, 5, 5,5]
paths_dict2_int['[3][4]'] = [0,4,2,1,5]
paths_dict2_int['[1][3]'] =  [0,1,3,5,5]
paths_dict2_int['[1][4]']  =   [0,1,5,5,5]
paths_dict2_int['[1][2]']  = [0,1,3,4,5]
paths_dict2_int['[2][4]'] = [0,2,1,5,5]
paths_dict2_int['[2][1]'] = [0,2,5,5,5]
paths_dict2_int['[2][3]'] = [0,2,1,3,5]
paths_dict2_int['[4][2]'] = [0,3,4,5,5]
paths_dict2_int['[4][3]'] = [0,3,5,5,5]
paths_dict2_int['[4][1]'] = [0,3,4,2,5]


paths_list_int = [ [None] * 4 , [None] * 4 , [None] * 4 ,[None] * 4 ]
paths_list_int[3-1][3-1] = [0,0,0,0,5]
paths_list_int[1-1][1-1] = [0,0,0,0,5]
paths_list_int[2-1][2-1] = [0,0,0,0,5]
paths_list_int[4-1][4-1] = [0,0,0,0,5]
paths_list_int[3-1][1-1] = [0,4, 2, 5,5]
paths_list_int[3-1][2-1] = [0,4, 5, 5,5]
paths_list_int[3-1][4-1] = [0,4,2,1,5]
paths_list_int[1-1][3-1] =  [0,1,3,5,5]
paths_list_int[1-1][4-1]  =   [0,1,5,5,5]
paths_list_int[1-1][2-1]  = [0,1,3,4,5]
paths_list_int[2-1][4-1] = [0,2,1,5,5]
paths_list_int[2-1][1-1] = [0,2,5,5,5]
paths_list_int[2-1][3-1] = [0,2,1,3,5]
paths_list_int[4-1][2-1] = [0,3,4,5,5]
paths_list_int[4-1][3-1] = [0,3,5,5,5]
paths_list_int[4-1][1-1] = [0,3,4,2,5]

paths_dict4 = {} #type: Dict[str, List[int]]
paths_dict4['4_2_2'] = [0,0,0,0,0,0,17]
paths_dict4['4_0_0'] = [0,0,0,0,0,0,17]
paths_dict4['4_1_1'] = [0,0,0,0,0,0,17]
paths_dict4['4_3_3'] = [0,0,0,0,0,0,17]
paths_dict4['4_2_0'] = [0,16,12,8,4,17,17]
paths_dict4['4_2_1'] = [0,16,17,17,17,17,17]
paths_dict4['4_2_3'] = [0,15,11,7,6,5,17]
paths_dict4['4_0_2'] = [0,1,5,9,13,17,17]
paths_dict4['4_0_3'] = [0,1,17,17,17,17,17]
paths_dict4['4_0_1'] = [0,2,6,10,11,12,17]
paths_dict4['4_1_3'] = [0,4,3,2,1,17,17]
paths_dict4['4_1_0'] = [0,4,17,17,17,17,17]
paths_dict4['4_1_2'] = [0,8,7,6,10,14,17]
paths_dict4['4_3_1'] = [0,13,14,15,16,17,17]
paths_dict4['4_3_2'] = [0,13,0,0,0,0,17]
paths_dict4['4_3_0'] = [0,9,19,11,7,3,17]

def print_tcl_initialization_2x2():
    for i in range(0,5):
        init = 'init(tcl['+str(i)+']) := case'
        print(init)
        for name,path in paths_dict2.items():
            lanes,from_symbol, to_symbol = name.split('_')
            print('\tfrom = '+from_symbol+' & '+'to = '+ to_symbol+' : '+str(path[i])+';')
        print('esac;')


def print_tcl_initialization_4x4():
    for i in range(0,len(paths_dict4['4_2_2'])):
        init = 'init(tcl['+str(i)+']) := case'
        print(init)
        for name,path in paths_dict4.items():
            lanes,from_symbol, to_symbol = name.split('_')
            print('\tfrom = '+from_symbol+' & '+'to = '+ to_symbol+' : '+str(path[i])+';')
        print('esac;')

print_tcl_initialization_4x4()
exit()

def first_conflicting_index(tcl1 : List[int], tcl2 : List[int]) -> int:
	for i in range(1, len(tcl1)):
		if tcl1[i] == 5: continue
		if tcl1[i] == 0: continue
		for j in range(1, len(tcl2)):
			if tcl2[j] == 5: continue
			#print('ho00', tcl1[i], tcl2[j])
			
			if tcl1[i] == 0: continue
			if tcl2[j] == 0: continue
			if tcl1[i] == tcl2[j]:
				#print('ecco')
				return i
	return 0

# for k1, tcl1 in paths_dict2_int.items():
# 	for k2, tcl2 in paths_dict2_int.items():
# 		# print(tcl1, tcl2)
# 		print('init(conflict'+k1+k2+') := ' + str(first_conflicting_index(tcl1, tcl2)) +';')
# 		#print('init(conflict'+k1+k2+') := ' + str(first_conflicting_index(tcl1, tcl2)) +';')

conflict = np.ndarray(shape=(4,4,4,4), dtype=int)
for fro in range(4):
	for to in range(4):
		for fro2 in range(4):
			for to2 in range(4):
				conflict[fro,to,fro2,to2] = first_conflicting_index(paths_list_int[fro][to],paths_list_int[fro2][to2])

print( conflict.tolist() )


	# 	for fro2 in paths_list_int:
	# 		if fro2 == None: continue
	# 		res += '['
	# 		for tcl2 in fro2:
	# 			if tcl2 == None: continue
	# 			res += str(first_conflicting_index(tcl1, tcl2))  + ', '
	# 		res += '], '
	# 	res += '], '
	# res += '], '
				#print(first_conflicting_index(tcl1, tcl2))

print(res)



	# for k2, tcl2 in paths_dict2_int.items():
		# print(tcl1, tcl2)
		# print('init(conflict'+k1+k2+') := ' + str(first_conflicting_index(tcl1, tcl2)) +';')
		#print('init(conflict'+k1+k2+') := ' + str(first_conflicting_index(tcl1, tcl2)) +';')

#print_tcl_initialization_2x2()






