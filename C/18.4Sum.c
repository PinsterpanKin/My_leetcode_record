//Runtime: 82.81%  Memory: 88.31%
#include <stdlib.h>
int compare(const void* a, const void* b){
    return (*(int*)a-*(int*)b);
}

int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    *returnSize=0;
    qsort(nums, numsSize, sizeof(int), compare);//sort already

    int capacity=16;
    int** res=(int**)malloc(sizeof(int*)*capacity);
    *returnColumnSizes=(int*)malloc(sizeof(int)*capacity);

    for(int i=0; i<numsSize-3; i++){
        if(i>0 && nums[i-1]==nums[i]){
            continue;
        }
        for(int j=i+1; j<numsSize-2; j++){
            if(j>i+1 && nums[j-1]==nums[j]){
                continue;
            }

            long prevalue=nums[i]+nums[j];
            int left=j+1;
            int right=numsSize-1;

            while(left<right){
                long total=prevalue+nums[left]+nums[right];
                if(total==target){
                    if(*returnSize>=capacity){
                        capacity*=2;
                        res=(int**)realloc(res, sizeof(int*)*capacity);
                        *returnColumnSizes=(int*)realloc(*returnColumnSizes, sizeof(int)*capacity);
                    }
                    res[*returnSize]=(int*)malloc(sizeof(int)*4);
                    res[*returnSize][0]=nums[i];
                    res[*returnSize][1]=nums[j];
                    res[*returnSize][2]=nums[left];
                    res[*returnSize][3]=nums[right];
                    (*returnColumnSizes)[*returnSize]=4;
                    (*returnSize)++;
                    left++;
                    right--;
                    while(left<right && nums[left]==nums[left-1]) left++;
                    while(left<right && nums[right]==nums[right+1]) right--;
                }
                else if(total<target){
                    left++;
                }
                else{
                    right--;
                }
            }
        }
    }

    if(*returnSize==0){
        free(res);
        free(*returnColumnSizes);
        *returnColumnSizes=NULL;
        return NULL;
    }
    else{
        res=(int**)realloc(res, sizeof(int*)*(*returnSize));
        *returnColumnSizes=(int*)realloc(*returnColumnSizes, sizeof(int)*(*returnSize));
    }

    return res;
}