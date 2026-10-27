class Solution {
    public int[] sortArray(int[] nums){
        if(nums.length <= 1) return nums;
        int[] temp = new int[nums.length];
        mergeSort(nums, 0, nums.length - 1, temp);
        return nums;
    }

    private void mergeSort(int[] nums, int left, int right, int[] temp){
        if(left >= right) return;
        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid, temp);
        mergeSort(nums, mid + 1, right, temp);
        merge(nums, left, mid, right, temp);
    }

    private void merge(int[] nums, int left, int mid, int right, int[] temp){
        for(int i = left; i <= right; i++){
            temp[i] = nums[i];
        }
        int i = left;
        int j = mid + 1;
        for(int k = left; k <= right; k++){
            if(i > mid){
                nums[k] = temp[j++];
            } else if(j > right){
                nums[k] = temp[i++];
            } else if(temp[i] <= temp[j]){
                nums[k] = temp[i++];
            } else {
                nums[k] = temp[j++];
            }
        }
    }
}