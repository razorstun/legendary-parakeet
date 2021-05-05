''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    details = []

    counter = 0

    V = input("Virus strain: ")
    N = abs(int(input("No of tests: ")))

    for i in range(N):
        details.append(input("Person{}: ".format(i+1)))

    for i in range((len(details))):
        if not len(details) == N:
            break
        for letter in details[i]:
            result = 0
            for j in range(len(V)):
                if counter >= j:
                    continue
                if letter == V[j]:
                    result = 1
                    counter = j
                    break
                else:
                    result = 0
        if result == 0:
            print("negative")
        else:
            print("positive")

    
main()

