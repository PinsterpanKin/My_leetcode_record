class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        boolean[] visited = new boolean[n];
        dfs(0, rooms, visited);
        for(int i=0; i < n; i++){
            if(!visited[i]){
                return false;
            }
        }
        return true;
    }

    private void dfs(int curr, List<List<Integer>> rooms, boolean[] visited){
        visited[curr] = true;
        for(int key: rooms.get(curr)){
            if(!visited[key]){
                dfs(key, rooms, visited);
            }
        }
    }
}