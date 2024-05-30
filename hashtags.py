def hashtag(strings:str):
    if len(strings)== 0 or len(strings) > 139:
        return False
    strings = strings.capitalized()
    strings = "#"+strings
    return strings
