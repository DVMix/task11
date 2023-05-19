import glob

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pathlib import Path


def visualize_statistic(differences):
    plt.plot(differences)
    plt.ylabel('some numbers')
    plt.show()


def main():
    pad = 100
    for file in glob.glob('./data/*/*.jpg'):
        array = cv2.imread(file, 0)
        small_image = cv2.resize(array, [2480, 1240])
        # Image.fromarray(small_image).show()

        medians = np.median(small_image, axis=1)

        differences = medians[:-pad] - medians[pad:]
        crop_start = np.argmax(differences)

        cropped_image = small_image[crop_start:]
        # Image.fromarray(cropped_image).show()
        save_name = f'{Path(file).parent}/2480x1240_{Path(file).name}'
        Image.fromarray(cropped_image).save(save_name)


if __name__ == '__main__':
    main()
