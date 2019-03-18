import numpy as np
import sys
import time
import matplotlib.pyplot as plt

bigrange = list(range(1,5000001))
big_list = np.arange(1,5000001)

print(sys.getsizeof(bigrange))
print(sys.getsizeof(big_list))
