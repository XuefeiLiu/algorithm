class UnionFindSimple:
    def __init__(self, cnt):
        self.parent = list(range(cnt))

    def find(self, i):
        while not self.parent[i] == i:
        # path compression: flatten the tree by recursively point parents to grandparents
            self.parent[i] = self.parent[self.parent[i]] 
            i = self.parent[i]
        return i
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        self.parent[r2] = r1

    def numSets(self):
        islands = 0
        for i, v in enumerate(self.parent):
            if i == v:
                islands += 1
        return islands
    
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        uf = UnionFindSimple(len(row) // 2)
        for i in range(0, len(row), 2):
            a = row[i] // 2
            b = row[i+1] // 2
            uf.union(a, b)
        islands = uf.numSets()

        return len(row)// 2 - islands