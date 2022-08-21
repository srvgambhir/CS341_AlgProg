import queue

# class to store info on each trail
class Trail:
    def __init__(self, id, d, h):
        self.id = id
        self.d = d
        self.h = h

# produce optimal schedule
def schedule(trails):

    # sort by due date in non-increasing order
    trails.sort(key=lambda Trail: Trail.d, reverse=True)
    
    sched = []
    pq = queue.PriorityQueue()

    for i in range(0,n):
        if i < n-1:
            free_days = trails[i].d - trails[i+1].d
        else:
            free_days = trails[i].d
        
        pq.put(((-trails[i].h, trails[i].id), trails[i]))

        while free_days > 0 and not(pq.empty()):
            sched.append(pq.get()[1])
            free_days -= 1
    
    # sort by due date in non-decreasing order
    sched.sort(key=lambda Trail: Trail.d)

    l = len(sched)
    final = []
    total_h = 0
    
    for i in range(0,n):
        if i < l:
            total_h += sched[i].h
            final.append(sched[i].id)
        else:
            final.append(-1)
    
    # print total happiness and final schedule
    print(total_h)
    print(*final)
    
# read in input
n = int(input())
due = list(map(int, input().split()))
happiness = list(map(int, input().split()))

trails = []

# create list of trail objects
for i in range(0,n):
    t = Trail(i+1, due[i], happiness[i])
    trails.append(t)

schedule(trails)