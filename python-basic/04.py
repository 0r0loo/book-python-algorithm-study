# 4-1 문자열
from re import I


print('4-1 문자열')
sentence = '나는 소션입니다.'
print(sentence)
str2 = "파이썬은 쉽다"
str3 = """
나는 소년이고,
파이썬은 쉽다.
"""


# 4-2 슬라이싱
print('4-2 슬라이싱')
jumin = '990120-1234567'
print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2]) # 0부터 2직전까지

print('생년월일 : ' + jumin[:6]) # 처음부터 6직전까지
print('뒤 7자리 : ' + jumin[7:]) # 7부터 끝까지
print('뒤 7자리 (뒤에서부터) : ' + jumin[-7:])  

# 4-3 문자열 처리 함수
print('4-3 문자열 처리 함수')
python = 'Python is Amazing'
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 0번째가 대문자냐? 
print(len(python)) # 문자열의 길이
print(python.replace('Python', 'Java')) # 바뀌기전문자, 바꿀문자

index = python.index('n') # n이 몇번째 인덱스이있는지 없으면 오류남
print(index)
index = python.index('n', index + 1) # 찾을 문자, 찾기 시작할 위치
print(index)

print(python.find('n')) # 찾을문자 n 없으면 -1

print(python.count('n')) # n이 몇번 등장하는지

# 4-4 문자열 포맷
print('4-4 문자열 포맷 ========')
print('a' + 'b') # => ab
print('a', 'b') # => a b

# 방법1
print('나는 %d살입니다.' % 20) # d는 정수를 의미하므로 정수값을 넣을수있음 d = 20
print('나는 %s을 좋아해요.' % '파이썬') # s는 문자열 s = 파이썬
print('Apple은 %c로 시작해요.' % 'A') # c는 char c = A
# 근데 사실 s로 다가능
print('나는 %s 색과 %s 색을 좋아요해요' %('파란', '빨간')) 

# 방법2
print('나는 {}살입니다.'.format(20)) # {} = 20
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간')) #
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간')) # format 파라미터 0번째 1번째 넣기

# 방법3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color = '빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format( color = '빨간', age = 20,))

# 방법4 (v3.6 이상)
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')

# 4-5 탈출문자
print('4-5 탈출문자 =====')
print('백문이 불여일견\n백견이 불여일타')
# \n : 줄바꿈
print('저는 \"나도코딩\"입니다')
# \' : ' \" : "

# \\ : \

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine') # => PineApple

# \b : 백스페이스(한글자 지움)
print('Redd\bApple') # => RedApple

# \t : 탭
print('Red\tApple') # => Red    Apple

# 퀴즈3
print('퀴즈3 =====')
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 에) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내 'e' 갯수 + "!"로 구성
#             nav               5         1               !
# 비밀번호 nav51!

def getPassword(url: str):
  newUrl = url.replace('http://', '')
  dotIndex = newUrl.find('.')
  newUrl = newUrl[:len(newUrl) if dotIndex == -1 else dotIndex]
  newUrlCnt = len(newUrl)
  eCnt = newUrl.count('e')
  return newUrl + str(newUrlCnt) + str(eCnt) + '!'
print(getPassword('http://naver.com'))
