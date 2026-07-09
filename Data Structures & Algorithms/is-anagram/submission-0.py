class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lists = {}
        for i in range(len(s)):
            if s[i] not in lists:
                lists[s[i]] = 1
            else:
                lists[s[i]] += 1
        for i in range(len(t)):
            if t[i] in lists and lists[t[i]] > 0:
                lists[t[i]] -= 1
            else:
                return False
        return True
        
