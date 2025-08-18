from indexWiki import formatString, INDEX_DIR, INDEX_POSTFIX
from urllib.parse import unquote

def binSearch(arr, targetVal):
  targetVal = targetVal + "\n"
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2

    if arr[mid][3] == targetVal:
      return mid
    if arr[mid][3] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

def file_from_name(name):
    nc = formatString(name)[:2].lower()
    fileAsArr = []
    
    with open(INDEX_DIR + nc + INDEX_POSTFIX, "r", encoding="utf8") as f:
        for line in f:
            linef = line.split(":", 3)
            fileAsArr.append(linef)
    
    pos = binSearch(fileAsArr, name)
    if (pos < 0):
       name = name[0].upper() + name[1:]
       posb = binSearch(fileAsArr, name)
       posc = binSearch(fileAsArr, name.replace('&', 'and'))
       if posb >= 0:
         return fileAsArr[posb]
       if posc >= 0:
         return fileAsArr[posc]
       raise Exception("Could not find " + name + " in index!")
    
    return fileAsArr[pos]
        

def file_from_url(URL):
    suffix = URL.rsplit('/', 1)[-1]
    suffix = unquote(suffix)
    suffix = suffix.replace("_", " ")
    return file_from_name(suffix)


def main():
    m = input("1.\tRetrieve by name\n2.\tRetrieve by URL\n>>> ")
    n = input("Enter " + ("name" if m=='1' else 'url') + "\n>>> ")
    if m == '1':
       print(file_from_name(n))
    if m == '2':
       print(file_from_url(n))


if __name__ == "__main__":
    main()