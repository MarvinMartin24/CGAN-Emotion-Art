import torch
from torch import nn
import torchvision.utils as vutils
import torch.nn.functional as F
import matplotlib.pyplot as plt
import os, random, glob, sys
import numpy as np
from PIL import Image


class Generator(nn.Module):

    def __init__(self, input_dim=10, im_chan=3, hidden_dim=64):
        super(Generator, self).__init__()
        self.input_dim = input_dim
        # Build the neural network
        self.gen = nn.Sequential(
            # input is Z, going into a convolution
            nn.ConvTranspose2d( self.input_dim, hidden_dim * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(hidden_dim * 8),
            nn.ReLU(True),
            # state size. (hidden_dim*8) x 4 x 4
            nn.ConvTranspose2d(hidden_dim * 8, hidden_dim * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(hidden_dim * 4),
            nn.ReLU(True),
            # state size. (hidden_dim*4) x 8 x 8
            nn.ConvTranspose2d( hidden_dim * 4, hidden_dim * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(hidden_dim * 2),
            nn.ReLU(True),
            # state size. (hidden_dim*2) x 16 x 16
            nn.ConvTranspose2d( hidden_dim * 2, hidden_dim, 4, 2, 1, bias=False),
            nn.BatchNorm2d(hidden_dim),
            nn.ReLU(True),
            # state size. (hidden_dim) x 32 x 32
            nn.ConvTranspose2d( hidden_dim, im_chan, 4, 2, 1, bias=False),
            nn.Tanh()
            # state size. (im_chan) x 64 x 64
        )

    def forward(self, noise):

        x = noise.view(len(noise), self.input_dim, 1, 1)
        return self.gen(x)

# helper function to un-normalize and display an image
def imshow(img, label, label_classes, save=False, epoch="", batch=""):
    img = img / 2 + 0.5  # unnormalize
    plt.title(str(label_classes[int(label)]))
    plt.imshow(np.transpose(img, (1, 2, 0)))  # convert from Tensor image
    if save:
      plt.savefig('./images/fake.png')

def make_gif():
    fp_in = "./animation/img/fake_*"
    fp_out = "./animation/animation.gif"
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in), key=os.path.getmtime)]
    img.save(fp=fp_out, format='GIF', append_images=imgs, save_all=True)
    print(fp_out)

def get_one_hot_labels(labels, n_classes):
    return F.one_hot(labels, num_classes=n_classes)

def get_one_hot_labels_from_str(num_img_to_gen ,str, label_classes):
  label_index = label_classes.index(str)
  labels = torch.full((num_img_to_gen,), label_index, dtype=torch.float16)
  return get_one_hot_labels(labels.to(torch.int64), len(label_classes))

def get_noise(n_samples, input_dim, device):
    return torch.randn(n_samples, input_dim, device=device)

def combine_vectors(x, y):
    return torch.cat((x, y), 1).float()

def get_dir_gen_w(category):
    return f'./weights/{category}/netG_{category}_64.weight'

def generate(selected_emotion, selected_style, nb_img):
    z_dim = 100
    device = 'cpu'
    label_classes = ['negative', 'neutral', 'positive']
    style_classes = ['portrait', 'landscape', 'abstract', "flower-painting"]
    n_classes = len(label_classes)
    num_img_to_gen = int(nb_img)

    emotion = selected_emotion

    gen = Generator(input_dim = z_dim + len(label_classes)).to(device)
    model_path = "./weights/" + selected_style.split('_')[1] + "/" + selected_style
    gen.load_state_dict(torch.load(model_path, map_location=torch.device(device)))

    label_index = label_classes.index(emotion)
    one_hot_labels = get_one_hot_labels_from_str(num_img_to_gen, emotion, label_classes).to(device)
    noise = get_noise(num_img_to_gen, z_dim, device=device).to(device)
    noise_and_labels = combine_vectors(noise, one_hot_labels.float())

    fake = gen(noise_and_labels).data.cpu()
    vutils.save_image(fake.data, './images/fake.png' , normalize=True)


if __name__ == '__main__':

    save = False
    device = 'cpu'

    z_dim = 100
    label_classes = ['negative', 'neutral', 'positive']
    style_classes = ['portrait', 'landscape', 'abstract', "flower-painting"]
    n_classes = len(label_classes)

    num_img_to_gen = int(sys.argv[3])
    emotion = str(sys.argv[2])
    style = str(sys.argv[1])

    if len(sys.argv) > 4:
        save = str(sys.argv[4])
        if save != "s": raise NameError(f'To save enter the letter s')

    if num_img_to_gen not in np.linspace(1, 20, 20): raise NameError('# of images to generate must be between 1 and 20')
    if emotion not in label_classes: raise NameError(f'Input emotion must be one of those: {label_classes}')
    if style not in style_classes: raise NameError(f'Input style must be one of those: {style_classes}')

    path = get_dir_gen_w(style)
    label_index = label_classes.index(emotion)
    one_hot_labels = get_one_hot_labels_from_str(num_img_to_gen, emotion, label_classes).to(device)
    noise = get_noise(num_img_to_gen, z_dim, device=device).to(device)
    noise_and_labels = combine_vectors(noise, one_hot_labels.float())

    gen = Generator(input_dim = noise_and_labels.shape[1]).to(device)
    gen.load_state_dict(torch.load(path, map_location=torch.device(device)))
    fake = gen(noise_and_labels).to(device).detach().numpy()

    if num_img_to_gen == 1:
        if save:
            imshow(fake[0], label_index,label_classes, True)
        else:
            imshow(fake[0], label_index,label_classes)
    else:
        fig = plt.figure(figsize=(10, 4))
        for i in np.arange(num_img_to_gen):
            ax = fig.add_subplot(2, num_img_to_gen/2, i+1)
            fig.patch.set_visible(False)
            ax.set_aspect("auto")
            ax.axis('off')
            ax.autoscale()
            if save:
                imshow(fake[i], label_index,label_classes, True)
            else:
                imshow(fake[i], label_index,label_classes)
        fig.tight_layout()
    plt.show()
