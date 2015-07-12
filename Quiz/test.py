def f(stuff):
    for thing in stuff:
        if thing == 'iPad':
            print "Found it"

f(["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"])	
print "***************************************"
f(("iBoy", "iGirl", "iQ", "iC","iPaid","iPad"))
print "***************************************"
f([ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ])
print "***************************************"
f(( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], ))
print "***************************************"
f("iPad")
print "***************************************"
f('iPad')
