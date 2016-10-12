import csv
import os
import sys
my_path = "C:/Users/dk070h/Downloads/book1-exercises-master/chp09/practice_files"
high_score_dic = {}
scores_file = os.path.join(my_path, "scores.csv")
with open(scores_file, "r") as my_inp:
	my_reader = csv.reader(my_inp)
	for person, score in my_reader:
		score = int(score)
		if person in high_score_dic:
			if high_score_dic[person] > score:
				pass
			else:
				high_score_dic[person] = score
		else:
			high_score_dic[person] = score

for keys in sorted(high_score_dic):
			
	print (keys ,high_score_dic[keys])
	
print (sys.argv)