#include <stdio.h>
int calculaProbabilidade(int num);
int main(){

    int num;
    printf("entre com um numero inteiro: ");
    scanf("%d", &num);

    printf("Probabilidade: %d", calculaProbabilidade(num));



    return 0;
}

int calculaProbabilidade(int num){
        if(num == 1){
            return 2;
        }
        return (num * num);
    }
