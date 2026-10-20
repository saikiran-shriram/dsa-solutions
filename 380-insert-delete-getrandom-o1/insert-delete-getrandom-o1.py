class RandomizedSet:
    import random 
    def __init__(self):
        self.RandomizedSet = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.RandomizedSet.keys() :
            return False
        else :
            self.RandomizedSet[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.nums :
            return False
        last = self.nums[-1]
        self.nums[self.nums.index(val)] = last
        self.RandomizedSet[last] -= 1
        del self.RandomizedSet[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        v = random.randint(0,len(self.nums)-1)
        return self.nums[v]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()