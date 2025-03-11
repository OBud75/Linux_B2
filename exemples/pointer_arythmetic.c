#include <stdio.h>
struct Person {
    int id;
};
int main() {
    int numbers[] = {1, 2, 3};
    printf("%i.\n", numbers[2]);
    printf("%i.\n", 2[numbers]);
    struct Person people[10];
    for (int i = 0; i < 10; i++) {
        people[i].id = i;
    }
    struct Person *person = people;
    for (int i = 1; i < 10; i++) {
        person->id = i;
        person += 1;
    }
    for (int i = 0; i < 10; i++) {
        printf("Personne id %i.\n", people[i].id);
    }
    int some_array[] = {1, 2, 3, 4, 5};
    for (int *p = some_array; p < some_array + 5; p++) {
        printf("%i\n", *p);
    }
    for (int i = 0; i < 5; i++) {
	printf("%i\n", some_array[i]);
    }
}
