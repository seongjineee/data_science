# 비교연산
print(f"1==1: {1==1}")
print(f"1==2: {1==2}")
print(f"2>1: {2>1}")
print(f"2<1: {2<1}")

# 자료형의 참과 거짓
# 데이터 값의 존재 여부를 판단하고자 할때 (결축값 여부 판단)
print(f"bool('python'): {bool('python')}")
input_str = 'python' # 사용자 입력, 특정 열의 특정행의 값
print(f"bool(input_str): {bool(input_str)}")

input_str = '' # Empty String(빈 문자열)은 False로 간주
print(f"boll(input_str): {bool(input_str)}")
#Empty String도 None(정의되지 않은 값)과 구분이 되나 데이터 값이
# 없다는 의미에서 Falsy로 분류되어 bool 연산시 False를 반환한다.
print(f"bool(input_str): {bool(input_str)}")

# 정의되지 않은 값 (Java에서 null)은 파이썬에서 None으로 표현한다.
input_str = None
print(f"bool(input_str): {bool(input_str)}")

pocket = ['핸드폰','지갑','차키']
# 도욱이 지갑에 있는거 다 내놔 라고 했을때.

while pocket:
    print(f"현재 pocket 상황: {pocket}")
    print(f' 현재 주머니에{  pocket.pop() }있어요')

