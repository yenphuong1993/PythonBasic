def count_even_odd():
    listA = []
    n = int(input("How many element on list: "))
    sole = sochan =  0
    for i in range(1,n+1):
        a = int(input(f'The number {i}: '))
        listA.append(a)
        if a%2:
            sole +=1
        else:
            sochan +=1
    print(f"LisatA {listA}")
    print(f"ListA have {sole} number odd")
    print(f"ListA have {sochan} number even")


def count_odd_even():
    listB = [1,2,3,4,5,6,7,8,9]
    sole = sochan = 0
    for i in listB:
        if i%2:
            sole += 1
        else:sochan +=1
    print(f"ListB: {listB}")
    print(f"ListB have {sole} number odd")
    print(f"ListB have {sochan} number even")


if __name__ == '__main__':
    count_even_odd()
    count_odd_even()