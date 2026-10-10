class FreqStack:
    def __init__(self):
       self.freq = {}
       self.group = {}
       self.maxFreq = 0

    def push(self, val: int) -> None:
        if val in self.freq : 
            self.freq[val] += 1 
            if self.freq[val] not in self.group:
                self.group[self.freq[val]] = []
        else : 
            self.freq[val] = 1 
            if self.freq[val] not in self.group:
                self.group[self.freq[val]] = []
        self.group[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()