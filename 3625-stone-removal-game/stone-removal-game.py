class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        remove = 10
        alice_turn = True
        while n : 
            if n < remove : 
                if not alice_turn : 
                    return True 
                else : 
                    return False
            n -= remove
            remove -= 1
            alice_turn = not alice_turn
        return True if not alice_turn else False