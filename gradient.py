"""
LINEAR GRADIENT GENERATOR
Takes a list of colors (or any other kind of tuple) and an interval lengh list for generating color gradients. 

For example, for a color strip that starts at GREEN = (0, 255, 0), at 2/3 of strip is RED = (255, 0, 0), and the final color is BLUE = (0, 0, 255),
initialize de generator as g = Generator([GREEN, RED, BLUE], [2, 1]) 
and you will have a gradient with two thirds gradient between green and red ending with a linear gradient from red to blue

To retrieve a value from the gradient, use the `Gradient::get(value)` method, with `value` between 0 and 1 representing the percentage from start to the end of the gradient

For more examples, look at the other file
"""

class Gradient:
    def __init__(self, colors: list, interval_lenghts: list) -> None:
        """Create the linear gradient

        Args:
            colors (list): List of tuples, all with the same amount of components
            interval_lenghts (list): "distance" between each color. It is then normalized so that the total length is represented as one
        """
        assert len(interval_lenghts) == len(colors) - 1
        self.colors = colors        
        self.stop_positions = [0]  # end position of each interval of the gradient. The first zero is there for simplifying things later  
        total = sum(interval_lenghts)
        s = 0
        for i in interval_lenghts:
            s+=i
            self.stop_positions.append(s/total)
        
    def get(self, value) -> tuple:
        """Return the color given by the gradient

        Args:
            value (int): Length from the start of the gradient ranging from 0 to 1, with 1 being the last color of the gradient

        Returns:
            tuple: Tuple of the same dimesions of the gradient stops
        """
        assert value >= 0 and value <=1
        if value == 0: return self.colors[0]
        if value == 1: return self.colors[-1]
        
        for i in range(1, len(self.stop_positions)):
            if self.stop_positions[i] > value:
                upper = self.stop_positions[i]
                lower = self.stop_positions[i-1]
                v = (value-lower) / (upper-lower)
                return self.lin_gradient(self.colors[i-1], self.colors[i], v)
        return ()

    def lin_gradient(self, colorA, colorB, value) -> tuple:
        """Returns a color between A and B

        Args:
            colorA (tuple)
            colorB (tuple)
            value (int): Number between 0 and 1, with 0 = colorA and 1 = colorB
        """
        return tuple(colorA[i] + (colorB[i] - colorA[i]) * value for i in range(len(colorA)))
    
            