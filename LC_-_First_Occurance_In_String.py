class Solution(object):
    def strStr(self, haystack, needle):
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i+needle_length] == needle:
                return i
        return -1
