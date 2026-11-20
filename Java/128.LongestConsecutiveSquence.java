class Solution{
    public int longestConsecutive(int[] nums){
        Set<Integer> numSet = new HashSet<>();
        for(int num : nums){
            numSet.add(num);
        }
        int max_len = 0;
        for(int num : numSet){
            if(!numSet.contains(num - 1)){
                int current_num = num;
                int current_len = 1;

                while(numSet.contains(current_num + 1)){
                    current_num += 1;
                    current_len += 1;
                }
                max_len = Math.max(max_len, current_len);
            }
        }
        return max_len;
    }
}