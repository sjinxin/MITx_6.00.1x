s = 'xbobboobbobbiooboboobobohobbobobobobo'
start=count=0
while True:
        start = s.find("bob", start) + 1
        if start > 0:
            count+=1
        else:
            break

print "Number of times bob occurs is:%d" % count;
