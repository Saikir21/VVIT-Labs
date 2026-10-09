def calculate_average(numbers):
    su = 0
    for i in range (len(numbers)):
        su = su + numbers[i]
    return su/len(numbers)
def find_min(numbers):
    mi =  numbers[0]
    for i in range (1,len(numbers)-1):
        if mi > numbers [i]:
            mi = numbers[i]
    return mi
def find_max(numbers):
    ma =  numbers[0]
    for i in range (1,len(numbers)-1):
        if ma < numbers [i]:
            ma = numbers[i]
    return ma
