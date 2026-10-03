class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet = 1
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        time = []
        for position,speed in cars:
            time.append((target - position) / speed)
        arrival_time = time[0]
        for i in range(1 ,len(time)):
            if time[i] > arrival_time :
                fleet += 1
                arrival_time = time[i]
        return fleet
       
