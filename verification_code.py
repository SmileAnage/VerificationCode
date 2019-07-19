"""
随机生成函数
"""

import random

random_list = []

# 特殊字符a[0]
random_list.append([chr(i) for i in range(33, 48)])
# 数字a[1]
random_list.append([chr(i) for i in range(48, 58)])
# 特殊字符a[2]
random_list.append([chr(i) for i in range(58, 65)])
# 大写字母a[3]
random_list.append([chr(i) for i in range(65, 91)])
# 特殊字符a[4]
random_list.append([chr(i) for i in range(91, 97)])
# 小写字母a[5]
random_list.append([chr(i) for i in range(97, 123)])

a = [i for i in random_list]
print(a)

# 随机验证码(6位字母)
print(''.join(random.sample(a[3] + a[5], 6)))
# 随机验证码(6位字母+数字)
print(''.join(random.sample(a[3] + a[5] + a[1], 6)))
# 随机验证码(4位数字)
print(''.join(random.sample(a[1], 4)))
# 随机验证码(4位数字+字母)
print(''.join(random.sample(a[3] + a[5] + a[1], 4)))
# 随机字符(8位)
print(''.join(random.sample(a[0] + a[2] + a[4], 8)))
