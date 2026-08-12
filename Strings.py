# Longest Common Prefix - Beat 100%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in strs[1:] :
            curr = i
            string = ""
            for j in range(len(prefix)):
                if j >= len(curr) :
                    break
                if prefix[j] == curr[j]:
                    string = string + curr[j]
                else :
                    break
            prefix = string
        return prefix

# Word Ladder
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        q = deque([(beginWord,1)])
        visited = set([beginWord])
        wordList = set(wordList)

        if endWord not in wordList :
            return 0
        while q :
            word ,steps = q.popleft()
            for i in range(len(word)) :
                for c in "abcdefghijklmnopqrstuvwxyz" :
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord :
                        return  steps +1
                    if new_word in wordList and new_word not in visited :
                        visited.add(new_word)
                        q.append((new_word,steps + 1))
        return 0
                    
# Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        if s == s[::-1]:
            return s
        if (len(s) == 1):
            return s

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if (s[i:j] == s[i:j][::-1]):
                    
                    if (len(s[i:j]) > len(longest)):
                        longest = s[i:j]
        return longest   
       

# Word Break
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp= [False] * (len(s) +1)
        dp[0] = True
        for i in range(1,len(s)+1) :
            for j in range(i) :
                if dp[j] and s[j:i] in wordDict :
                    dp[i] = True
        return dp[len(s)]
                
                
