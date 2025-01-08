class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ## hashmap of nodes mapped to (in_degree, out_degree)
        degrees = defaultdict(lambda: [0, 0])
        degrees[1] = [0, 0]
        for u, v in trust:
            degrees[u][1] += 1  # out degree
            degrees[v][0] += 1  # in degree
        
        judge = -1
        for key, (in_degree, out_degree) in degrees.items():
            if in_degree == n-1 and out_degree == 0:
                if judge > 0:
                    return -1
                judge = key

        return judge
        