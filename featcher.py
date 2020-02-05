def decorate_text(text):
    str.lower(text)
    return f'~*o*o*  {text}  *o*o*~'

if __name__ == "__main__":
    text = 'hello FROM featcher.py'
    print(decorate_text(text))