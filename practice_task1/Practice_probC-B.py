def solve_maze(g, start, end): # 함수 정의

    qu = [] # qu : 빈 리스트 (저장공간)
    done = set() # done : 빈 세트, 중복을 방지

    qu.append(start) # 출발점을 리스트에 저장
    done.add(start) # 출발점을 세트에 저장
    
    while qu: # qu 리스트에 요소가 있다면 반복
        p = qu.pop(0) # qu 리스트의 첫 요소를 꺼내서 p에 할당
        v = p[-2:] # 현재 도착점 (qu에 저장된 마지막 이동경로) 
        if v == end: # 처리해야할 p의 마지막 요소(현재 도착점)가 최종 도착점이라면
            return p # p값을 반환
        for x in g[v]: # 길과 연결된 갈림길 중에
            if x not in done: # 아직 done에 없는 값이 있다면
                qu.append(p + x) # 지금까지 이동한 경로와 함께 qu 한 요소로 저장
                done.add(x) # done 세트에도 추가
        
    return "?"
# 탐색을 마칠 때까지 도착점이 나오지 않으면 나갈 수 없는 미로임 

maze = {
    "a1": ["b1", "k1"],
    "b1": ["a1", "l1"], 
    "c1": ["m1", "d1"], 
    "d1": ["c1", "e1"],
    "e1": ["d1", "o1"],
    "f1": ["g1", "p1"], 
    "g1": ["f1"], 
    "h1": ["i1", "r1"],
    "i1": ["h1", "j1"], 
    "j1": ["i1", "t1"],
    "k1": ["a1", "u1"], 
    "l1": ["b1", "m1"], 
    "m1": ["c1", "l1"], 
    "n1": ["o1", "x1"], 
    "o1": ["e1", "n1"],
    "p1": ["f1", "q1"],
    "q1": ["p1", "a2"],
    "r1": ["h1", "b2"],
    "s1": ["c2"],
    "t1": ["j1", "d2"],
    "u1": ["k1", "v1", "e2"],
    "v1": ["u1", "w1", "f2"],
    "w1": ["v1", "g2"],
    "x1": ["n1", "h2"],
    "y1": ["z1", "i2"],
    "z1": ["y1", "j2"],
    "a2": ["q1", "b2"],
    "b2": ["r1", "a2", "l2"], 
    "c2": ["s1", "d2"], 
    "d2": ["t1", "c2"],
    "e2": ["u1", "o2"],
    "f2": ["v1"], 
    "g2": ["w1", "q2"], 
    "h2": ["x1", "i2"],
    "i2": ["y1", "h2"], 
    "j2": ["z1", "k2", "t2"],
    "k2": ["j2", "l2"], 
    "l2": ["b2", "k2", "v2"], 
    "m2": ["n2", "w2"], 
    "n2": ["m2"], 
    "o2": ["e2", "p2"],
    "p2": ["o2", "z2"],
    "q2": ["g2", "r2"],
    "r2": ["q2"],
    "s2": ["t2", "c3"],
    "t2": ["j2", "s2"],
    "u2": ["v2"],
    "v2": ["l2", "u2", "w2"],
    "w2": ["m2", "v2"],
    "x2": ["h3"],
    "y2": ["z2", "i3"],
    "z2": ["p2", "y2"],
    "a3": ["k3"],
    "b3": ["c3", "l3"], 
    "c3": ["s2", "b3"], 
    "d3": ["n3"],
    "e3": ["f3", "o3"],
    "f3": ["e3", "p3"], 
    "g3": ["h3", "q3"], 
    "h3": ["x2", "g3"],
    "i3": ["y2", "j3"], 
    "j3": ["i3", "k3", "t3"],
    "k3": ["a3", "j3"], 
    "l3": ["b3", "m3"], 
    "m3": ["l3", "w3"], 
    "n3": ["d3", "x3"], 
    "o3": ["e3", "x3"],
    "p3": ["f3", "z3"],
    "q3": ["g3", "a4"],
    "r3": ["b4"],
    "s3": ["t3", "c4"],
    "t3": ["j3", "s3", "d4"],
    "u3": ["v3", "e4"],
    "v3": ["u3", "f4"],
    "w3": ["m3", "x3"],
    "x3": ["n3", "w3"],
    "y3": ["o3", "i4"],
    "z3": ["p3", "a4"],
    "a4": ["q3", "g3", "b4"],
    "b4": ["r3", "a4"], 
    "c4": ["s3", "m4"], 
    "d4": ["t3"],
    "e4": ["u3", "o4"],
    "f4": ["v3", "g4", "p4"], 
    "g4": ["f4"], 
    "h4": ["i4", "r4"],
    "i4": ["y3", "h4", "j4"], 
    "j4": ["i4", "t4"],
    "k4": ["l4"], 
    "l4": ["k4", "v4"], 
    "m4": ["c4", "n4"], 
    "n4": ["m4", "o4"], 
    "o4": ["e4", "n4"],
    "p4": ["f4", "q4"],
    "q4": ["p4", "r4"],
    "r4": ["h4", "q4", "s4"],
    "s4": ["r4"],
    "t4": ["j4", "u4"],
    "u4": ["t4", "v4"],
    "v4": ["l4", "u4"],
}

print(solve_maze(maze, "y2", "x2"))