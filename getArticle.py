from navigateIndex import file_from_name, file_from_url
import xml.etree.ElementTree as ET
import bz2
import re

DUMP_FILE = "enwiki-20250801-pages-articles-multistream.xml.bz2"

def get_wikitext(offset, nextOffset):
    unzipper = bz2.BZ2Decompressor()

    nextOffset = int(nextOffset)
    offset = int(offset)

    blockSize = nextOffset - offset

    # Read the compressed stream, decompress the data                                                                                                                                                        
    uncompressed_data = b""
    with open(DUMP_FILE, "rb") as infile:
        infile.seek(offset)
        compressed_data = infile.read() if nextOffset == 0 else infile.read(blockSize)
        uncompressed_data += unzipper.decompress(compressed_data)
            
    return uncompressed_data

def get_article(details):
    block = get_wikitext(details[0], details[1])
    block = b"<pages>" + block + b"</pages>"
    target_title = details[3][:-1]
    root = ET.fromstring(block)

    for page in root.findall("page"):  
        title_elem = page.find("title")  
        if title_elem is not None and title_elem.text == target_title:
            return ET.tostring(page, encoding="utf-8").decode("utf-8")
    else:
        raise FileNotFoundError(target_title + " Can not be found!")
    
def get_inlinks(article):
    s = set(re.findall(r"\[\[(.*?)\]\]", article))
    for i in s:
        i = i.split('|')[0]
    return s

def get_inlinks_from_name(n):
    a = file_from_name(n)
    article = get_article(a)
    return get_inlinks(article)

def get_inlinks_from_url(n):
    a = file_from_url(n)
    article = get_article(a)
    return get_inlinks(article)
    

def main():
    m = input("1.\tRetrieve by name\n2.\tRetrieve by URL\n>>> ")
    n = input("Enter " + ("name" if m=='1' else 'url') + "\n>>> ")
    if m == '1':
        a = file_from_name(n)
    if m == '2':
        a = file_from_url(n)
    article = get_article(a)
    inlinks = set(re.findall(r"\[\[(.*?)\]\]", article))

    print(inlinks)
    
    

if __name__ == "__main__":
    main()