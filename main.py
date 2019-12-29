from ttlru import TTLRU
import time

#Contain 10 items with ttl 5 min
l = TTLRU(10, ttl=300*1000000000)

l[0]="pen"
l[1]="pencil"
l[2]="book"
l[3]="note-book"
l[4]="color-pen"
l[5]="pin"
l[6]="cover-page"
l[7]="ruler"
l[8]="fountain-pen"
l[9]="paper-weight"

#get values
print(l.items())

time.sleep(300)

#item expire

#get keys and values

length = l.get_size()

for i in length:
    print("key:"+str(l.keys())+" value:"+l.values()+" ",end="")

# add an item with specified ttl, in this case it's 100 seconds
l.set_with_ttl(1, 'school-dress', 100*1000000000)