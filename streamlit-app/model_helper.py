from PIL import Image
from torchvision import models, transforms
from torch import nn
import torch


trained_model = None
class_name = ['Front Breakage', 'Front Crushed', 'Fronted Normal', 'Rear Breakage', 'Rear Crushed', 'Rear Normal']




class CarClassifierResNet(nn.Module):

    def __init__(self, num_classes):
        super().__init__()

        self.model = models.resnet50(weights=None)

        # Freeze all pretrained layers
        for param in self.model.parameters():
            param.requires_grad = False

        # Unfreeze final residual block
        for param in self.model.layer4.parameters():
            param.requires_grad = True

        # Replace fully connected layer
        in_features = self.model.fc.in_features

        self.model.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(in_features, num_classes)
        )

    def forward(self, x):
        return self.model(x)



def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize(224, 224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])


    ])
    image_tensor = transform(image).unsqueeze(0)


    global trained_model

    if trained_model is None:
        trained_model = CarClassifierResNet()
        trained_model.load_state_dict(torch.load("models/saved_model.pth"))
        trained_model.eval()

    with torch.no_grad():
        output = trained_model(image_tensor)
        _, predicted_class = torch.max(output, 1)
        return class_name[predicted_class.item()]

