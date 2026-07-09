from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sletter = defaultdict(int)
        Tletter = defaultdict(int)

        for i in range(len(s)):
            Sletter[s[i]] += 1

        for j in range(len(t)):
            Tletter[t[j]] += 1

        if Sletter == Tletter:
            return True
        else:
            return False
        