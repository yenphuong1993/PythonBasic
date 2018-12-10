def construct_pattern():
    for i in range(6):
        print("*" * i)
        if i == 5:
            for i in range (i-1,0,-1):
                print("*" * (i-1))


if __name__ == '__main__':
    construct_pattern()