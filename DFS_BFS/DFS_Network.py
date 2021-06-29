def dfs(n,computers,com,visited):
    visited[com]=True
    for connected in range(n):
        if com!=connected and computers[com][connected]==1: 
            if visited[connected]==False:
                dfs(n,computers,connected,visited)



def solution(n, computers):
    answer = 0
    visited=[False]*n
    for com in range(n):
        if visited[com]==False:
            dfs(n,computers,com,visited)
            answer+=1
    
    return answer