import torch.nn as nn
import torch
import torch.functional as F
# target output size of 5x7\

m = nn.AdaptiveAvgPool2d(output_size=1)

input = torch.randn( 1536)
print(torch._C._nn.adaptive_avg_pool2d(input,1))
output = m(input)
print(output.size())
# # target output size of 7x7 (square)
# m = nn.AdaptiveAvgPool2d(7)
# input = torch.randn(1, 64, 10, 9)
# output = m(input)

# # target output size of 10x7
# m = nn.AdaptiveAvgPool2d((None, 7))
# input = torch.randn(1, 64, 10, 9)
# output = m(input)