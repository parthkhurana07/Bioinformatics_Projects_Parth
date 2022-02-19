def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern
    

def Reverse(Pattern):
    reversed_pattern= Pattern[::-1]
    return reversed_pattern
    

def Complement(Pattern):
    basepairs= {"A":"T", "G":"C", "T":"A","C":"G"}
    Complement=""
    for base in Pattern:
        Complement += basepairs.get(base)
    return Complement
