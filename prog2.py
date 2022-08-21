
maxInt = float('inf')

def shortest_walk(h, n, g):
    
    # base case
    if (h == 1):
        return g

    else:

        #even case
        if ((h % 2) == 0):
            T1 = shortest_walk(h/2, n, g)
            T2 = T1.copy()
        else:
            T1 = shortest_walk(h-1, n, g)
            T2 = g

        walk = [[maxInt for x in range(n)] for y in range(n)]
        
        for u in range(n):
            for v in range(n):
                for a in range(n):
                    if (T1[u][a]!=maxInt and T2[a][v]!=maxInt):
                        walk[u][v] = min(walk[u][v], T1[u][a] + T2[a][v])
        
        return walk

def init():

    params = list(map(int, input().split()))
    n = params[0]
    h = params[2]

    g = [[maxInt for x in range(n)] for y in range(n)]

    while True:
        try:
            line = input()
        except EOFError:
            break
        edge = list(map(int, line.split()))
        g[edge[0]-1][edge[1]-1] = edge[2]

    ret = shortest_walk(h, n, g)

    for i in range(n):
        for j in range(n):
            if (ret[i][j] == maxInt):
                print('x', end=" ")
            else:
                print(ret[i][j], end = " ")
        print()

init()