def binaryGap(self, n):
    binary_representation = bin(n)[2:] 
    zero_sequences = binary_representation.split('1')  
  
    if len(zero_sequences) <= 2:
          return 0  
      
    longest_sequence = max(len(seq) for seq in zero_sequences[1:-1])
    return longest_sequence + 1
  
# My approach finds the longest "0" sequence within "1"s and adds 1 to account for the extra step
