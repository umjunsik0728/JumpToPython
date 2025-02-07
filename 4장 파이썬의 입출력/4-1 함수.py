
# def add(a, b):
#     return a+b

# a = 3
# b = 4
# c = add(a, b)  # add(3, 4)의 리턴값을 c에 대입
# print(c)

# def say(): 
#     return 'Hi' 
# print(say())

# def add(a, b): 
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# add(2, 3)


# def say(): 
#     print('Hi')

# say()
# say()

# def sub(a, b):
#     return a - b

# print(sub(a=4, b=3))
# print(sub(b=4, a=3))

# def add_many(*args): 
#     result = 0 
#     for i in args: 
#         result = result + i   # *args에 입력받은 모든 값을 더한다.
#     return result 

# print(add_many(1, 2, 678, 10000000, 42, 2444444, 14141414))

# def add_mul(choice, *args): 
#     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
#         result = 0 
#         for i in args: 
#             result = result + i 
#     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
#         result = 1 
#         for i in args: 
#             result = result * i 
#     return result

# print(add_mul("mul", 1, 2, 678, 10000000, 42))

# def print_kwargs(**kwargs):
#     print(kwargs.get('name'))

# # print_kwargs(a=1)
# print_kwargs(name='foo', age=3)

# def add_and_mul(a,b): 
#     return a+b, a*b

# print(add_and_mul(1, 3))

# def add_and_mul(a,b):
#     if a > b:
#         return a - b
#     else:
#         return a+b
# print(add_and_mul(1, 4))

# default1.py
# def say_myself(name, age=20, man=True): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % age) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")

# say_myself("name", man=False)


# vartest.py

# def vartest(a):
#     a = a +1

# a = 1
# vartest(a)
# print(a)

# def vartest(a):
#     return a + 1

# a = 1
# a = vartest(a)
# print(a)

# vartest_global.py
# b = 1
# def vartest(): 
#     global a
#     a = a+1

# vartest() 
# print(a)

add = lambda a, b: a+b
result = add(3, 4)
print(result)