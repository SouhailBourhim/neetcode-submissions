class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m :
            return False
        S_count = {}
        T_count = {}
        for c in s:
            S_count[c] = S_count.get(c,0) + 1
        for d in t:    
            T_count[d] = T_count.get(d,0) + 1
        return True if S_count == T_count else False
