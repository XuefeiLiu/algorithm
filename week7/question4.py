from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for item in times:
            start,end,weight = item
            graph[start].append((end,weight))
        cost_to_get_to = {node: float('inf')  for node in range(1,n+1)}
        cost_to_get_to[k] = 0
        visited = set()
        
        priority_queue = []
        path = {}
        # push tuple (value, key) into the priority queue
        heapq.heappush(priority_queue, (0, k))
        while priority_queue:
            cheapest_cost, cheapest_node  = heapq.heappop(priority_queue)
        
            # similar to visisted in BFS
            visited.add(cheapest_node)
            for neighbor, neighbor_cost in graph[cheapest_node]:
                if neighbor in visited:
                    continue
                if cost_to_get_to[neighbor] > cheapest_cost + neighbor_cost:
                    cost_to_get_to[neighbor] = cheapest_cost + neighbor_cost
                    path[neighbor] = cheapest_node
                    heapq.heappush(priority_queue, (cost_to_get_to[neighbor],  neighbor))
        if len(path)!=n-1:
            return -1
        result = 0
        for i in cost_to_get_to:
            result = max(result, cost_to_get_to[i])
        return result