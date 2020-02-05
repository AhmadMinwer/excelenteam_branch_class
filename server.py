import featcher  

def printer(text):
    print('from printer>>')
    print(text)

if __name__ == "__main__":
    
    text = "it's so great to be here!!"
    text = featcher.decorate_text(text)
    printer(text)