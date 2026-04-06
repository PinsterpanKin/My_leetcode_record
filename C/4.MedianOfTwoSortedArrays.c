#include <stdio.h>
#define Larger(a, b) ((a) > (b) ? (a) : (b))
#define Smaller(a, b) ((a) < (b) ? (a) : (b))

// My original solution. It worked but was not accepted by leetcode due to runtime limitation.
double findMedianSortedArrays_original(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    if (nums1Size > nums2Size) 
        return findMedianSortedArrays_original(nums2, nums2Size, nums1, nums1Size);

    int m = nums1Size, n = nums2Size;
    int total = m + n;
    int i = m / 2; 
    int median1, median2;

    while (1) {
        int j = (total + 1) / 2 - i;
        if (i > 0 && nums1[i - 1] > nums2[j]) {
            i--;
        } 
        else if (i < m && nums2[j - 1] > nums1[i]) {
            i++; 
        } 
        else {
            if (i == 0) {
                median1 = nums2[j - 1];
            } else if (j == 0) {
                median1 = nums1[i - 1];
            } else {
                median1 = Larger(nums1[i - 1], nums2[j - 1]);
            }

            if (total % 2 == 1) {
                return (double)median1;
            }

            if (i == m) {
                median2 = nums2[j];
            } else if (j == n) {
                median2 = nums1[i];
            } else {
                median2 = Smaller(nums1[i], nums2[j]);
            }

            return (median1 + median2) / 2.0;
        }
    }
    return 0.0;
}
//testing main
int main() {
    int n1[] = {1, 2};
    int n2[] = {3, 4};
    printf("Test 1: Expected 2.50000, Got %.5f\n", findMedianSortedArrays(n1, 2, n2, 2));
    int n3[] = {1, 3};
    int n4[] = {2};
    printf("Test 2: Expected 2.00000, Got %.5f\n", findMedianSortedArrays(n3, 2, n4, 1));
    int n5[] = {0, 0};
    int n6[] = {0, 0};
    printf("Test 3: Expected 0.00000, Got %.5f\n", findMedianSortedArrays(n5, 2, n6, 2));
    int n7[] = {100001};
    int n8[] = {100000};
    printf("Test 4: Expected 100000.50000, Got %.5f\n", findMedianSortedArrays(n7, 1, n8, 1));
    return 0;
}
//Right solution using binary search.

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }

    int m = nums1Size;
    int n = nums2Size;
    int left = 0, right = m;
    int halfLen = (m + n + 1) / 2;

    while (left <= right) {
        int i = (left + right) / 2;
        int j = halfLen - i;

        if (i < right && nums2[j - 1] > nums1[i]) {
            left = i + 1; 
        } else if (i > left && nums1[i - 1] > nums2[j]) {
            right = i - 1; 
        } else {
            int maxLeft = 0;
            if (i == 0) { maxLeft = nums2[j - 1]; }
            else if (j == 0) { maxLeft = nums1[i - 1]; }
            else { maxLeft = Larger(nums1[i - 1], nums2[j - 1]); }
            if ((m + n) % 2 == 1) {
                return maxLeft;
            }

            int minRight = 0;
            if (i == m) { minRight = nums2[j]; }
            else if (j == n) { minRight = nums1[i]; }
            else { minRight = Smaller(nums1[i], nums2[j]); }
            return (maxLeft + minRight) / 2.0;
        }
    }
    return 0.0;
}