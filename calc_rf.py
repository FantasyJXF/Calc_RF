import numpy as np

convs = [{'f':4, 's':2, 'd':1}, {'f':4, 's':2, 'd':1}, {'f':4, 's':2, 'd':2}, {'f':4, 's':2, 'd':2}, {'f':5, 's':2, 'd':2}]

def calc_rf(dt):
    l = [1]
    for i in range(len(dt)):
        si = np.prod([x['s'] for x in dt[:i]])
        li = l[i] + (dt[i]['d']*(dt[i]['f'] - 1)) * si
        l.append(li)
        print("The receptive field of layer%d is %d" %(i+1, li))

calc_rf(convs)
