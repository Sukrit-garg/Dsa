class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig= image[sr][sc]
        if color == orig:
            return image
        rows,cols = len(image),len(image[0])
        def dfs(r,c):
            if r>=rows or r<0 or c>=cols or c<0:
                return
            if image[r][c]==orig:
                image[r][c] = color
            else:
                return
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        dfs(sr,sc)
        return image

        