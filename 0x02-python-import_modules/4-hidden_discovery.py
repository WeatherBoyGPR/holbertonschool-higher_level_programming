#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for cur in dir(hidden_4):
        if not (cur.startswith("__", 0, 3)):
            if not (cur.endswith("__", -1, -3)):
                print("{}".format(cur))
