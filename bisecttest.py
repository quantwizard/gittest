
import bisect
import random
random.seed(1)
print('New pos contents')
print('-----------------')
l=[]
 
for i in range(1,15):
    r=random.randint(1,100)
    #bisect_left only get position of the list, do not operate the list at all
    #if r exist get the postition of r, if not, get the insert position if r insert in the list
    position=bisect.bisect_left(l,r)

    # insort_left insert and sort the data in the list
    bisect.insort_left(l,r)
    print '%3d %3d'%(r,position),l
