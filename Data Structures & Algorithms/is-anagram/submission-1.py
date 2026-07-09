class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sletter = {}
        Tletter = {}

        for i in range(len(s)):
            if s[i] not in Sletter:
                Sletter[s[i]] = 1
            else:
                Sletter[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in Tletter:
                Tletter[t[j]] = 1
            else:
                Tletter[t[j]] += 1

        if Sletter == Tletter:
            return True
        else:
            return False
        