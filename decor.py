def wrapper(f): #func
    def fun(l): #list
        mobile_num = [] #create an empty list for future numbers
        for numbers in l:
            n = "" #empty value
            n = numbers[::-1][0:10][::-1] #c poslednego do nachala shtoby ubrat nol
            n = " ".join(["+91"] + [n[0:5], n[5:]]) #string.join (("a", "b", "c"), ".") Приведет к "abc".
            mobile_num.append(n) #results of n are adding to empty list mobile_number
        f(mobile_num) #call function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 