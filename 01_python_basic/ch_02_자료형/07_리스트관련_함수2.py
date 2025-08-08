a=[1,2,3,4,5]
print(f"a.index(4): {a.index(4)}")

b=["k","l",'m','n']
# print(f"b.index(3): {b.index(3)}") #3이 리스트 b에 없기 때문에 에러 발생
print(f"b.index('l'): {b.index('l')}")# 리슽트에 있는 요소로 검색을 해야한다.

a= [1,2,3]
a.insert(0,4)
print(f"a: {a}")
a.insert(3,5)
print(f"a: {a}")

a=[1,2,3,1,2,3]
a.remove(3)
print(f"a: {a}")
a.remove(3)
print(f"a: {a}")

a=[1,2,3]
print(a.pop())
print(f"a: {a}")

a=[1,2,3,1]
print(a.count(1))

a=[1,2,3]
a.extend([4,5])
print(f"a: {a}")
