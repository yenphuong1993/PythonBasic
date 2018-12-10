def sum_list():
    List = [1, 2, 3, 4, 8, 9, 10, 11, 13]
    sum = 0
    for i in List:
        sum = sum + i
    print(f"Tong cac so trong list: {sum}")


if __name__ == '__main__':
    sum_list()
