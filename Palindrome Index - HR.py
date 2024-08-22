def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    n = len(s)
    if is_palindrome(s):
        return -1

    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]:
            if is_palindrome(s[i+1:j+1]):
                return i
            elif is_palindrome(s[i:j]):
                return j
            else:
                return -1
        i += 1
        j -= 1
    return -1
