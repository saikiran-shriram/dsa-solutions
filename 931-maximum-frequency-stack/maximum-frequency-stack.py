class FreqStack:
    def __init__(self):
       self.maxFreq = 0
       self.group = {}
       self.freq = {}

    def push(self, val: int) -> None:
        if val in self.freq :
            self.freq[val] +=1 
        else :
            self.freq[val] = 1
        self.maxFreq = max(self.maxFreq,self.freq[val])
        if self.freq[val] not in self.group:
            self.group[self.freq[val]] = []
        self.group[self.freq[val]].append(val)        

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq] :
            self.maxFreq -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()