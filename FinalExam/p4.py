def uniqueValues(aDict):
    keys = []
    vDict = {}	
    for v in aDict.values():
	vDict[v] = vDict.get(v,0) + 1 
    
    for k1,v1 in vDict.iteritems():
	if v1 == 1 :
           for k2,v2 in aDict.iteritems():
		if k1 == v2:
		    keys.append(k2)
    return sorted(keys)


aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print uniqueValues(aDict)

aDict = {1: 1, 2: 1, 3: 1}
print uniqueValues(aDict)

