class RandomizedSet:
    import random
    def __init__(self):
        self.dict = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.dict :
            return False
        self.nums.append(val)
        self.dict[val] = len(self.nums) - 1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.dict :
            return False
        i = self.dict[val]
        self.nums[i] = self.nums[-1]
        self.dict[self.nums[-1]] = i
        self.nums.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums) - 1)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()