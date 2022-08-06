import torch
from torchvision import transforms
import random
from torch.utils.data import Dataset
import os
import numpy as np


class makeDataset(Dataset):
    def __init__(self,transform=None,mode='train',alignB=False,sameTransformB=False,normalize=True):
        self.transform=transform
        self.mode=mode
        self.alignB=alignB
        self.sameTransformB=sameTransformB
        self.random_idxs=np.arange(1,self.__len__()+1)
        self.normalize=normalize
        np.random.shuffle(self.random_idxs)
        self.random_idxs=list(self.random_idxs)
        self.normalizer=transforms.Normalize((0.5),(0.5))
    def __len__(self):
        if(self.mode=='train'):
            return 3839
        else:
            return 421
    def __getitem__(self,idx):
        root=os.path.join('.','data_normalized',self.mode)
        origin_root = os.path.join('.', 'data', self.mode)
        img_fd=torch.unsqueeze(torch.tensor(np.load(os.path.join(root,'fd','{}.npy'.format(idx+1)))),dim=0)
        img_fd_o = torch.unsqueeze(torch.tensor(np.load(os.path.join(origin_root,'fd','{}.npy'.format(idx + 1)))), dim=0)
        if self.alignB:
            img_qd=torch.unsqueeze(torch.tensor(np.load(os.path.join(root,'qd','{}.npy'.format(idx+1)))),dim=0)
            img_qd_o= torch.unsqueeze(torch.tensor(np.load(os.path.join(origin_root,'qd','{}.npy'.format(idx + 1)))), dim=0)
        else:
            if len(self.random_idxs)==0:
                self.random_idxs = np.arange(1, self.__len__() + 1)
                np.random.shuffle(self.random_idxs)
                self.random_idxs = list(self.random_idxs)
            random_idx=self.random_idxs.pop(0)
            img_qd=torch.unsqueeze(torch.tensor(np.load(os.path.join(root,'qd','{}.npy'.format(random_idx)))),dim=0)
            img_qd_o = torch.unsqueeze(torch.tensor(np.load(os.path.join(root, 'qd', '{}.npy'.format(random_idx)))),
                                     dim=0)

        if self.normalize:
            img_fd=self.normalizer(img_fd)
            img_qd=self.normalizer(img_qd)

        if self.transform is not None:
            if self.sameTransformB:
                seed=np.random.randint(2^31)
                torch.manual_seed(seed)
                img_fd=self.transform(img_fd)
                torch.manual_seed(seed)
                img_qd=self.transform(img_qd)

                torch.manual_seed(seed)
                img_fd_o = self.transform(img_fd_o)
                torch.manual_seed(seed)
                img_qd_o = self.transform(img_qd_o)

            else:
                seed = np.random.randint(2 ^ 31)
                seed2=np.random.randint(2 ^ 31)
                torch.manual_seed(seed)
                img_fd=self.transform(img_fd)
                torch.manual_seed(seed)
                img_fd_o=self.transform(img_fd_o)

                torch.manual_seed(seed2)
                img_qd=self.transform(img_qd)
                torch.manual_seed(seed2)
                img_qd_o = self.transform(img_qd_o)

        return (img_fd,img_qd,img_fd_o,img_qd_o)
