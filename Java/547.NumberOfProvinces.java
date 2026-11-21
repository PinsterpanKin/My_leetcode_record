//My Solution: recursively traverse the graph and mark all the connected nodes as 0 to avoid repeated counting. Not efficient.
class MySolution {
    public int findCircleNum(int[][] isConnected) {
        int count = 0;
        int row = isConnected.length;
        int col = isConnected[0].length;
        for(int i=0; i < row; i++){
            for(int j=0; j < col; j++){
                if(isConnected[i][j] == 1){
                    count++;
                    dfs(i, j, col, isConnected);
                }
            }
        }
        return count;
    }

    private void dfs(int i, int j, int col, int[][] grid){
        while(j < col){
            if(grid[i][j] == 1){
                grid[i][j] = 0;
                dfs(j, 0, col, grid);
            }
            j++;
        }
    }
}

//A better solution could be turning the 2 dimension traversal in to 1 dimension visted record.
class Solution{
    public int findCircleNum(int[][] isConnected) {
        int count = 0;
        int row = isConnected.length;
        boolean[] visited = new boolean[row];
        for(int i=0; i < row; i++){
            if(!visited[i]){
                count++;
                dfs(i, row, isConnected, visited);
            }
        }
        return count;
    }

    private void dfs(int i, int row, int[][] grid, boolean[] visited){
        for(int j=0; j < row; j++){
            if(grid[i][j] == 1 && !visited[j]){
                visited[j] = true;
                dfs(j, row, grid, visited);
            }
        }
    }
}