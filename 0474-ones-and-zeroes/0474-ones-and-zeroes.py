class Solution(object):
    def findMaxForm(self, strs, m, n):
        def dfs(i,z,o):
            if i==len(strs):
                return 0
            zc=strs[i].count('0')
            oc=strs[i].count('1')
            res=dfs(i+1,z,o)
            if z>=zc and o>=oc:
                res=max(res,1+dfs(i+1,z-zc,o-oc))
            return res
        return dfs(0,m,n)