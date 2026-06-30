string="""
\n\n\n<html><body><h1>   Welcome to the Project!   </h1></body></html>
   
Check out our website at https://example.com/download-links for more info!!! 
   
   Please   remove   the   unnecessary    spaces here. Use code: #Markdown_123.
   https://example.com/download-links
   📧 Contact us at support@example.com or call 1-800-555-0199...   a-b-c
   bigmain@gmail.com 
   
   \n\nGoodbye!

"""

import re
from bs4 import BeautifulSoup

def clean_text(target_string: str) -> str:
    """using only pythonic methods to clean large string documents"""
    url_pattern=r"https://[^\s]+"
    email_pattern=r"[A-Za-z0-9]+[@]{1}[^\s]*"
    phone_pattern=r"[0-9]+[-]{1}[0-9]+[^\s]*"
    soup_string = BeautifulSoup(target_string,"html.parser")
    string_without_tags = soup_string.get_text()
    string_stripped = string_without_tags.strip() #remove whitespaces    
    urls = re.findall(url_pattern,string_stripped)
    emails = re.findall(email_pattern,string_stripped)
    phones = re.findall(phone_pattern,string_stripped)
    stuff_to_remove = [urls,emails,phones]
    for list_to_remove in stuff_to_remove:
        for substring in list_to_remove:
            string_stripped = string_stripped.replace(substring,"")
    string_stripped  = string_stripped.replace("\n","")
    string_stripped  = string_stripped.replace("\t","")

    #removing all white spaces but leaving a single space in between words
    split_string = string_stripped.split()
    string = " ".join(split_string)
    return string
clean_text(string)