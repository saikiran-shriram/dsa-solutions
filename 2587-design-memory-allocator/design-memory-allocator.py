class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        
    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)) :
            if self.memory[i] == 0 :
                count += 1
                if count == size :
                    start = i-size + 1
                    for j in range(start,start + size) :
                        self.memory[j] = mID
                    return start
            else :
                count= 0
        return -1
            
    def freeMemory(self, mID: int) -> int:
        rel_count = 0
        for i in range(len(self.memory)) :
            if self.memory[i] == mID :
                self.memory[i]= 0 
                rel_count += 1
        return rel_count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)