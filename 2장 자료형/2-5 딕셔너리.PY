# 딕셔너리의 기본 모습
# {Key1: Value1, Key2: Value1, Key3: Value3, ...}

# # 딕셔너리 쌍 추가하기
# a = {1: 'a'}
# a[2] = 'b'
# print(a)

# a['name'] = 'pey'
# print(a)

# 딕셔너리 요소 삭제하기
# del a[1]
# print(a)

# 딕셔너리에서 Key를 사용해 Value 얻기
# grade = {'pey': 10, 'julliet': 99}
# print(grade['julliet'])

# grade['julliet']

# a = {1:'a', '1':'b'}
# print(a[1])
# print(a['1'])

# 딕셔너리 만들 때 주의할 사항
# a = {1:'a', 2:'b'}
# print(a[1])

# a = {[1,2] : 'hi'}
# print(a)

# Key 리스트 만들기 - keys
# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(a.keys())

# for k in a.keys():
#    print(k)

# Value 리스트 만들기 - values
# print(a.values())

# Key, Value 쌍 얻기 - items
# print(a.items())

# Key: Value 쌍 모두 지우기 - clear
# a.clear()
# print(a)

# Key로 Value 얻기 - get
# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(a.get('um'))

# a.get('phone')

# print(a.get('nokey', 'foo'))
# print(a.get('phone', 'foo'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
# a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
# print('name' in a)

# print('email' in a)
