class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentPath = new ArrayList<>();
        currentPath.add(0);
        dfs(0, graph.length - 1, graph, currentPath, result);
        return result;
    }

    private void dfs(int u, int target, int[][] graph, List<Integer> currentPath, List<List<Integer>> result){
        if(u == target){
            result.add(new ArrayList<>(currentPath));
            return;
        }
        for(int v: graph[u]){
            currentPath.add(v);
            dfs(v, target, graph, currentPath, result);
            currentPath.remove(currentPath.size() - 1);
        }
    }
}