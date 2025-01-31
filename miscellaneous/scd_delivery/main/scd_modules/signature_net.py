import torch
from torch import nn


class SignatureNet1(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=96, kernel_size=(7, 7), padding=(3, 3), stride=(2, 2))
        self.bn1 = nn.BatchNorm2d(num_features=96)
        self.conv2 = nn.Conv2d(in_channels=96, out_channels=64, kernel_size=(5, 5), padding=(2, 2))
        self.bn2 = nn.BatchNorm2d(num_features=64)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(5, 5), padding=(2, 2))
        self.bn3 = nn.BatchNorm2d(num_features=64)
        self.conv4 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(1, 1))
        self.bn4 = nn.BatchNorm2d(num_features=128)

        # the size 2048 is for inputs of size 3x128x128
        self.fcn5 = nn.Linear(in_features=2048, out_features=1024)
        self.dropout5 = nn.Dropout(p=0.3)
        self.fcn6 = nn.Linear(in_features=1024, out_features=200)
        self.dropout6 = nn.Dropout(p=0.3)
        self.fcn7 = nn.Linear(in_features=200, out_features=num_classes)

    def forward(self, cnn_inputs):
        x = self.extract_features(cnn_inputs)
        x = self._classify_features(x)
        return x

    def extract_features(self, cnn_inputs):
        # Block 1
        x = self.conv1(cnn_inputs)
        x = self.bn1(x)
        x = nn.ReLU()(x)
        x = nn.MaxPool2d(2, 2)(x)

        # Block 2
        x = self.conv2(x)
        x = self.bn2(x)
        x = nn.ReLU()(x)
        x = nn.MaxPool2d(2, 2)(x)

        # Block 3
        x = self.conv3(x)
        x = self.bn3(x)
        x = nn.ReLU()(x)
        x = nn.MaxPool2d(2, 2)(x)

        # Block 4
        x = self.conv4(x)
        x = self.bn4(x)
        x = nn.ReLU()(x)
        x = nn.MaxPool2d(2, 2)(x)

        # Block 5
        x = torch.flatten(x, start_dim=1)
        x = self.fcn5(x)
        x = nn.Tanh()(x)
        x = self.dropout5(x)

        return x

    def _classify_features(self, features):
        # Block 6
        x = self.fcn6(features)
        x = nn.Tanh()(x)
        x = self.dropout6(x)

        # Block 7
        x = self.fcn7(x)
        x = nn.Softmax(dim=1)(x)

        return x
