import csv
import chardet
from pathlib import Path
from requests import request

FAIL="failed"
SUCCESS="success"


def handle_web_requests(url: str):
    try:
        respond = request(method="GET",url=url,timeout=2)
        if respond.status_code == 200:
            return (respond, SUCCESS)
        else:
            error_msg = f"Error Failed due to status_code in handle_web_requests Reason : {e}"
            return (error_msg, FAIL)
    except Exception as e:
        error_msg = f"Error Failed to handle_web_requests reason : {e}"
        return (error_msg, FAIL)

#################################################################
def get_encoding(filepath) -> str:
    """Given a filepath it will read it as binary text file to detect its encoding, note encoding detection is not 100% accurate"""
    with open(filepath,mode="rb") as file:
        raw_content_binary = file.read()
        result = chardet.detect(raw_content_binary)
        return result["encoding"]


def locate_file(filepath, allowed_time=30) -> Path | str:
    """given filepath it checks if it exists else it will search for file based on filename in current directory,
    then correct filepath"""

    file_path = Path(filepath)
    if file_path.is_file():
        return file_path
    else:
        target=file_path.name
        extension=file_path.suffix
        root = Path(Path.cwd())
        files_seen=0
        for file in root.rglob(f"*{extension}"):
            if file.is_file() and file.name == target:
                return file
            files_seen+=1
            if files_seen==allowed_time:
                return FAIL
    print(f"error does not exist {filepath}")
    return FAIL
