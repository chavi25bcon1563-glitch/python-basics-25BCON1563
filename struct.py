#!/usr/bin/env python3
"""
Module Name: Circle Tool
Description: A simple script to calculate area, demonstrating basic Python structure.
"""

# 1. Imports
import math

# 2. Global Constants
PI_VALUE = math.pi

# 3. Function Definitions
def calculate_area(radius):
    """Calculates the area of a circle given its radius."""
    if radius < 0:
        return "Radius cannot be negative"
    
    area = PI_VALUE * (radius ** 2)
    return area

# 4. Main Program Execution
if __name__ == "__main__":
    # Code inside this block runs directly
    user_radius = 5.0
    result = calculate_area(user_radius)
    
    print(f"The area of a circle with radius {user_radius} is: {result}")
