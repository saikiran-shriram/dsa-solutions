class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month - 1]) + day
        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))
        return max(0, end - start + 1)



        # from datetime import datetime
        # d1 = datetime.strptime(arriveAlice, "%m-%d")
        # d2 = datetime.strptime(arriveBob, "%m-%d")
        # diff = abs((d2 - d1).days)
        # if diff <=