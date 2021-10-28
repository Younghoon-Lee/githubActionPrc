import torch
from collections import OrderedDict

model = torch.load('./iter_22000.pth')
print(len(model['state_dict']))
model2 = torch.load('./iter_23000.pth')
model3 = torch.load('./iter_24000.pth')
model4 = torch.load('./iter_25000.pth')
model5 = torch.load('./best_mIoU_iter_20000.pth')
temp2 = model2['state_dict']
temp = model['state_dict']
temp3 = model3['state_dict']
temp4 = model4['state_dict']
temp5 = model5['state_dict']

result = OrderedDict()

# print(model['state_dict'].keys())
for k, v in temp.items():
    result[k] = (temp[k] + temp2[k] + temp3[k] + temp4[k]+ temp5[k])/5.0

model5['state_dict'] = result
torch.save(model5,'SWA.pth')
# print(result)
# print(temp)
# sum = Counter(model['state_dict']) + Counter(model2['state_dict'])
# result = dict(sum)
# print(len(result))