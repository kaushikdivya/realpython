cats_with_hat=[]
total = 0
cats = []
for gap in range(1,101):

	for cat in range(0,100,gap):
		if len(cats_with_hat) < 100:
			
			cats_with_hat.append(1)
		elif cats_with_hat[cat] == 1:
			cats_with_hat[cat] = 0
		else:
			cats_with_hat[cat] = 1
	

for i in range(0,100):
	if cats_with_hat[i] == 1:
		cats.append(i)
		
print (cats)