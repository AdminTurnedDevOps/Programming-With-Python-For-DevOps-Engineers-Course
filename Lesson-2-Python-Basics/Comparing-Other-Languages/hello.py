import os


def hello():
    try:
        hello = os.system('echo hello')
        print(hello)
    
    except Exception as e:
        print(e)

hello()