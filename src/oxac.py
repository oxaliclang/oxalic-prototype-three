import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".oxa"):
    print("Usage: oxac <file>.oxa")
    exit(1)

def lexer(line):
    splitLine = [char for char in line]
    wordBuilder = str()
    tokenList = list()
    for char in splitLine:
        if char.isalpha(): wordBuilder += char
        else:
            tokenList.append(wordBuilder)
            wordBuilder = str() 
            tokenList.append(char)

    cleanTokenList = list()
    for item in tokenList:
        if item != "":
            cleanTokenList.append(item)
    
    combinedStringTokenList = list()
    enableStringMode = False
    combineString = str()
    for item in cleanTokenList:
        if not enableStringMode:
            if item == "\"":
                enableStringMode = True
                combineString += item
            else: combinedStringTokenList.append(item)
        else:
            if item == "\"":
                enableStringMode = False
                combineString += item
                combinedStringTokenList.append(combineString)
                combineString = str()
            else: combineString += item

    # Lexer = {ID, LINE, POSITION, TYPE, SYMBOL}
    finalTokenList = list()
    identityNumber = 0
    positionNumber = 0
    while positionNumber < len(combinedStringTokenList):
        token = combinedStringTokenList[positionNumber]
        if positionNumber < len(combinedStringTokenList) - 1:
            nextToken = combinedStringTokenList[positionNumber + 1]
        identityNumber += 1
        positionNumber += 1
        if token.startswith("\""): finalTokenList.append(["STRING", token])
        if token == "(": finalTokenList.append(["OPEN_PAREN", token])
        if token == ")": finalTokenList.append(["CLOSED_PAREN", token])
        if token == "{": finalTokenList.append(["OPEN_BRACKET", token])
        if token == "}": finalTokenList.append(["CLOSED_BRACKET", token])
        if token == ",": finalTokenList.append(["OBJECT_SEPERATOR", token])
        if token == ";": finalTokenList.append(["LINE_TERMINATOR", token])
        if token == ":": finalTokenList.append(["ASSIGN", token])
        if token == "=": finalTokenList.append(["EQUALS", token])
        if token == "&": finalTokenList.append(["RETURN", token])
        if token == "@": finalTokenList.append(["PRINT", token])
        if token == "?": finalTokenList.append(["IF", token])
        if token == "#": finalTokenList.append(["COMMENT", token])
        if token == " ": 
            if nextToken != " ":
                finalTokenList.append(["SPACE", token])
        if token.isnumeric(): finalTokenList.append(["INTEGER", token])
        if token.isalpha(): finalTokenList.append(["IDENTIFIER", token])

    return finalTokenList

def parser(lexerContent):
    position = 0
    ast = list()
    lines = list()
    line = list()
    while position < len(lexedContent):
        if lexerContent[position][0] != "LINE_TERMINATOR": line.append(lexerContent[position])
        else:
            line.append(lexerContent[position])
            lines.append(line) 
            line = list()
        position += 1
    print(lines)


lineCount = int()
with open(sys.argv[1]) as oxafile:
    program = str()
    for i in oxafile.readlines():
        program += i
    lexedContent = lexer(program)
    parser(lexedContent)
        
