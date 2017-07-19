# Usage of preprocess.py (Python3 required):
# > python preprocess.py filename.smv

import sys
import os
import animation
from precomputed_code import tcl_initialization2x2, sqrt_init
from typing import Iterable, List

lanes = 2
max_tcl_index = lanes + 2
speed = [5, 8]
num_cars = 2
max_speed = 8
from_dir = [3, 4] #['BOTTOM', 'LEFT'   ]
to_dir   = [1, 3] #['TOP'   , 'BOTTOM' ]

throttle = 1
brake = -3

def my_eval(expr: str):
    try:
        return eval(expr)
    except:
        print('EVAL ERROR:', expr)
        exit()
        return None


def int_direction(direction: str) -> int:
    if direction == 'TOP': return 1
    if direction == 'RIGHT': return 2
    if direction == 'BOTTOM': return 3
    if direction == 'LEFT': return 4


def range_string(text : str) -> Iterable[int] :
    start, end = text.split('..')
    return range(my_eval(start), my_eval(end)+1)

def process_body_for(command: str, text : str) -> str :
    for_str, varname, in_str, range_str = command.split(' ')
    assert(in_str == 'in')
    result = ''
    # print('cmon0', text)
    lines = text.splitlines()
    for i in range_string(range_str):
        # for line in lines:
            # print(line)
        result += text.replace(varname, str(i))

    message = '-- Code generated as <for> (preprocess.py)'
    return message, result


def process_body_insert_string(insert_name: str) -> str:
    insert_string = my_eval(insert_name.strip())
    message = '-- Code generated as <insert_string> (preprocess.py)\n'
    return message, insert_string


def process_body_my_eval(body: str) -> str:
    # print(body)
    eval_body = my_eval(body.strip())
    # print(body, eval_body)
    message = '-- Code generated as <eval_python> (preprocess.py)\n'
    return message, str(eval_body)


def process_body_exec(body: str) -> str:
    exec_body = exec(body.strip())
    message = '-- Code generated as <exec_python> (preprocess.py)\n'
    return message, ''


def process_body_if(command: str, body : str) -> str:
    message = '-- Code generated as <if> (preprocess.py)\n'
    if my_eval(command[2:].strip()):
        return message, body
    return message, ''


def process_body_define(body: str) -> str:
    var, val = body.strip().split('=')
    exec_body = exec('global ' + var + ';' + body.strip())
    message = '-- Code generated as <exec_python> (preprocess.py)\n'
    return message, '' #var + ' := ' + val + ';'


def process_body_list(command:str, body: str) -> str:
    list_str, varname, in_str, range_str = command.split(' ')
    print(list_str)
    print(list_str.split('(') )
    _, separator = list_str.split('(')
    separator = separator[:-1]
    assert(in_str == 'in')
    result = ''
    # print('cmon0', text)
    lines = body.splitlines()
    for i in range_string(range_str):
        # for line in lines:
            # print(line)
        result += body.strip().replace(varname, str(i)) + separator + ' '

    # result = result[:-2]
    message = '-- Code generated as <for> (preprocess.py)'
    return message, result[:-2]

def process_body(command : str, body : str) -> str :
    if command.startswith('for'):
        return process_body_for(command, body)
    if command.startswith('list'):
        return process_body_list(command, body)
    if command == 'insert_string':
        return process_body_insert_string(body)
    if command == 'eval':
        return process_body_my_eval(body)
    if command.startswith('if'):
        return process_body_if(command, body)
    if command == '':
        return process_body_my_eval(body)
    if command == 'exec':
        return process_body_exec(body)
    if command == 'define':
        return process_body_define(body)

    try:
        return my_eval(command)
    except:
        print('ERROR in process_body\n','commmand:', command, 'body:', body)
        assert(0)
        return 'PREPROCESS_FAILURE'


def find_closing_token(text: str, start: int, opening : str = '{', closing : str = '}') -> int:
    opening_found = 1
    closing_found = 0
    # opening_index = text.find(opening, start + 1) # +1 ???

    for i, char in enumerate(text):
        if i <= start: continue
        if char == opening:
            opening_found += 1

        if char == closing:
            closing_found += 1

        if closing_found == opening_found:
            return i

    # while last_index >= 0:
    #     opening_index = text.find(opening, opening_index + 1)
    #     opening_found += 1

    # print('opn', text[start:])

    # closing_index = start
    # while closing_index >= 0:
    #     closing_index = text.find(closing, closing_index + 1)
    #     if opening_found == 0:
    #         print('ecco', text[start:closing_index])
    #         return closing_index

    #     opening_found -= 1

    return -1


