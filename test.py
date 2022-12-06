import string

#output:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters1 = list(string.ascii_lowercase)  

# way 2 - ASCII code (A-Z:65-90, a-z:97-122)
letters2 = list(map(chr, range(97, 123)))
letters3 = list(map(chr, range(ord('a'), ord('z')+1)))
print(letters1)
print(letters2)
print(letters3)


print(1, 2, 3)

numbers = [1, 2, 3]
print(numbers)    
print(*numbers)                                 # output:1, 2, 3
