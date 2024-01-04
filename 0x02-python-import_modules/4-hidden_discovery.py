#!/usr/bin/python3
if __name__ == "__main__":
    """ program that prints all the names defined by the compiled"""
    import hidden_4 as hid

    for files in dir(hid):
        if files[:2] != "__":
            print(files)
