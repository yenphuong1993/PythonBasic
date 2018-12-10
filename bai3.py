
def kiemtra_tuoi(ns):
    return int(ns)+ 80 + 1996

def main():
    ten = input("Enter your name: ")
    tuoi = input("Enter your ege: ")
    print("vao nam {} ".format(kiemtra_tuoi(tuoi))+"ban se duoc 100 tuoi")


if __name__ == '__main__':
    main()