import torch
import timm
from models import UPerNet
input = torch.rand(2,3,384,384)
# print(torch.cuda.is_available())
input = input.cuda().float()

model = timm.create_model('swin_large_patch4_window12_384_in22k',pretrained=True)
decoder = UPerNet(num_class=11,fc_dim=1536)
decoder.cuda()
# model.cuda()
# output = model.forward_features(input)
# print(output.size())
output = decoder(input,segSize=384)

# print(output.size())