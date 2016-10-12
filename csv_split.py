import os
import csv
import argparse
import sys
import re

def argument_parser():
	parser = argparse.ArgumentParser(description="Splitting CSV with input file, output file and row limits")
	parser.add_argument("-i", "--input", help="Input File Name", type=str, required=True)
	parser.add_argument("-o", "--output", help="Output File Name", type=str, required=True)
	parser.add_argument("-r", "--row_limit", help="Row Limit", type=int, required=True)
	args = parser.parse_args()
	is_valid_input_file(args.input)
	is_valid_row_limit(args.input, args.row_limit)
	return args.input, args.output, args.row_limit
	
def is_valid_input_file(input):
	if os.path.isfile(input):
		pass
	else:
		sys.exit(1)
		
def is_valid_row_limit(input, row_limit):
	file_len = 0
	with open (input, "r") as my_inp:
		inp = csv.reader(my_inp)
		file_len = sum (1 for i in inp)
	if file_len > row_limit:
		pass
	else:
		sys.exit(2)

def split_csv(argument):
	current_dir = "."
	input = argument[0]
	output = argument[1]
	row_limit = argument[2]
	rows = []
	with open(input, "r") as my_inp:
		inp = csv.reader(my_inp)
		for i in inp:
			rows.append(i)
	header = rows.pop(0)
	chunk = []
	count = 0
	for i in range(0, len(rows), row_limit):
		chunk = rows[i:i + row_limit]
		chunk.insert(0, header)
		output_file = os.path.join(current_dir, re.sub(r'\.',str(count)+'.',output))
		print (output_file)
		with open(output_file, "w") as my_out:
			out = csv.writer(my_out)
			out.writerows(chunk)
		count += 1
		
		print ()
		print ("output file = ", output_file)
		print ("no of rows =", len(chunk))
		
if __name__ == "__main__":
	argument = argument_parser()
	print (argument)
	split_csv(argument)
	
	
