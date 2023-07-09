#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for each_name in names:
        if each_name[0:2] != "__":
            print(each_name)
