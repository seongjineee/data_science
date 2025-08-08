from PyQt5.uic.properties import int_list

str = '12345'
print(str[0:2])
list1 = [1,2,3,4,5]
print(list1[0:1])
# print(list1[0:2]) / 시작 인덱스 생략은 0과 동일
print(list1[2:])

#중첩 리스트 슬라이싱

a=  [1,2,3,['a','b','c'],4,5] #a[3] : 리스트(['a','b','c',])도 결국 a[3]의 요소일 뿐이다.
print(a[3][2])
print(a[2:5])
print(a[3][:2])

temp = ['a','b','c']
print(temp[1])
print(['a','b','c'][1])
print(['a','b','c'][:1])

int_list = [1,2,3,4,5]
print(int_list[:2])



