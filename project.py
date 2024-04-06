# Importing the Libraries
import torch 
from torch import nn 
import matplotlib.pyplot as plt
from keras.datasets import mnist
torch.manual_seed(42)

(train_image, train_label) , (test_image, test_label) = mnist.load_data()

plt.imshow(train_image[0])



