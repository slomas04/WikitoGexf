import os
import glob
import re

INDEX_PATH = "enwiki-20250801-pages-articles-multistream-index.txt"
INDEX_DIR = "index/"
INDEX_POSTFIX = "_wikiindex.txt"

CURRENT_LINES = []

fileDict = {}

def formatString(s):
    return re.sub(r'[\\/*?:"<>|.]',"",s).strip()

def submit_linegroup(lines, nextCode):
    for line in lines:
        lineCode = formatString(line[2])[:2].lower()
        if lineCode not in fileDict:
            fileDict[lineCode] = open(INDEX_DIR + lineCode + INDEX_POSTFIX, "w+", encoding="utf8")
        line.insert(1, nextCode)

        sline = ":".join(line)
        fileDict[lineCode].write(sline)

def handle_index(line):
    global CURRENT_LINES
    linef = line.split(":", 2)
    if (CURRENT_LINES == []):
        CURRENT_LINES.append(linef)
    elif(CURRENT_LINES[len(CURRENT_LINES)-1][0] != linef[0]):
        submit_linegroup(CURRENT_LINES, linef[0])
        CURRENT_LINES = []
        CURRENT_LINES.append(linef)
    else:
        CURRENT_LINES.append(linef)

def main():
    print("Creating new Index dir...")
    # If folder exists, wipe it
    if os.path.exists(INDEX_DIR):
        files = glob.glob(INDEX_DIR + "*")
        for f in files:
            os.remove(f)
    else:
        os.makedirs(INDEX_DIR)

    print("Reformatting and Writing...")
    with open(INDEX_PATH, encoding="utf8") as infile:
        for line in infile:
            handle_index(line)
    handle_index("0:-1:FILE_TERMINATE") # I am too tired to think of a good solution to this

    print("Closing file instances...")
    for key in fileDict:
        fileDict[key].close()

    print("Sorting files...")
    files = glob.glob(INDEX_DIR + "*")
    for i in files:
        fileArr = []
        with open (i, 'r', encoding="utf8") as f:
            for line in f:
                linef = line.split(":", 3)
                fileArr.append(linef)
        fileArr.sort(key=lambda x: x[3])
        with open(i, 'w', encoding="utf8") as f:
            for x in fileArr:
                sline = ":".join(x)
                f.write(sline)

    print("Done!")

if __name__ == "__main__":
    main()