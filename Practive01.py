def multiple_five_seven():
    A = []
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            A.append(i)
    print(A)


if __name__ == '__main__':
    multiple_five_seven()

