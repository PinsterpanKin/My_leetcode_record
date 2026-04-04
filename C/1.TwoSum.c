//my stupid original solution that beginners must have written
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* ans = (int*)malloc(sizeof(int) * 2);
    
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                ans[0] = i;
                ans[1] = j;
                *returnSize = 2;
                return ans;
            }
        }
    }
    
    *returnSize = 0;
    return NULL;
}
//popular solution using hash map
#define HASH_SIZE 10007
typedef struct Node {
    int key;            
    int value;          
    struct Node* next;  
} Node;

int hash(int key) {
    int h = key % HASH_SIZE;
    return h < 0 ? h + HASH_SIZE : h;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    Node* map[HASH_SIZE] = {NULL};
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int h = hash(complement);
        Node* curr = map[h];
        while (curr) {
            if (curr->key == complement) {
                int* res = (int*)malloc(sizeof(int) * 2);
                res[0] = curr->value;
                res[1] = i;
                *returnSize = 2;
                return res;
            }
            curr = curr->next;
        }
        int h_now = hash(nums[i]);
        Node* newNode = (Node*)malloc(sizeof(Node));
        newNode->key = nums[i];
        newNode->value = i;
        newNode->next = map[h_now];
        map[h_now] = newNode;
    }
    *returnSize = 0;
    return NULL;
}