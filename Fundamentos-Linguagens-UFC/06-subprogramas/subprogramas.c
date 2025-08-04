#include <stdio.h>

void dobrar_valor(int n) {
    n = n * 2;
    printf("Dentro da função: %d\n", n);
}

int main() {
    int x = 5;
    printf("Antes da função: %d\n", x);
    dobrar_valor(x);
    printf("Depois da função: %d\n", x);
    return 0;
}
