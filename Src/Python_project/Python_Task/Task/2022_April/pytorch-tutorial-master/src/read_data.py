import os

from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")

class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.image_path = os.listdir(self.path)


    def __getitem__(self, idx):
        img_name = self.image_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label=self.label_dir
        # sample = {'img': img, 'label': label}
        return img,label

    def __len__(self):
        # assert len(self.image_list) == len(self.label_list)
        return len(self.image_path)

if __name__ == '__main__':
    transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
    root_dir = "../dataset/train"
    ants_label_dir = "ants_image"
    bees_label_dir = "bees_image"
    ants_dataset = MyData(root_dir, ants_label_dir)
    bees_dataset = MyData(root_dir, bees_label_dir)
    train_dataset = ants_dataset+bees_dataset
