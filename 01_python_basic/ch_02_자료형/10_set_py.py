# 빈  set 변수로 생성하기

s = set()
print(f"s: {s}")

# set 자료형 : 유일한 데이터 목록

s1 = set([1,2,3,5,8,2,3,3,1,1,8,8])
print(f"s1: {s1}")

s2 = set('python is powerful languages')
print(f"s3: {s2}")

s3 = set(['python','java','c++','java'])
print(f"s4: {s3}")


l1 = set([1,2,3])
print(f"list(s1): {list(s1)}")
print(f"tuple(s1): {tuple(s1)}")

# 리스트에 존재하는 요소중 중복되는 요소를 제거하여 유일한 목록으로 제공
s3 = set(['python','java','c++','java'])
print(f"list(s3): {list(s3)}")

# 교집합, 합집합 ,차집합

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(f"set1 & set2: {set1 & set2}")
print(f"set1 | set2: {set1 | set2}")
print(f"set1 ^ set2: {set1 ^ set2}")
print(f"set1 - set2: {set1 - set2}")

# 집합 자료형 관련 함수

set = {1,2,3,4}
set.add(5)
print(f"set: {set}")
set.update([6,7,8])
print(f"set: {set}")
set.remove(6)
print(f"set: {set}")



