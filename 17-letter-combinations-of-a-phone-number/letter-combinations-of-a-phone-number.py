class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone ={ '2':'abc' , '3':'def' , '4':'ghi' , '5':'jkl' , '6':'mno' , '7':'pqrs' , '8':'tuv' , '9':'wxyz'}
        current = ''
        result = []
        def fun(index, current):
            if index == len(digits):
                result.append(current)
                return
            letters = phone[digits[index]]
            for i in range(len(letters)):
                current += letters[i]
                fun(index+1,current)
                current = current[:-1]
            return result
        return fun(0,current)
