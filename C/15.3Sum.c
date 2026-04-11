//This solution is graceful, so proud of myself!!!
//I used dynamic allocation and quick sort to ensure the efficiency while reducing the space complexity.
#include <stdlib.h>//qsort

int compare(const void* a, const void* b){
    return (*(int*)a-*(int*)b);
}//compare function for quick sort

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    *returnSize = 0;//cautious initialization

    qsort(nums, numsSize, sizeof(int), compare);//sort already

    if(nums[0]>0 || nums[numsSize-1]<0){
        *returnColumnSizes=NULL;
        return NULL;
    }//obvious no-solution array

    int capacity=16;
    int** res=(int**)malloc(sizeof(int*)*capacity);
    *returnColumnSizes=(int*)malloc(sizeof(int)*capacity);
    //cautious definition of initial size considering space complexity

    for(int i=0;i<numsSize-2;i++){//traveling and searching
        if(nums[i]>0) break;//the smallest element shouldn't be larger than 0
        if(i>0 && nums[i] == nums[i-1]) continue;//avoid repeatition
        int left=i+1;
        int right=numsSize-1;

        while(left<right){
            int sum=nums[i]+nums[left]+nums[right];

            if(sum==0){//find one!!!
                if(*returnSize>=capacity){//dynamic allocation
                    capacity*=2;
                    res=(int**)realloc(res,sizeof(int*)*capacity);
                    *returnColumnSizes=(int*)realloc(*returnColumnSizes,sizeof(int)*capacity);
                }
                res[*returnSize]=(int*)malloc(sizeof(int)*3);
                res[*returnSize][0]=nums[i];
                res[*returnSize][1]=nums[left];
                res[*returnSize][2]=nums[right];
                (*returnColumnSizes)[*returnSize]=3;
                (*returnSize)++;

                while(left<right && nums[left]==nums[left+1]) left++;
                while(left<right && nums[right]==nums[right-1]) right--;//avoid repeatition

                left++;
                right--;
            }//find one!!!

            else if(sum<0){
                left++;
            }
            else right--;

        }
    }//the work has been done!!!

    if(*returnSize==0){//no solution was found
        free(res);
        free(*returnColumnSizes);
        *returnColumnSizes=NULL;
        return NULL;
    }
    else{
        res=(int**)realloc(res,sizeof(int*)*(*returnSize));
        *returnColumnSizes=(int*)realloc(*returnColumnSizes,sizeof(int)*(*returnSize));
    }//no waste of space complexity

    return res;
}