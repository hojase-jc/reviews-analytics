data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('總共有',len(data),'筆留言')
sum_len = 0
for d in data:
	len(d)
	sum_len = sum_len + len(d)
print('平均留言長度為',sum_len/len(data))
