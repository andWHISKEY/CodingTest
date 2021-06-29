class DisjoinSet:
    def __init__(self,n):
        self.data=list(range(n)) #자기자신을 데이터로 init
        self.size=n

    def find(self,idx):
        return self.data[idx]

    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return 

        for i in range(self.size):
            if self.find(i)==y:
                self.data[i]=x
    @property
    def length(self):
        return len(set(self.data))

       

def solution(n, computers):

    disjoint=DisjoinSet(n)
    
    for i in range(n):
        for x in range(i+1,n):
            if computers[i][x]==1:
                disjoint.union(i,x)
    return disjoint.length