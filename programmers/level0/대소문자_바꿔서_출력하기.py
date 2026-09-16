#영어 알파벳으로 이루어진 문자열 str이 주어집니다. 
#각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.


str = input()


#print(str.swapcase())
#대소문자 한 번에 뒤집기

result = ""

for c in str:
    if c.isupper():
        #이게 대문자인가?
        
        result += c.lower()
        #소문자로 바꿈
    else:
        result += c.upper()
        #대문자로 바꿈
        
print(result)

