
def list_number():
    s= [1,2,3,10,21,5,7,100,9,0]
    max = 0

    for number in s:
        max = number if number > max else max
    return max

def main():
    max = list_number()
    print(f"maximum of list numbers: {max}")

if __name__ == '__main__':
    main()