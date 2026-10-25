class Solution{
	public void moveZeroes(int[] nums){
		int writepointer = 0;
		for(int readpointer = 0; readpointer < nums.length; readpointer++){
			if(nums[readpointer] != 0){
				nums[writepointer] = nums[readpointer];
				writepointer;
			}
		}
		while(writepointer < nums.length){
			nums[writepointer] = 0;
			writepointer++;
		}
	}
}
