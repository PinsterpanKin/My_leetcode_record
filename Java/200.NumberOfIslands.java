class Solution{
    public int numIslands(char[][] grid){
        int count = 0;
        int row = grid.length;
        int col = grid[0].length;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    count++;
                    dfs(i, j, row, col, grid);
                }
            }
        }
        return count;
    }

    private void dfs(int i, int j, int row, int col, char[][] grid) {
        if (i < 0 || i >= row || j < 0 || j >= col || grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';
        dfs(i + 1, j, row, col, grid);
        dfs(i - 1, j, row, col, grid);
        dfs(i, j + 1, row, col, grid);
        dfs(i, j - 1, row, col, grid);
    }
}