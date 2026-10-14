class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time = []
        fleet = 1
        cars = sorted(zip(position, speed), reverse=True)
        cars.sort(reverse = True)
        for position , speed in cars :
            time.append((target - position )/ speed)
        arrival_time = time[0]
        for i in range(len(time)) :
            if time[i] > arrival_time :
                fleet += 1
                arrival_time = time[i]
        return fleet
        
       
