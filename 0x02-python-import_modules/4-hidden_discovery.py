#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    string = dir(hidden_4)
    sorted_str = sorted(string)
    for i in sorted_str:
        if i[:2] != "__":
            print("{}".format(i))
