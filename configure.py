from pathlib import Path

import torch
from torch import optim, nn

from signature_net.cnn_models import AutoEncoder


class Configure(object):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_data = r'D:\Data\INCIBE_dataset\train'
    test_data = r'D:\Data\INCIBE_dataset\test'

    runtime_dir = Path('./runtime_dir')
    signet_dir = runtime_dir

    runtime_dir.mkdir(exist_ok=True, parents=True)
    signet_dir.mkdir(exist_ok=True, parents=True)


class SigNet(object):
    name = 'signature_net'
    model = AutoEncoder().to(Configure.device)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    scheduler = optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.95, last_epoch=-1)
    epochs = 1