def preprocess(text : str, args : List[str] = []) -> str :
    lines = text.splitlines()
    text = ''
    for line in lines:
        if not line.strip().startswith('--'):
            text += line + '\n'

    preprocess_token = '#'
    start_token = '{'
    end_token = '}'
    preprocess_start = text.find(preprocess_token)



    while preprocess_start > 0:
        start = text.find(start_token, preprocess_start)
   
        # end = text.find(end_token, start)
        end = find_closing_token(text, start, start_token, end_token)

        if start < 0 or end < 0 or end < start:
            assert(0) 

        command = text[preprocess_start+1: start].strip()
        body = text[start+len(start_token):end]

        message, body_processed = process_body(command, body.rstrip() )
        text = text[:preprocess_start] + body_processed + text[end+len(end_token):]
        preprocess_start = text.find(preprocess_token, preprocess_start+len(start_token)+1)

    return text

def planning(speeds_in: List[int], from_in: List[str], to_in: List[str], model: str, output_name) -> str:
    # speed[1] = speed_in[0]
    # speed[2] = speed_in[1]
    # with open('animations.txt', 'a') as file:
        # file.write('SPEEDS: ' + str(v1) + ', ' + str(v2) )
    # global num_cars, max_speed, speed
    # with open(model_name, 'r') as input_file:
    global speed 
    global num_cars
    global max_speed
    global from_dir
    global TO
    # print(speed)
    # print(num_cars)
    # print(max_speed)
    speed = speeds_in[:]
    from_dir = [ int_direction(x) for x in from_in]
    to_dir = to_in[:]
    num_cars = len(speeds_in)
    max_speed = 8
    print(speed)
    print(num_cars)
    # print(max_speed)
    processed_model = preprocess(model)


    with open(output_name, 'w') as output_file:
        output_file.write(processed_model)

    command = "time /Users/giacomo/dev/NuSMV-2.6.0-Darwin/bin/NuSMV "+output_name+" > log.txt"
    print('command:', command)
    os.system(command)
    # print('tutto ok')
    anim = animation.animate_log()
    speed_stamp = 'speeds: '
    for s in speed:
        if s == None: continue
        speed_stamp += str(s) + ' '
    anim = speed_stamp + '\n' + anim
    return anim
    # # else:
    #     print('problemi!!')
        # return ''


def compile_NuSMV(output_name: str):
    command = "time /Users/giacomo/dev/NuSMV-2.6.0-Darwin/bin/NuSMV "+output_name+" > log.txt"
    print('command:', command)
    os.system(command)


if __name__ == '__main__':



    # speed[1] = 4
    # speed[2] = 0
    # speed[3] = 4
    # speed[4] = 10

    input_name = sys.argv[1]
    # max_speed = 14
    # num_cars = 2 
    
    output_name = input_name.replace('.', '_processed.')
    
    # for v1 in range(0,max_speed+1):
        # for v2 in range(0,max_speed+1):
    # for v1 in range(14, 14+1):
        # for v2 in range(5, 5+1):
    # speed[1] = v1
    # speed[2] = v2
    # with open('animations.txt', 'a') as file:
        # file.write('SPEEDS: ' + str(v1) + ', ' + str(v2) )

    with open(input_name, 'r') as input_file:
        model = input_file.read()

    with open(output_name, 'w') as output_file:
        output_file.write(preprocess(model))

    compile_NuSMV(output_name)
    # anim = animation.animate_log()
    # print(anim)
    exit()

    anim = planning([8,8,4,4],['TOP','RIGHT', 'RIGHT','LEFT'],['BOTTOM','LEFT','BOTTOM','TOP'], model, output_name)
    # print(anim)
    with open('animation_test.txt', 'a') as out:
        out.write(anim)


    
    # every combination with 2 cars.
    # for c2_from in ['BOTTOM','TOP', 'RIGHT','LEFT']:
    #     for c2_to in ['BOTTOM','TOP', 'RIGHT','LEFT']:
    #         if c2_from == c2_to: continue
    #         for c1_to in ['LEFT', 'TOP', 'RIGHT']:
    #             anim = planning([8,8],['BOTTOM', c2_from],[c1_to, c2_to], model, output_name)
    #             # print(anim)
    #             with open('animation_test.txt', 'a') as out:
    #                 out.write(anim)
