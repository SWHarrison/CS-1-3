#function for finding a a single phone number's cost
def find_phone_number_cost(text_file, phone_number):

    if(phone_number[0] == '+'):
        phone_number = phone_number[1:]

    file = open(text_file,'r')
    read_numbers = file.readlines()
    file.close()

    prev_offset = 99999
    to_return = 0
    for number in read_numbers:

        split_number = number.strip().split(',')
        phone_num = split_number[0][1:]
        is_match = True
        for i in range(len(phone_num)):
            if(phone_num[i] != phone_number[i]):
                is_match = False
                break
        if is_match:
            offset = len(phone_number) - len(phone_num)
            print("prefix is", phone_num)
            print(offset)
            if(offset <= prev_offset):
                prev_offset = offset
                to_return = float(split_number[1])

    return to_return

print(find_phone_number_cost('route_costs100.txt','443607738'))
