'''
# 1.Program for remving duplicates
nums = [23,4,6,23,4,7]
empty_ = []
def removes_(nums,empty):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
    print(empty_)
removes_(nums,empty_)


# 2.program for prime numbers
prime_ = int(input("enter a number : "))
count = 0
def prime_not(prime_,count):
    for i in range(1,prime_+1):
        if prime_ % i == 0:
           count += 1
    if count == 2:
        print(f"{prime_} is a prime")
    else:
        print(f"{prime_} is not a prime")
prime_not(prime_,count)


# 3.program for counting the string
S = "Python is a Prorgamming Language"
count = 0
def counting(S,count):
    so = S.split(' ')
    for i in so:
        count += 1
    print(count)
counting (S,count)


# 4.Program for counting uppercase  and lowercase words
S = "PythoN Is a ProGramminG LanGuagE"
cap_count = 0
small_count = 0
space_count = 0
def cap_small(S,cap_count,small_count,space_count):
    for j in S:
        if j.isupper():
            cap_count += 1
        elif j.islower():
            small_count +=1
        else:
            space_count +=1
    print(f'There total {cap_count} number cap')
    print(f'There total {small_count} number small')
    print(f'There total {space_count} number spaces')
cap_small(S,cap_count,small_count,space_count)
    

'''
