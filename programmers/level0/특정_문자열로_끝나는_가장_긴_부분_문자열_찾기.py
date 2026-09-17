/*
문자열 myString과 pat가 주어집니다. 
myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.  


     find  왼쪽에서 찾아서 나온 첫번째 위치
     rfind 오른쪽에서 찾아서 나온 첫번째 위치 
*/



def solution(myString, pat):
    
    word = ""
    #find  왼쪽에서 찾아서 나온 첫번째 위치
    #rfind 오른쪽에서 찾아서 나온 첫번째 위치
    word = myString[:myString.rfind(pat)+ len(pat)]
    return word
