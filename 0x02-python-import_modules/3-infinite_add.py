#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            count += int(sys.argv[i])
    print(count)
