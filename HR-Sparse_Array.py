def matchingStrings(strings, queries):
    
    length = len(queries)
    output = [0] * length
    for i in range(length):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                output[i] += 1
                
    return output
                
