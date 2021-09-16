# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(map(lambda x: int(x),input().split(" ")))
b = list(map(lambda x: int(x),input().split(" ")))

string = ""

for x in list(product(a,b)):
    string +=" " + str(x)
string = string.strip()
print(string)
