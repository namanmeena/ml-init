import cv2

from utils.file_utils import FileUtils as fs


class ImageUtils:

    @staticmethod
    def read_img(img_path, size=None):
        assert fs.exists(img_path), f"[ERROR] - File does not exist: {img_path}"

        img = cv2.imread(img_path)
        if size is not None:
            if type(size) == tuple or list:
                img = cv2.resize(img, size)
            else:
                print("[WARN] - Image resize not performed, "
                      "value must be either a tuple or a list")
        return img
