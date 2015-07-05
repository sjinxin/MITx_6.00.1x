startidx=0
maxcount=0

for i in range(len(s)):
	count=0
	j = i
	while j+1 < len(s) and s[j] <= s[j+1]:
		count+=1
		j+=1

	if count > maxcount:
		maxcount = count
		startidx = i		


print "Longest substring in alphabetical order is: %s" % s[startidx:startidx+maxcount+1]

