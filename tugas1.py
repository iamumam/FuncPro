# # kode 1 
# def sequenceGenerator(start, stop):
#     x = []
#     for i in range(start,stop+1):
#         x.append(i)
#     return x
# print(sequenceGenerator(1, 10))

# sequenceGenerator = lambda start, stop: list(range(start, stop + 1))
# print(sequenceGenerator(1, 10))

# #kode 2

# def fizzBuzz(a,b):
#     x = []
#     for num in range(a,b):
#         if num % 3 == 0 and num % 5 == 0:
#             x.append("fizzBuzz")
#         elif num % 3 == 0:
#             x.append("Fizz")
#         elif num  % 5 == 0:
#             x.append("Buzz")
#         else:
#             x.append(num)
#     return x

# fizzBuzz = lambda a, b: [(x % 3 == 0) * "Fizz" + (x % 5 == 0) * "Buzz" or x for x in range(a, b)]
# print(fizzBuzz(1, 16))

# fizzBuzz = lambda a, b: ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(a, b)]
# print(fizzBuzz(1, 16))

# def twoNumber(l):
#     res = []
#     for i in 1:
#         if l.index(i) == len(l)-1:
#             break
#         z = i + l[i+1]
#         res.append(z)
#     return res

twoNumberTest = lambda l: list(filter(lambda e: e is not None, map(lambda e: l.index(e) + l[l.index(e) + 1] if l.index(e) != len(l) - 1 else None, l)))
print(twoNumberTest([x for x in range(0, 15)]))

twoNumber = lambda l: list(map(lambda i: l[i] + l[i+1], range(len(l)-1)))
print(twoNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))