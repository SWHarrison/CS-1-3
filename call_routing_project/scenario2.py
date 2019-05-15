def create_dict(text_file):

    file = open(text_file,'r')
    read_numbers = file.readlines()
    file.close()

    cost_checker = {}

    for number in read_numbers:

        split_number = number.strip().split(',')
        phone_num = split_number[0]
        if phone_num in cost_checker:
            if split_number[1] < cost_checker[phone_num]:
                cost_checker[phone_num] == split_number[1]
        else:
            cost_checker[phone_num] = split_number[1]

    return cost_checker

def check_price(phone_number, cost_checker):

    while(len(phone_number) > 1):

        print(phone_number)
        if (phone_number in cost_checker):
            return cost_checker[phone_number]

        phone_number = phone_number[0:-1]

    return 0

cost_checker = create_dict('route-costs-106000.txt')
file = open('phone-numbers-10000.txt','r')
read_numbers = file.readlines()
file.close()

file2 = open('phone-numbers-10000-test-scenario2.txt',"w")
for number in read_numbers:
    number = number.strip()
    cost = check_price(number, cost_checker)
    file2.write(number+ " cost: " + str(cost)+"\n")

file2.close()
