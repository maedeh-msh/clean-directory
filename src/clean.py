import json
import shutil
from collections import Counter
from pathlib import Path

from loguru import logger

from src.data import DATA_DIR
from src.utils.io import read_json


class CleanDirectory:
    """
    This class is used to organize files in a directory by moving files into directories based on extensions.
    """
    def __init__(self, directory) : 
       self.directory = Path(directory)
       
       if not self.directory.exists():
            raise FileExistsError(f"{self.directory} does not exists.")

    extensions = {}
    extensions = read_json(DATA_DIR / "extensions.json")
    

    def __call__(self):
        """ Orgnize files in a directory
        """
        logger.info(f"Orgnizing files in {self.directory}...")
        file_extentions = []
        for file_path in self.directory.iterdir():
            if file_path.is_dir():
                continue
            file_extentions.append(file_path.suffix)
            
            if file_path.suffix not in extensions:
                continue
                
            DEST_DIR = self.directory / extensions[file_path.suffix]
            DEST_DIR.mkdir(exist_ok=True)
            logger.info(f'Moving {file_path.suffix:10} to {DEST_DIR}')
            shutil.move(str(file_path), str(DEST_DIR))


if __name__ == "__main__":
    org_files = CleanDirectory('/mnt/d/Downloads/Telegram_Desktop')
    org_files()
    print('Done')
