def is_techno(n):
    
    if len(str(n))%2==0:
        counter = 0
        boun = int(int(len(str(n)))/2)
        no1 = []
        no2 = []
        for i in range(len((str(n)))):
            if counter == 0:
                no1.append(str(n)[i])
            else:
                no2.append(str(n)[i])
            if i >= boun-1:
                counter = 1
        no1 = int("".join(no1))
        no2 = int("".join(no2))
        if (int((no1+no2)**2)) == int(n):
            return True
        else:
            return False

boundary = int(input("please enter a range: "))
print(boundary)
result= []

for j in range(2,boundary,2):
    if is_techno(j):
        result.append(j)

print(result)
