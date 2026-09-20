class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = (len(s)+1) * [False]
        dp[0]= True
        for i in range(len(s)+1) :
            for j in range(i):
                if s[j:i] in wordDict and dp[j] == True :
                    dp[i] = True
        return dp[-1]
