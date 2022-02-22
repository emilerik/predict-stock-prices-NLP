import re
def get_invalid_documents(df):
    # Returns indices of documents that are invalid
    invalidIndices = []
    for j in range(len(df)):
        text = df['text'][j]
        thresholdExceed = re.compile("Request Rate Threshold Exceeded", re.IGNORECASE).search(text)
        NoSuchKey = re.compile("NoSuchKey", re.IGNORECASE).search(text)
        noItems = not re.compile("(item\s[1-9]\.[\d]*)", re.IGNORECASE).search(text)
        emptyText = len(text) == 0
        invalidDocument = thresholdExceed or NoSuchKey or noItems or emptyText
        if invalidDocument:
            invalidIndices.append(j)
    return invalidIndices

def find_items_positions(text):
    itemPattern = re.compile("(item\s[1-9]\.[\d]*)", re.IGNORECASE)
    itemsIter = itemPattern.finditer(text)
    itemsSet = set()
    items = []
    for i in itemsIter:
        itemName = str.upper(i.group())
        if itemName not in itemsSet:
            itemsSet.add(itemName)
            items.append(i)

    stop = re.compile("SIGNATURE|/s/", re.IGNORECASE)
    stopMatch = stop.search(text)
    if stopMatch:
        items.append(stop.search(text))

    return [item.span() for item in items]  

def extract_8k(text):
    text_8k = ''
    positions = find_items_positions(text)
    for i in range(len(positions)-1):
        beg = positions[i][1]
        end = positions[i+1][0]
        text_8k += text[beg:end].strip()
    return text_8k

