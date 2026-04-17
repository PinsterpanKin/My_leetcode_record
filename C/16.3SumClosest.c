//I actually wrote my python solution first, and then I treat it as a pseudocode to write the C version.
//The brilliance of this solution is that I applied a pruning step to reduce runtime,by which I beat 99.57% of the C submissions
int compare(const void* a, const void* b){//sorting rules
    return (*(int*)a-*(int*)b);
}

int threeSumClosest(int* nums, int numsSize, int target) {

    qsort(nums, numsSize, sizeof(int), compare);//sorting

    int closest_sum=nums[0]+nums[1]+nums[2];
    for(int i=0;i<numsSize-2;i++){
        if(i>0 && nums[i]==nums[i-1]){
            continue;
        }
        int left=i+1, right=numsSize-1;

        //apply a pruning step here to reduce runtime
        int min_sum=nums[i]+nums[left]+nums[left+1];
        if(min_sum>target){
            if(abs(min_sum-target)<abs(closest_sum-target)){
                closest_sum=min_sum;
            }
            break;
        }

        while(left<right){
            int current_sum=nums[i]+nums[left]+nums[right];
            if(current_sum==target){
                return target;
            }

            if(abs(current_sum-target)<abs(closest_sum-target)){
                closest_sum=current_sum;
            }

            if(current_sum<target){
                left++;
            }
            else{
                right--;
            }
        }
    }
    return closest_sum;
}