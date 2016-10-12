import sys, getopt, argparse, os, csv

parser = argparse.ArgumentParser(description='This script needs and input , output file and no. of rows to split the input file')
parser.add_argument('-i', '--input', help = 'Input file name', required = True)
parser.add_argument('-o', '--output', help = 'Output file name', required = True)
parser.add_argument('-r', '--row', help = 'No. of rows to split the file', required = True)
args = parser.parse_args()
print ("args = ", args)
print ("Input file: {}".format(args.input))
print ("Output file: {}".format(args.output))
print ("Rows: {}".format(args.row))

if not os.path.exists(args.input):
	print ("Input file doesn't exists")
	sys.exit(2)
	
with open(args.input, "r") as my_inp:
	file_len = sum (1 for _ in csv.reader(my_inp))
	if file_len < int(args.row):
		print ("file len is smaller then no. of rows to split the file")
		sys.exit(2)
	else:
		print ("file len is greater than no. of rows")
count = 0
rows = []
chunk = []
header = []
with open(args.input, "r") as my_inp:
	print ("file length type:" , type(file_len))
	inp = csv.reader(my_inp)
	header.append(next(inp))
	for i in inp:
		count += 1
		print (count)
		print (file_len)
		rows.append(i)
		
		if not count % int(args.row):
			print (rows)
			print (count)
			chunk.append(rows)
			rows = []
			
		if count == file_len - 1:
			print (rows)
			print (count)
			chunk.append(rows)
			rows = []
	print (len(chunk))
	
	
	

count = 0
for i in chunk:
	count += 1
	with open(args.output+str(count), "w") as my_out:
		out = csv.writer(my_out)
		out.writerows(header)
		out.writerows(i)

for i in range(len(chunk)):
	print ("{} has {} chunks".format(args.output+str(i), i*int(args.row)))
# try:
	# opts, args = getopt.getopt(sys.argv[1:], "i:o:")
# except getopt.GetoptError as e:
	# print (e)
	# print ("Usage: {} -i inputfile -o outputfile".format(sys.argv[0]))
	# sys.exit(2)
	
# for o,a in opts:
	# if o == "-i":
		# input = a
	# elif o == "-o":
		# output = a
		
# print ("Input file: {} and output file: {}".format(input, output))