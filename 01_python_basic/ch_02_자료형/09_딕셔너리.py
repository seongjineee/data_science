l_person_info = ['홍길동','010-123-4567','1294/03/27']
# 전제조건 : 이름 , 전화번호 ,생년월일의 인덱스가 무엇인지 알고 있어야 한다.
print(f"l_person_info[0]: {l_person_info[0]}") # 이름
print(f"l_person_info[1]: {l_person_info[1]}") # 전화번호
print(f"l_person_info[2]: {l_person_info[2]}") # 생년월일
d_person_info = {
        '이름': '홍길동',
        '전화번호':'010-123-4567',
        '생년월일': '1294/03/27',
        
}
d_person_info['이름'] # 딕셔너리 요소 접근 : 딕셔너리[키값]
print(f"d_person_info['이름']: {d_person_info['이름']}")
d_person_info['전화번호']
print(f"d_person_info['전화번호']: {d_person_info['전화번호']}")
d_person_info['생년월일']
print(f"d_person_info['생년월일']: {d_person_info['생년월일']}")

print(f"type(d_person_info): {type(d_person_info)}")

# dict 요소 추가
# 딕셔너리명 ['새로추가할 키'] = 새로추가할 값
#

d_person_info['나이'] = 45
print(f"d_person_info['나이']: {d_person_info['나이']}")
print(f"d_person_info: {d_person_info}")
# dict 요소 변경
# 딕셔너리명 ['변경할 키'] = 변경 할 값
d_person_info['이름'] = '홍순이'
print(f"d_person_info: {d_person_info}")
d_person_info['나이'] = 21
print(f"d_person_info: {d_person_info}")
d_person_info['전화번호'] = '010-8797-6621'
d_person_info['생년월일'] = '1998/09/01'
print(f"d_person_info: {d_person_info}")

# dict 요소 삭제 
# del 딕셔너리명 ['삭제할 키']
del d_person_info ['나이']
print(f"d_person_info: {d_person_info}")

print(f"d_person_info.keys() : {d_person_info.keys() }")
print(f"list(d_person_info.items()): {list(d_person_info.items())}")

# 모든 요소 삭제
d_person_info.clear()
print(f"d_person_info: {d_person_info}")


d_person_info = {
    '이름': '홍길동',
    '전화번호': '010-123-4567',
    '생년월일': '1294/03/27',

}
d_person_info['이름']
print(f"d_person_info['이름']: {d_person_info['이름']}")
# dict 내장함수로 키로 매핑되는 값 가져오기 
print(f"d_person_info.get('이름'): {d_person_info.get('이름')}")
# dict 요소 접근 기본 문법 vs get()
# print(f"d_person_info['주소']: {d_person_info['주소']}")
print(f"d_person_info.get('주소'): {d_person_info.get('주소')}")


print(f"d_person_info.get('주소','대구 수성구 알파시티1로 170'): {d_person_info.get('주소','대구 수성구 알파시티1로 170')}")

# 리스트의 전체 값 조회 (예습)

numbers = [1,2,3,4,5]

# 열거형타입(Enumeration type): 여러개의 값을 포함할 수 있는 타입
# 예) 문자열, list, tuple , dict
# for 개별값 in 열거형타입의값
for number in numbers:
    print(number)

item_list = ['핸드폰','지갑','차키']
print('차키' in item_list)
print('지폐' in item_list)

# dict 전체 키값 조회
d_person_info.keys()
print(f"d_person_info.keys(): {d_person_info.keys()}")

# 전체 키값을 개별 키값으로 조회

for key in d_person_info.keys():
    print(f"key: {key}")

# 전체 value 값 조회
print(f"d_person_info.values(): {d_person_info.values()}")
# 전체 value의 개별 타입으로 조회
for value in d_person_info.items():
    print(f"value: {value}")

for key, value in d_person_info.items():
    print(f"key: {key}, value: {value}")

for key in d_person_info.keys():
    print(f"d_person_info['{key}']: {d_person_info.get(key)}")
# 개별 item(key, value) 조회
d_person_info.items()
print(f"d_person_info.items(): {d_person_info.items()}")

# 개별 item 조회

for item in d_person_info.items():
    print(f"item: {item}")

# 개별 item을 key, value로 조회
print('{')
for key, value in d_person_info.items():
    print(f"key: {key}, value: {value}")
print('}')






