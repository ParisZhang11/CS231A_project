from depth_anything.dpt import DepthAnything
import os
import numpy as np
from PIL import Image
import torch

def indoor_metrics(img_dir, output_dir):
    model = DepthAnything.from_pretrained('LiheYoung/depth_anything_{:}14'.format('vitl'))
    model.load_state_dict('/vision/u/parisz/DepthRegularizedGS/DepthAnything/pretrained/depth_anything_metric_depth_outdoor.pt?download=true')
    model = model.to('cuda')
    img_lst = os.listdir(img_dir)
    for img in img_lst:
        img_path = os.path.join(img_dir, img)
        img = np.array(Image.open(img_path))
        img = torch.from_numpy(img).unsqueeze(0).unsqueeze(0).float()
        img = img / 255.0
        img = img.cuda()
        pred = model(img)
        pred = pred.squeeze().cpu().numpy()
        pred = (pred * 1000).astype(np.uint16)
        pred = Image.fromarray(pred)
        pred.save(os.path.join(output_dir, img))
