


def sum(list):
    result = 0
    for i in list:
        result+=i
    return result


print(sum([1,2,3,4]))

#ayni islemi recursion ile yapalim
#recursion da function kendi kendini call eder

def sum1(list1):
    if len(list1)==0:
        return 0
    else:
        return list1[0] + sum(list1[1:])

print(sum1([1,2,3,4,5]))