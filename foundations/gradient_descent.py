class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = float(init)

        for _ in range(iterations):
            x = x - (learning_rate * (2 * x))
        
        x = round(x , 5)
        
        if x == 0:
            return 0.0
        
        elif x.is_integer():
            return int(x)
        
        else:
            return float(x)

