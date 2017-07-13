# Usage of preprocess.py (Python3 required):
# > python preprocess.py filename.smv

import sys
from precomputed_code import tcl_initialization2x2
from typing import Iterable

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
    return message + result


def process_body_insert_string(insert_name: str) -> str:
    insert_string = eval(insert_name.strip())
    message = '-- Code generated as <insert_string> (preprocess.py)\n'
    return message + insert_string


def process_body_eval(body: str) -> str:
    eval_body = eval(body.strip())
    message = '-- Code generated as <eval_python> (preprocess.py)\n'
    return message + str(eval_body)


def process_body(command : str, body : str) -> str :
    if command.startswith('for'):
        return process_body_for(command, body)
    if command == 'insert_string':
        return process_body_insert_string(body)
    if command == 'eval_python':
        return process_body_eval(body)

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


def preprocess(text : str) -> str :
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

        body_processed = process_body(command, body.rstrip() )
        text = text[:preprocess_start] + body_processed + text[end+len(end_token):]
        preprocess_start = text.find(preprocess_token, preprocess_start+len(start_token)+1)

    return text


if __name__ == '__main__':
    # text = "012345(0(89)sd)sffs"
    # i = find_closing_token(text, 6,'(', ')')
    # print(text[6:])
    # print(text[i:])
    # exit(0)


    input_name = sys.argv[1]
    input_file = open(input_name, 'r')

    output_name = input_name.split('.')[0] + '_processed.' + input_name.split('.')[1]
    output_file = open(output_name, 'w')
    
    input_text = input_file.read()

    out_text = preprocess(input_text)
    output_file.write(out_text)

    input_file.close()
    output_file.close()