import sys

x = sys.argv[1]
print("input: %s" % x)
aux = ""
string = ""
init = False
count = 0
two_elements = False
three_elements = False
for i in range(1, len(x)):
    if((int(x[i-1]) > 1)and(not init)):
        two_elements = True
        init = True
    else:
        if(not init):
            three_elements = True
            init = True

    if(init):
        if(two_elements):
            aux += x[i-1]
            count += 1
            if(count == 2):
                string += chr(int(aux))
                aux = ""
                count = 0
                init = False
                two_elements = False

        if(three_elements):
            aux += x[i-1]
            count += 1
            if(count == 3):
                string += chr(int(aux))
                aux = ""
                count = 0
                init = False
                three_elements = False
print(string)
