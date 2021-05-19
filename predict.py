from train import Net
from PIL import Image
import numpy as np
import glob
import torch
import torch.nn.functional as F



weights = glob.glob("models/*.pth")
if len(weights) == 0:
    raise IOError("Could not find any model")
print(f"Found {len(weights)} models, using {weights[0]}")

model = Net()
model.load_state_dict(torch.load(weights[0]))


def predict(file_path):
    
    img = np.array(Image.open(file_path).resize(size=(28, 28)))
    img = img.reshape(1, 1, 28, 28)
    img = img.astype('float32')
    img = img / 255.0
    digit = F.softmax(model(torch.from_numpy(img)), dim=1)
    return str(int(digit[0].argmax()+1))


if __name__ == "__main__":
    
    print(predict("./301.png"))