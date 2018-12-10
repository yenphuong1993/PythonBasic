from math import sqrt
class Triangle():
    def __init__(self,a,b,c):
        self.a1 = a
        self.a2 = b
        self.a3 =c
    def perimeter(self):
        p = self.a1+self.a2+self.a3
        return  p
    def area_Triangle(self):
        triangle1 = Triangle(self.a1,self.a2,self.a3)
        p = triangle1.perimeter()/2
        s = sqrt(p*(p-self.a1)*(p-self.a2)*(p-self.a3))
        return s
def main():

        a=4
        b =5
        c=6
        triangle = Triangle(int(a),int(b),int(c))
        print(f"Perimeter of triangle: {triangle.perimeter()}")
        print(f"Area of the triangle: {triangle.area_Triangle()}")
        # print("Area of the triangle: ".format(triangle.area_Triangle()))
        # print ("Perimeter of triangle:".format(triangle.perimeter()))
if __name__ == '__main__':
    main()
