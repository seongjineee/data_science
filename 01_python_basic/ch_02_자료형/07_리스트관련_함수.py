a= [1,2,3]
print(type(a))
a.append([5,6]) # 해당값 리스트에 추가 (리스트 확장이 아님)
print(a)
a= [1,2,3]
print(a)
a.append(4)
print(a)
a.append(5)
print(a)
#############################################
a = [1,4,3,2]
print(a)
a.sort()
print(a)
b = ['a','c','b']
print(b)
b.sort()
print(b)

a=['a','c','b']
a.reverse() # 배열의 순서를 뒤집는다
print(a)

a = [1,4,3,2]
a.reverse()
print(a)

# 그렇다면 내림차순 정렬은

a=[1,4,3,2]
a.sort(reverse=True)
print(a)


######################################
# 출력 포맷 설정 및 자동화
######################################

a=[1,4,3,2]
print(f"a: {a}")
a.sort(reverse=True)
print(f"a: {a}")

print(f"a: {a}")
print ((12+5)/2)

print(f"(12+5)/2: {(12+5)/2}")

# 리스트로 생성된 값은 변경 가능하다.
a=[1,4,3,2]
print(f"a: {a}")
a.append(5)
print(f"a: {a}")
a=[1,4,3,2]

########
# 리스트의 값은 변경 가능한 속상을 가지고 있다.

# 문자열은 변경이 불가능(immurtable)한 속성을 가지고 있다.
str1 = "Life is too short"
print(f"str1: {str1}")
print(f"str1[0]: {str1[0]}")
# str1[0]='n' # 변경 불가하기 때문에 에러 발생
# Immutable 한 타입의 멤버 메소드는 자기 자신을 변경할 수 없기 때문에
# 변경된 값을 반환하는 특징을 가지고 있다.
print(f'str1.replace("Life", "Your leg"): {str1.replace("Life", "Your leg")}')

#문자열 타입이 변경 가능하다고 착각하는 이유

str1 = str1.replace("Life", "Your leg")
print(f"str1: {str1}")