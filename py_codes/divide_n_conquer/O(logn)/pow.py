#!/usr/bin/env python

def pow2(x, y):
    if y < 0:
        if x == 0:
            return None
        else:
            return float(1)/pow2(x, -y)
    elif y == 0:
        if x == 0:
            return 0
        else:
            return 1
    else:
        result = 1
        while y > 1:
            if y & 1 == 1:
                result *= x
            y /= 2
            x *= x
        result *= x
    return result

if __name__ == "__main__":
    x, y = map(int, raw_input().strip().split())
    print pow2(x, y)