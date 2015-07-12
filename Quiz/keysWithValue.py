def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    l = []
    for key in aDict.keys():
	if aDict.get(key,0) == target:
		l.append(key)
    return sorted(l)
