class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        current = []
        result = []
        if digits == '':
            return []
        phone = {'2':'abc', '3':'def', '4':'ghi' , '5':'jkl' , '6':'mno' , '7':'pqrs' ,'8':'tuv' , '9':'wxyz'}
        def fun(index, current) :
            if index == len(digits) :
                current  = ''.join(current)
                result.append(current)
                return
            for value in phone[digits[index]] :
                current.append(value)
                fun(index +1 ,current)
                current.pop()
            return result
        return fun(0,current)
