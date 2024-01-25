#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define MAX_EXPRESSION_LENGTH 50

int apply_operator(char op, int a, int b) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            return a / b;
        case '^':
            return (int)pow(a, b);
        case '!':
            if (a < 0) {
                fprintf(stderr, "Factorial not defined for negative values\n");
                exit(EXIT_FAILURE);
            }

            int result = 1;
            for (int i = 2; i <= a; i++) {
                result *= i;
            }
            return result;
        default:
            fprintf(stderr, "Invalid operator\n");
            exit(EXIT_FAILURE);
    }
}

int evaluate_expression(char *expression) {
    char *operators[] = {"+", "-", "*", "/", "^", "!"};
    char *token = strtok(expression, " ");
    int result = atoi(token);

    while ((token = strtok(NULL, " ")) != NULL) {
        char *operator = token;
        token = strtok(NULL, " ");
        int operand = atoi(token);
        result = apply_operator(operator[0], result, operand);
    }

    return result;
}

void generate_expressions(int *numbers, int size, FILE *output_file) {
    char *operators[] = {"+", "-", "*", "/", "^", "!"};

    for (int i = size - 1; i > 0; i--) {
        int j = rand() % (i + 1);

        int temp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = temp;
    }

    char expression[MAX_EXPRESSION_LENGTH] = "";
    for (int i = 0; i < size - 1; i++) {
        sprintf(expression + strlen(expression), "%d %s ", numbers[i], operators[rand() % 6]);
    }
    sprintf(expression + strlen(expression), "%d\n", numbers[size - 1]);

    fprintf(output_file, "%s", expression);
}

int count_unique_results(FILE *input_file) {
    int result;
    int unique_results = 0;
    int current_result;
    int first_result = 1;

    while (fscanf(input_file, "%d", &result) == 1) {
        if (first_result || current_result != result) {
            unique_results++;
            current_result = result;
            first_result = 0;
        }
    }

    return unique_results;
}

int main() {
    srand((unsigned int)time(NULL));

    int numbers[] = {2, 0, 2, 4};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    FILE *output_file = fopen("results.txt", "w");
    if (output_file == NULL) {
        fprintf(stderr, "Error opening file for writing\n");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < 100000000; i++) {
        generate_expressions(numbers, size, output_file);
    }

    fclose(output_file);

    FILE *input_file = fopen("results.txt", "r");
    if (input_file == NULL) {
        fprintf(stderr, "Error opening file for reading\n");
        return EXIT_FAILURE;
    }

    int unique_results = count_unique_results(input_file);
    printf("Number of unique results: %d\n", unique_results);

    fclose(input_file);

    return 0;
}
