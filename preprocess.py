import sys
from typing import Iterable

def range_string(text : str) -> Iterable[int] :
	start, end = text.split('..')
	return range(eval(start), eval(end)+1)

def process_body_for(text : str) -> str :
	lines = text.splitlines()
	_, varname, in_str, range_str = lines[0].split(' ')
	assert(in_str == 'in')
	result = ''
	for i in range_string(range_str):
		result += lines[1].replace(varname, str(i)) + '\n'

	return result


def process_body(text : str) -> str :
	if text.startswith('for'):
		return process_body_for(text)

	return text


def preprocess(text : str) -> str :
	start_token = '<'
	end_token = '>'
	start = text.find(start_token)
	while start > 0:
		end = text.find(end_token)
		body = text[start+1:end].strip()
		body_processed = process_body(body)
		text = text[:start] + body_processed.strip() + text[end+1:]
		start = text.find(start_token, start+1)

	return text


if __name__ == '__main__':
	input_name = sys.argv[1]
	input_file = open(input_name, 'r')

	output_name = input_name.split('.')[0] + '_process.' + input_name.split('.')[1]
	output_file = open(output_name, 'w')
	
	input_text = input_file.read()

	out_text = preprocess(input_text)
	output_file.write(out_text)

	input_file.close()
	output_file.close()