cnt=0
def dfs(numbers,target,idx,value,length):
    global cnt
    if idx==length and target==value:
        cnt+=1
        return 
    if idx==length:
        return

    dfs(numbers,target,idx+1,value+numbers[idx],length)
    dfs(numbers,target,idx+1,value-numbers[idx],length)

def solution(numbers, target):
    length=len(numbers)
    global cnt

    dfs(numbers,target,0,0,length)

    return cnt
