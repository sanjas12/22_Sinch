from pathlib import Path
from pprint import pprint
import os

path_flash = "h:\\"
path_pc = "d:\\sanja"

sinch_dirs = ["Ком", "My_Works", "!computer science"]

def is_path(root_path, sinch_dirs):
    list_dir = [Path(root_path, d) for d in sinch_dirs]
    if os.path.exists(root_path):
        list_paths = [p for p in Path(root_path).iterdir() if p in list_dir]
        return list_paths
    else:
        print(f'Путь"{root_path}" не существует') 
        

pc_dir = is_path(path_pc, sinch_dirs)
flash_dir = is_path(path_flash, sinch_dirs)

pprint(flash_dir)
pprint(pc_dir)

# path_pc = "d:\"



# Directories
# BASE_DIR = Path(__file__).parent.parent.absolute()
# CONFIG_DIR = Path(BASE_DIR, "config")

# LOGS_DIR = Path(BASE_DIR, "logs")
# LOGS_DIR.mkdir(parents=True, exist_ok=True)
# LOG_FILE = Path(LOGS_DIR, 'log.log')

# OUT_DIR = Path(BASE_DIR, "DATA_out")
# OUT_DIR.mkdir(parents=True, exist_ok=True)
# OUT_FILE = Path(OUT_DIR, 'out_merge.csv')

#Logging
# FORMAT = '%(asctime)s:%(levelname)s:%(message)s'