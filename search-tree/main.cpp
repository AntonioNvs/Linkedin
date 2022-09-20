#include <iostream>
#include "node.h"

using namespace std;

Node::Node(int v) {
  right = NULL;
  left = NULL;
  val = v;
}

Node* insert(Node* root, int value) {
  if(root == NULL) {
    root = new Node(value);
    return root;
  }

  if(root->val >= value)
    root->left = insert(root->left, value);
  else
    root->right = insert(root->right, value);

  return root;
}

bool search(Node *root, int target) {
  if(root == NULL) return false;
  if(root->val == target) return true;
  if(root->val > target) return search(root->left, target);
  else return search(root->right, target);
}

int main() {
  Node* root;
  root = NULL;

  root = insert(root, 15);
  root = insert(root, 20);
  root = insert(root, 3);
  root = insert(root, 90);
  root = insert(root, 45);
  root = insert(root, 12);

  cout << "Has '13'? " << search(root, 13) << endl;
  cout << "Has '90'? " << search(root, 90) << endl;
}
