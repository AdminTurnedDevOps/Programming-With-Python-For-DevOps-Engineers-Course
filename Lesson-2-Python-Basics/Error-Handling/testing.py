import os
import logging


def hello():
    try:
        print_hello = os.system('echo hello')
        print(print_hello)

    except Exception as e:
        #print(e)
        #logging.fatal(msg=e)
        logging.log(level=1, msg='An error has occurred')
        logging.error(msg=e)

hello()
