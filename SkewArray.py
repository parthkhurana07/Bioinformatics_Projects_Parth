def SkewArray(Genome):
    Skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew
