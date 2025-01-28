#include <stdio.h>

void swap(int* x, int* y) {
	printf("value of x: %i.\n", *x);
	printf("Inside swap : x = %i et y = %i.\n ",*x, *y);
        int temp = *x;
        *x = *y;
        *y = temp;
	printf("Inside swap : x = %i et y = %i.\n ", *x, *y);
};

int main(int argc, char* argv[]) {
	int a = 1;
	int b = 2;
	int* a_ptr = &a;
	printf("a = %i et b = %i.\n ", a, b);
	printf("address of a : %p, address of b: %p \n", a_ptr, &b);
	swap(a_ptr, &b);
	printf("a = %i et b = %i.\n ", a, b);
	printf("address of a : %p, address of b: %p \n", a_ptr, &b);
	return 0;
};
