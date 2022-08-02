#!/usr/bin/env python
# coding: utf-8

# In[5]:


import torch
from torchvision import transforms
import random
from torch.utils.data import Dataset,DataLoader
import os
import numpy as np


# In[12]:


class makeDataset(Dataset):
    def __init__(self,transform=None,mode='train',alignB=False,sameTransformB=False):
        self.transform=transform
        self.mode=mode
        self.alignB=alignB
        self.sameTransformB=sameTransformB
        self.random_idxs=np.arange(1,self.__len__()+1)
        np.random.shuffle(self.random_idxs)
    def __len__(self):
        if(self.mode=='train'):
            return 3839
        else:
            return 421
    def __getitem__(self,idx):
        root=os.path.join('.','data_normalized',self.mode)
        img_fd=torch.unsqueeze(torch.tensor(np.load(os.path.join(root,'fd','{}.npy'.format(idx+1)))),dim=0)
        if self.alignB:
            img_qd=torch.unsqueeze(torch.tensor(np.load(os.path.join(root,'qd','{}.npy'.format(idx+1)))),dim=0)
        else:
            random_idx=self.random_idxs[idx]
            img_qd=torch.unsqueeze(torch.tensor(np.load(os.path.join(root,'qd','{}.npy'.format(random_idx)))),dim=0)
        if self.transform is not None:
            if self.sameTransformB:
                seed=np.random.randint(2^31)
                torch.manual_seed(seed)
                img_fd=self.transform(img_fd)
                torch.manual_seed(seed)
                img_qd=self.transform(img_qd)
            else:
                img_fd=self.transform(img_fd)
                img_qd=self.transform(img_qd)
        return (img_fd,img_qd)


# In[ ]:




