def clean(s):
    """
    This function takes the string input from the HTML text area 
    field and converts those entries into a list of integers which
    will be used to intialize the matrices.
    """
    temp = s.split()
    for i in range(0, len(temp)):
        temp[i] = int(temp[i])
    return temp
