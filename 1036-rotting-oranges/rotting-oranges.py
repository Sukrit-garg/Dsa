class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_time = 0
        start_indices = []
        rows = len(grid)
        cols = len(grid[0])
        good_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    start_indices.append([i,j])
                elif grid[i][j]==1:
                    good_oranges+=1
        if good_oranges == 0:
            return 0
        new_grid = copy.deepcopy(grid)
        del_r= [-1,1,0,0]
        del_c= [0,0,-1,1]
        queue = deque(start_indices)
        def bfs(queue):
            size=len(queue)
            if size == 0:
                return
            nonlocal max_time, good_oranges
            max_time+=1
            for i in range(size):
                row,col = queue.popleft()
                for j in range(4):
                    new_r,new_c = row+del_r[j],col+del_c[j]
                    if 0<=new_r<rows and 0<=new_c<cols and new_grid[new_r][new_c]==1:
                        new_grid[new_r][new_c]=2
                        good_oranges-=1
                        queue.append([new_r,new_c])
            bfs(queue)
            return
        bfs(queue)
        if good_oranges:
            return -1
        else:
            return max_time - 1
        
        



