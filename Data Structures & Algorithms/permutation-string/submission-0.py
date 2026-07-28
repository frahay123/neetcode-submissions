from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        
        if s1_length > s2_length:
            return False

        for letter in s1:
            s1_dict[letter] += 1
    

        for letter in range(s1_length):
            s2_dict[s2[letter]] += 1


        if s2_dict == s1_dict:
            return True

       
        l = 0
        for r in range(s1_length, s2_length):
            s2_dict[s2[r]] += 1
            s2_dict[s2[l]] -= 1
            
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
                
            l += 1
            
            if s2_dict == s1_dict:
                return True
                
        return False