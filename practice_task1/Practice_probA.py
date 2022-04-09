def search_binary(list, value): # 입력 : list, value
    low = 0 # low 변수에 0을 할당

    high = len(list)-1 # high 변수에 list 길이에 1을 뺀 값을 할당 (list의 첫 열은 0부터 	시작하므로)

    while low <= high: 
    # high에 저장된 값이 low에 저장된 값보다 크거나 같은 경우 반복

        middle = (low+high)//2
        # low 값과 high값을 더해 2로 나눠 middle에 저장 (나누어 떨어지지 않을 	경우 올림한다)

        if list[middle] > value: # (middle에 저장된 숫자)번째의 값이 입력한 value 값보다 클 경우

            high = middle-1 # high에 (middle-1)값을 저장 (middle값 뒤의 자료는 모두 버림)

        elif list[middle] < value: # (middle에 저장된 숫자)번째의 값이 입력한 value 값보다 작을 경우 

            low = middle+1 # low에 (middle+1)값을 저장 (middle값 앞의 자료는 모두 버림)

        else: return middle # 위의 경우가 모두 아니면 (value 값과 일치하면) middle 값을 return

    return -1

myList = [ 2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47] 
print("인덱스=", search_binary(myList, 34))
