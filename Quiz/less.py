def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    l = []
    for c in aList:
	if len(c) < 4:
		l.append(c)
    return l
