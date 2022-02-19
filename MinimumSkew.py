def MinimumSkew(Genome):
    positions = [] # output variable
    count= 0
    array= SkewArray(Genome)
    minarray= min(array)
    for i in array:
        if i==minarray:
            positions.append(count)
        count= count+1
    return positions


def SkewArray(Genome):
    Skew = [0] # output variable
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew
