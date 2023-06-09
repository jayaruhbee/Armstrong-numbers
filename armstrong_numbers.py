# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong_arr = []
    for num in range(1, len(numbers)):
        digits = len(str(num))
        working_num = [int(digit) for digit in str(num)]
        sum = 0
        for n in range(len(working_num)):
            sum += working_num[n] ** digits
        if sum == num:
            armstrong_arr.append(num)
        return armstrong_arr

# input: list of #'s 0-999
# create empty armstrong nums list
# create total var
# create variable that will reflect the # of digits for arr[n]
# edge case if arr[n] < 10 push to armstrong arr
# for arr[n] -iterate over each digit and n^digits
# after each calc, update total
# if total == arr[n]: push arr[n] to armstrong arr





# print(f'digits: {digits}')
# print(f'num: {num} working_num: {working_num}')
# print(f'armstrong: {armstrong_arr}')
# numbers = list(range(0, 999))
# find_armstrong_numbers(numbers)