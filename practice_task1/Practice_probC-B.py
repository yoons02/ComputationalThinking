def solve_maze(g, start, end): # 함수 정의

    qu = [] # qu : 빈 리스트 (저장공간)
    done = set() # done : 빈 세트, 중복을 방지

    qu.append(start) # 출발점을 리스트에 저장
    done.add(start) # 출발점을 세트에 저장
    
    while qu: # qu 리스트에 요소가 있다면 반복
        p = qu.pop(0) # qu 리스트의 첫 요소를 꺼내서 p에 할당
        v = p[-1] # 현재 도착점 (qu에 저장된 마지막 이동경로) 
        if v == end: # 처리해야할 p의 마지막 요소(현재 도착점)가 최종 도착점이라면
            return p # p값을 반환
        for x in g[v]: # 길과 연결된 갈림길 중에
            if x not in done: # 아직 done에 없는 값이 있다면
                qu.append(p + x) # 지금까지 이동한 경로와 함께 qu 한 요소로 저장
                done.add(x) # done 세트에도 추가
        
    return "?"
# 탐색을 마칠 때까지 도착점이 나오지 않으면 나갈 수 없는 미로임 

maze = {
    "a" : ["e"],
    "b": ["c", "f"], 
    "c": ["b", "d"], 
    "d": ["c"],
    "e": ["a", "i"],
    "f": ["b", "g", "j"], 
    "g": ["f", "h"], 
    "h": ["g", "l"],
    "i": ["e", "m"], 
    "j": ["f", "k", "n"],
    "k": ["j", "o"], 
    "l": ["h", "p"], 
    "m": ["i", "n"], 
    "n": ["m", "j"], 
    "o": ["k"],
    "p": ["l"],
}

print(solve_maze(maze, "a", "p"))