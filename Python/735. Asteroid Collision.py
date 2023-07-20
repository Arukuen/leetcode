def asteroidCollision(asteroids: list[int]) -> list[int]:
    while True:
        exploded_index= []
        for i in range(len(asteroids) - 1):
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if abs(asteroids[i]) > abs(asteroids[i+1]): 
                    exploded_index.append(i+1)
                elif abs(asteroids[i]) < abs(asteroids[i+1]): 
                    exploded_index.append(i)
                else:
                    exploded_index.append(i)
                    exploded_index.append(i+1)
        
        for i, index in enumerate(exploded_index):
            asteroids.pop(index - i)

        if len(exploded_index) == 0:
            return asteroids
        
print(asteroidCollision([10,2,-5]))
                