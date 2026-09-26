def index_root_of_num(num, index):
    guess = num / 2
    while abs(guess**index - num) > 0.0000001:
        guess = ((index - 1) * guess + num / guess ** (index - 1)) / index
    return round(guess, 8)




def square_root(num):
    return index_root_of_num(num, 2)




def cube_root(num):
    return index_root_of_num(num, 3)




def pow(num, exponent):

    count = exponent
    result = 1
    while count >= 1:
        result *= num
        count -= 1

    return result




def factorial(num):
    multiplier = num
    result = 1
    while multiplier >= 1:
        result *= multiplier
        multiplier -= 1

    return result






def gcd(a, b):
    A = find_max(a, b)
    B = find_min(a, b)

    remainder = A % B

    if A%B == 0:
        return B

    while remainder != 0:
        C= remainder
        if B % remainder == 0:
            return remainder
        else:
            remainder = B % remainder
        B = C

    return remainder




def lcm(a,b):
    return (a*b)//gcd(a,b)





def find_max(*numbers):
    if len(numbers) == 0:
        return
    maxi = float('-inf')
    if type(numbers[0]) == type([1]):
        for num in numbers[0]:
            if num > maxi:
                maxi = num
    else:
        for num in numbers:
            if num > maxi:
                maxi = num
    return maxi





def find_min(*numbers):
    if len(numbers) == 0:
        return
    mini = float('inf')
    if type(numbers[0]) == type([1]):
        for num in numbers[0]:
            if num < mini:
                mini = num
    else:
        for num in numbers:
            if num < mini:
                mini = num
    return mini




def abvalue(num):
    if num > 0:
        return num
    else:
        return -1*num





def is_prime(num):
    count = 0
    if num == 1:
        return False
    if num > 0:
        for n in range(1, int(square_root(num)+1)):
            if num % n == 0:
                count += 1

        if count == 1:
            return True

    else:
        return False
    return False




def floor_it(num):
    if num == 0:
        return 0

    if num < 0:
        result = abvalue(num) -abvalue(int(num))
        if result == 0:
            return int(num)
        else:
            return int(num-1)

    elif num > 0:
        return int(num)

def ceil_it(num):
    if num == 0:
        return 0
    elif num < 0:
        return int(num)

    if num > 0:
        if num == int(num):
            return int(num)

        else:
            return int(num+1)


def sum_it(*numbers):
    total_sum = 0

    if len(numbers) == 0:
        return

    elif type(numbers[0]) == int or type(numbers[0]) == float:
        for num in numbers:
            total_sum += num

    else:
        for num in numbers[0]:
            total_sum += num

    return total_sum


def average(*nums):
    if type(nums[0]) == type([1]):
        return sum_it(*nums)/len(nums[0])

    return sum_it(*nums)/len(nums)


def permute_it(choices, reminders):
    return factorial(choices)//factorial(choices-reminders)


def combine_it(choices, reminders):
    return int(permute_it(choices, reminders) * (1/factorial(reminders)))


def fibonacci(num):
    count = 2
    tab = [0, 1]

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        while count <= num:
            tab.append(tab[0] + tab[1])
            count += 1
            tab.pop(0)

    return tab[-1]


def factors(num):
    result = []
    for n in range(1, num+1):
        if num % n == 0:
            result.append(n)
    return result



def prime_factors(num):
    result = []

    if is_prime(num):
        return [num]

    n = 2
    while num >= 1 and n <= num:
        if is_prime(n) and num % n == 0:
            result.append(n)
            num = num // n

        elif num % n != 0:
            n += 1

    return result