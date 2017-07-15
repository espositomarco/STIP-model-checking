# Usage of preprocess.py (Python3 required):
# > python preprocess.py filename.smv

import sys
from precomputed_code import tcl_initialization2x2
from typing import Iterable, List

speed = [None] * 5


def range_string(text : str) -> Iterable[int] :
    start, end = text.split('..')
    return range(eval(start), eval(end)+1)

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
    insert_string = eval(insert_name.strip())
    message = '-- Code generated as <insert_string> (preprocess.py)\n'
    return message, insert_string


def process_body_eval(body: str) -> str:
    eval_body = eval(body.strip())
    message = '-- Code generated as <eval_python> (preprocess.py)\n'
    return message, str(eval_body)


def process_body_exec(body: str) -> str:
    exec_body = exec(body.strip())
    message = '-- Code generated as <exec_python> (preprocess.py)\n'
    return message, ''


def process_body_if(command: str, body : str) -> str:
    message = '-- Code generated as <if> (preprocess.py)\n'
    if eval(command[2:].strip()):
        return message, body
    return message, ''


def process_body_define(body: str) -> str:
    var, val = body.strip().split('=')
    exec_body = exec('global ' + var + ';' + body.strip())
    message = '-- Code generated as <exec_python> (preprocess.py)\n'
    return message, '' #var + ' := ' + val + ';'


def process_body_list(command, body: str) -> str:
    for_str, varname, in_str, range_str = command.split(' ')
    assert(in_str == 'in')
    result = ''
    # print('cmon0', text)
    lines = body.splitlines()
    for i in range_string(range_str):
        # for line in lines:
            # print(line)
        result += body.strip().replace(varname, str(i)) + ', '

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
        return process_body_eval(body)
    if command.startswith('if'):
        return process_body_if(command, body)
    if command == '':
        return process_body_eval(body)
    if command == 'exec':
        return process_body_exec(body)
    if command == 'define':
        return process_body_define(body)

    try:
        return eval(command)
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


if __name__ == '__main__':

    speed[1] = 10
    speed[2] = 14
    speed[3] = 5
    speed[4] = 10

    input_name = sys.argv[1]
    output_name = input_name.replace('.', '_processed.')
    
    with open(input_name, 'r') as input_file:
        out_text = preprocess(input_file.read(), sys.argv[2:])

    with open(output_name, 'w') as output_file:
        output_file.write(out_text)
