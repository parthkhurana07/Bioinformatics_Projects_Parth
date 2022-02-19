def HammingDistance(p, q):
    # your code here
    h_distance= 0
    for i in range (len(p)):
        if p[i] != q[i]:
            h_distance= h_distance + 1
    return h_distance
