class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        for car in cars:
            hours_to_target = (target - car[0]) / car[1]
            if not stack or stack[-1] < hours_to_target:
                stack.append(hours_to_target)
        
        return len(stack)