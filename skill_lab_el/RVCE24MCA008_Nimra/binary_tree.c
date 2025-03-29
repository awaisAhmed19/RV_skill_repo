#include <stdio.h>
#include <stdlib.h>

// Structure of a Binary Tree Node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Function to find the height of the binary tree
int heightOfTree(struct Node* root) {
    if (root == NULL)
        return -1;

    int leftHeight = heightOfTree(root->left);   // Height of left subtree
    int rightHeight = heightOfTree(root->right); // Height of right subtree
    
    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
}

// Driver Code
int main() {
    // Binary Tree Formation
    struct Node* root = newNode(10);
    root->left = newNode(20);
    root->right = newNode(30);
    root->left->left = newNode(40);
    root->left->right = newNode(28);
    root->right->left = newNode(27);
    root->right->right = newNode(50);
    root->right->left->right = newNode(29);

    printf("Height of given binary tree is %d\n", heightOfTree(root));
    return 0;
}
