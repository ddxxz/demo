import torch

x = torch.randn([10,10])

r = x @ x

print(r)

a = r * 2
1