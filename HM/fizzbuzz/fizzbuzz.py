array = []

with open("fizzbuzztext.txt") as filename:
    s1 = filename.readline()
    for i in s1.split():
        array.append(int(i))

print(array)
fizz = array[0]
buzz = array[1]
numm = array[2]

fizzbuzz = " "
for i in range(1, numm):
    if i % fizz == 0 and i % buzz == 0:
        fizzbuzz += " FB "
    elif i % fizz == 0:
        fizzbuzz += " F "
    elif i % buzz == 0:
        fizzbuzz += " b "
    else:
        fizzbuzz += str(i) + " "
print(fizzbuzz)
with open("fizzbuzzfinfsh.txt", "w") as file_object:
    file_object.write(fizzbuzz)


