def anagram(s):

 if len(s) % 2 != 0:
   return -1

 mid = len(s) // 2

 start = sorted(s[:mid])
 end = sorted(s[mid:])

 character = {}

 for chars in start:
   character[chars] = character.get(chars, 0) +1

 for chars in end:
   if chars in character and character[chars] > 0:
     character[chars] -= 1

 return sum(character.values()) 
