# 변수는 어떻게 만들까?
# a = 1
# b = "python"
# c = [1, 2, 3]

# 변수란?
# a = [1, 2, 3]

# a = [1, 2, 3]
# id(a)

# 리스트를 복사하고자 할 때
# a = [1, 2, 3]
# b = a

# id(a)

# id(b)

# a[1] = 4
# a
# b

# [:] 이용하기
# a = [1, 2, 3]
# b = a[:]
# a[1] = 4
# a
# b

# copy 모듈 이용하기
# from copy import copy
# a = [1, 2, 3]
# b = copy(a)

# b is a

# 변수를 만드는 여러 가지 방법
# a, b = ('python', 'life')

# (a, b) = 'python', 'life'

# [a, b] = ['python', 'life']

# a = b = 'python'

# a = 3
# b = 5
# a, b = b, a
# a
# b