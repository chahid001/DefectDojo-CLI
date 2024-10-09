

def parse_tags(tags): 
    i = 0

    str = []

    while i < len(tags):
        char = ""
        while i < len(tags) and tags[i] != ",":
            char += tags[i]
            i += 1
        str.append(char)
        while i < len(tags) and (tags[i] == " " or tags[i] == ","):
            i += 1
    return str

