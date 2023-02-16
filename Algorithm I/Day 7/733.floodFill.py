class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        value = image[sr][sc]
        rows, cols = len(image), len(image[0])

        if value == color:
            return image 

        def dfs(r, c):
            if (r < 0 or r > rows-1 or c < 0 or c > cols-1 or image[r][c] != value):
                return 
            else:
                image[r][c] = color
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        dfs(sr, sc)
        return image

# T: O(n)
# S: O(n)
