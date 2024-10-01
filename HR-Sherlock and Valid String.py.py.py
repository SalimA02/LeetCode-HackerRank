from collections import Counter

def isValid(s):
    freq = Counter(s)
    freq_of_freq = Counter(freq.values())
    
    if len(freq_of_freq) == 1:
        return "YES"
    elif len(freq_of_freq) == 2:
        freq1, count1 = freq_of_freq.most_common()[0]
        freq2, count2 = freq_of_freq.most_common()[1]
        
        if (count1 == 1 and (freq1 - 1 == freq2 or freq1 == 1)) or (count2 == 1 and (freq2 - 1 == freq1 or freq2 == 1)):
            return "YES"
    
    return "NO"
