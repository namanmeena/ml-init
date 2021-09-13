import os


class FileUtils:
    @staticmethod
    def exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def get_all_files(dir_path, with_path=True):
        files = os.listdir(dir_path)
        if with_path:
            files = [f"{dir_path}/{f}" for f in files]
        return files
