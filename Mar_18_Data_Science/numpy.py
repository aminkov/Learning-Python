import numpy as np
import sys

bigrange = list(range(1,5001))
big_list = np.arange(1,5001)

print(sys.getsizeof(bigrange))
print(sys.getsizeof(big_list))
