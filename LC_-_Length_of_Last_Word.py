class Solution(object):
    def lengthOfLastWord(self, s):
        
        s = s.strip()

        words = s.split()

        lastWord = words[-1]
        
        return len(lastWord) 
      

        
