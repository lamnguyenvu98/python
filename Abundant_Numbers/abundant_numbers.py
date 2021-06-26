def proper_sum(number):
    result = 1
    i  = 2
    while(i*i <= number):
        if (number % i == 0):
            result += i if i == (number/i) else (i+number/i)
        i+=1
    return result

def find_abundant(value):
    return proper_sum(value) - value;

print(find_abundant(12))
