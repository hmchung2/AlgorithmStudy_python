import numpy as np;

participant = [ "leo", "kiki", "eden"]
completion  = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

solution(participant, completion)
