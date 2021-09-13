import numpy as np
from tqdm import tqdm

from utils.file_utils import FileUtils as fsutils
from utils.image_utils import ImageUtils as imutils


class ImageDataLoader:

    def __init__(self):
        self.labels = None

    def set_seed(self, seed):
        np.random.seed(seed)

    def get_images_from_directory(self, dir_path, preprocess=None, size=None,
                                  seed=123):
        self.set_seed(seed)
        labels_path = fsutils.get_all_files(dir_path)
        self.labels = [l.split("/")[-1] for l in labels_path]

        print(f"[INFO] Num labels: {len(self.labels)}")
        print(f"[INFO] Labels: {self.labels}")
        X = []
        y = []
        for i, directory in enumerate(labels_path):
            print(f"[INFO] Loading images for label: {self.labels[i]}")
            images = fsutils.get_all_files(directory)
            for file in tqdm(images):
                img = imutils.read_img(file, size)
                if preprocess is not None:
                    if type(preprocess) == list:
                        for preprocess_fn in preprocess:
                            img = preprocess_fn(img)
                    else:
                        img = preprocess(img)
                X.append(img)
                y.append(self.labels[i])

        X = np.array(X)
        y = np.array(y)
        np.random.shuffle(X)
        np.random.shuffle(y)
        return X, y
