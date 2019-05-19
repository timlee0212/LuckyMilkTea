#
# @Author: Li Shiyu 
# @Date: 2019-05-19 20:32:19 
# @Last Modified by:   Li Shiyu 
# @Last Modified time: 2019-05-19 20:32:19 
#

import numpy as np

num_people = 4
total_price = 100
mapping = {1:'zyd', 2:'spzyd', 3:'sdzyd', 4:'btzyd'}


res = np.random.rand(num_people)
res = res / np.sum(res)
#Or Using Softmax
#res = np.exp(res)/np.sum(np.exp(res))

for i in range(1, num_people):
    print(mapping[i], "\t%.2f"%(res[i-1] * total_price))