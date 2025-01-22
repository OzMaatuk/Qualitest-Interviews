import math


def solution(N):
    x = N
    l = math.floor(math.log2(x))

    r = 0
    start = False
    max = 0

    while (l+1) > 0:
        x = x - math.pow(2, l)
        l -= 1
        if x >= 0:
            # it's 1
            if start:
                # check for new max, and init
                if r > max:
                    max = r
                r = 0
                start=False
            else:  # nothing
                start=True
        else:
            # it's 0
            if start:
                # last one was also 0, so continue counting
                pass
            else:
                # last one was 1, need to start new count
                start = True
            r += 1
            x = x + math.pow(2, l+1)

    return max


def main():
    print("Start main()")
    for i in range(64,129):
        print(i, solution(i), "{:b}".format(i))


if __name__ == "__main__":
    main()