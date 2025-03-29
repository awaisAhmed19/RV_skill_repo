#include <stdio.h>

// Function to check if p! contains at least n trailing zeroes
int check(int p, int n) {
    int temp = p, count = 0, f = 5;
    while (f <= temp) {
        count += temp / f; // Count factors of 5, 25, 125, etc.
        f *= 5;
    }
    return (count >= n); // Return true if at least n trailing zeroes are found
}

// Function to find the smallest number whose factorial has at least n trailing zeroes
int findNum(int n) {
    if (n == 1)
        return 5; // 5! = 120, which has 1 trailing zero

    int low = 0, high = 5 * n; // Define search range
    
    while (low < high) {
        int mid = (low + high) / 2; // Find mid-point for binary search
        
        if (check(mid, n))  
            high = mid; // If mid! has enough zeroes, search left half
        else
            low = mid + 1; // Otherwise, search right half
    }
    
    return low; // Smallest number whose factorial has at least n trailing zeroes
}

int main() {
    int n = 6; // Find smallest number whose factorial has at least 6 trailing zeroes
    printf("Smallest number with at least %d trailing zeroes in factorial: %d\n", n, findNum(n));
    return 0;
}
