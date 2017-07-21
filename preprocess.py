# Usage of preprocess.py (Python3 required):
# > python preprocess.py filename.smv

import sys
import os
import animation
from collections import namedtuple
from precomputed_code import tcl_initialization2x2, sqrt_init
from typing import Iterable, List

Settings = namedtuple('Settings', 'lanes max_tcl_index speed num_cars max_speed from_dir to_dir acc_param dec_param max_time cell_progress')


def int_direction(direction: str) -> int:
    if direction == 'TOP': return 0
    if direction == 'RIGHT': return 1
    if direction == 'BOTTOM': return 2
    if direction == 'LEFT': return 3


def int_direction_list(directions: List[str]) -> List[int]:
    return [int_direction(x) for x in directions ]


lanes = 2
max_tcl_index = lanes + 2
speed = [8, 4]
num_cars = 2
max_speed = 8
from_dir = int_direction_list(['RIGHT', 'BOTTOM'])
to_dir   = int_direction_list(['BOTTOM'   , 'LEFT'])
acc_param = 1
dec_param = -1
max_time = 50
cell_progress = 30;


def my_eval(expr: str):
    try:
        return eval(expr)
    except:
        print('EVAL ERROR:', expr)
        exit()
        return None



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
    # print(list_str)
    # print(list_str.split('(') )
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
    global to_dir
    # print(speed)
    # print(num_cars)
    # print(max_speed)
    speed = speeds_in[:]
    from_dir = [ int_direction(x) for x in from_in]
    to_dir = to_in[:]
    num_cars = len(speeds_in)
    max_speed = 8
    # print(speed)
    # print(num_cars)
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


def compile_NuSMV(filename: str, logfile: str = 'log.txt'):
    command = "time /Users/giacomo/dev/NuSMV-2.6.0-Darwin/bin/NuSMV " + filename + " > " + logfile
    print('compiling NuSMV model:', command)
    os.system(command)


def write_processed_model(model_name: str, settings) -> str:
    setup_model(settings)
    with open(model_name + '.smv', 'r') as file:
        model = file.read()
    model = preprocess(model)

    out_model_name = model_name + '_processed.smv'
    with open(out_model_name, 'w') as file:
        file.write(model)

    return out_model_name


def setup_model(settings):
    global lanes, from_dir, to_dir, max_tcl_index, speed, num_cars, max_speed, acc_param, dec_param, max_time, cell_progress
    lanes = settings.lanes
    from_dir = int_direction_list(settings.from_dir)
    to_dir = int_direction_list(settings.to_dir)
    max_tcl_index = settings.max_tcl_index
    speed = settings.speed
    num_cars = settings.num_cars
    max_speed = settings.max_speed
    acc_param = settings.acc_param
    dec_param = settings.dec_param
    max_time = settings.max_time
    cell_progress = settings.cell_progress


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
