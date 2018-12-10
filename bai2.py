import re
x = True
a= ""
b =s= ""

#s.startswith(".") or
while s.endswith(".") or s.startswith(".") or s == "." or not re.search("[.]",s):
    count = 0
    s = input("Please inter input valid: ")
    for i in s:
        if re.search("[.]", i):
          count =count+1
    if count >=2:
        print(f"Invalid input: {s}")
        #continue
        b = s.split(".")
        a =b[-1]
print(f"tail file: .{a}")