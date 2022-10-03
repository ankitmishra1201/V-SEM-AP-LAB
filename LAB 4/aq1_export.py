def reverseString(name):
    return name[::-1]

def pallindrome(name):
    if(name==name[::-1]):
        return "Its pallindrome"
    else:
        return "Its not pallindrome"
