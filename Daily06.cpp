#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* izquierda;
    Node* derecha;

    Node(int val) : data(val), izquierda(nullptr), derecha(nullptr) {}
};

class BST {
public:
    BST() : raiz(nullptr) {}

    void insert(int val) {
        raiz = insertRec(raiz, val);
    }

    void inorder() {
        inorderRec(raiz);
    }

private:
    Node* raiz;

    Node* insertRec(Node* node, int val) {
        if (node == nullptr) {
            return new Node(val);
        }

        if (val < node->data) {
            node->izquierda = insertRec(node->izquierda, val);
        } else if (val > node->data) {
            node->derecha = insertRec(node->derecha, val);
        }

        return node;
    }

    void inorderRec(Node* node) {
        if (node != nullptr) {
            inorderRec(node->izquierda);
            cout << node->data << " ";
            inorderRec(node->derecha);
        }
    }
};

int main() {
    BST bst;
    int elements[] = {20, 10, 30, 5, 15};

    for (int val : elements) {
        bst.insert(val);
    }

    cout << "Recorrido Inorder del BST: ";
    bst.inorder();
    cout << endl;

    return 0;
}
