import csv
import chardet
from pathlib import Path

def get_encoding(filepath) -> str:
    """Given a filepath it will read it as binary text file to detect its encoding, note encoding detection is not 100% accurate"""
    with open(filepath,mode="rb") as file:
        raw_content_binary = file.read()
        result = chardet.detect(raw_content_binary)
        return result["encoding"]


def locate_file(filepath, allowed_time=30) -> Path | str:
    """given filepath it checks if it exists else it will search for file based on filename in current directory,
    then correct filepath"""

    print("filepath is",filepath)
    file_path = Path(filepath)
    if file_path.is_file():
        return file_path
    else:
        target=file_path.name
        root = Path(Path.cwd())
        files_seen=0
        for file in root.rglob("*.csv"):
            if file.is_file() and file.name == target:
                return file
            files_seen+=1
            if files_seen==allowed_time:
                return "time allowed to search for file has passed!, please enter correct filepath"
    return f"error does not exist {filepath}"


def read_csv(filepath, correct_encoding)->list:
    """read file function csv, given encoding and filepath returns list"""
    with open(filepath,mode="r", encoding=correct_encoding) as file:
        reader = csv.DictReader(file,delimiter=",")
        data = list(reader)
        return data
    
def read_txt(filepath, correct_encoding)->str:
    """read file txt , given encoding, filepath returns string"""
    with open(filepath,mode="r", encoding=correct_encoding) as file:
        return file.read()




# locate_file("yes//random.txt")
filepath = locate_file("mock_product_catalog.csv")
encoding = get_encoding(filepath)
file_content = read_csv(filepath,encoding)
print("encoding is",encoding)
print("file path is",filepath)
print("file extension is",filepath.suffix)
