# import os
# print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
# print("PATH:", os.environ.get('PATH'))

import numpy as np
def square_root_array(arr):
    return np.sqrt(arr)

# Example usage
numbers = [4, 9, 16, 25]
result = square_root_array(numbers)
print(result)