#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0
    count = len(sys.argv) - 1
    for i in range(0, count):
        sums = int(sys.argv[i + 1]) + sums
    print(sums)
