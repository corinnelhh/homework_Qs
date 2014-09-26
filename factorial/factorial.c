// works for inputs up to 20

#include <stdio.h>

long int factorial(long int x){
    long int c = 1;
    long int o = 1;
    while (c <= x) {
        o *= c;
        c += 1;
    }
    return o;
}

int main(){
    long int n = 1;
    while ( n <= 20 ) {
        printf("%ld: %ld\n", n, factorial(n));
        n ++;
    }
}
