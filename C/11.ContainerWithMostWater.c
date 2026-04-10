/*In my view
this problem reminded me 
an esential different between homework at school and real engineering trial.
Reading the statement, I can easily come up with a lightly brute-force solution,
with double layers of for loops, which is O(n^2) time complexity.
But it wasn't accepted!
It's silly to do that in leetcode and any other real engineering example,
probably because I was just a beginner...
*/
//Use double pointers instead, the time complexity is O(n) and space complexity is O(1).
#define min(a,b) ((a)>(b) ? (b):(a))

int maxArea(int* height, int heightSize) {
    int n = heightSize;
    int current;
    int h, max = 0; 
    int left = 0, right = n - 1;

    while (left < right) {
        current = min(height[left], height[right]) * (right - left);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
        max = current > max ? current : max;
    }
    return max;
}