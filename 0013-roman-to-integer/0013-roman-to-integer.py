class Solution(object):
    def romanToInt(self, s):
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for i in range(len(s)):
            if i<len(s)-1 and values[s[i]]<values[s[i+1]]:
                num -= values[s[i]]
            else:
                num += values[s[i]]
        return num