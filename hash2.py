#################### my solution

def solution(phone_book):
    answer = True
    phone_book.sort();
    for i in range(len(phone_book) - 1 ):
        if( len(phone_book[i + 1] ) > len(phone_book[i])   ):
            if(phone_book[ i + 1].startswith(phone_book[i]) ):
                answer = False;
                break;
    return answer;


solution( ["119", "97674223", "1195524421"] )
solution(["123","456","789"])


#################### other solution

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
