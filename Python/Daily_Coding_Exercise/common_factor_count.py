def find_factor(n):
    result = []
    start = 1
    while start <= int(n/2):
        if n%start == 0 and not start in result:
            result.append(start)
            if not (int(n/start)) in result:
                result.append(int(n/start))
        start+=1
    return sorted(result)

num1,num2 = int(input("Enter no 1: ")),int(input("Enter no 2: "))
list1_set = set(find_factor(num1))
common_factor = list(list1_set.intersection(find_factor(num2)))
print(len(common_factor))
