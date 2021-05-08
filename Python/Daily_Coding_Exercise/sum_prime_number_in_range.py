def prime_num_sum_range(ran = input('Please provide the range: ')):
    ran = int(ran)
    prime_number_list = [2,3]
    sum = 5
    num = 4
    while len(prime_number_list) <  ran:
        counter = 1
        for i in prime_number_list:
            if num%i == 0:
                counter = 1
                break
            else:
                counter = 0

        if counter == 0:
            prime_number_list.append(num)
            sum+=num
        num+=1
    print(f"\nSum of first {ran} prime number is {sum}")

prime_num_sum_range()
    