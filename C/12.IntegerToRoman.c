//easy, reached best runtime without brainstorming
char* intToRoman(int num) {
    char* result = (char*)malloc(16 * sizeof(char));
    int i = 0;

    while (num >= 1000) {
        num -= 1000;
        result[i] = 'M';
        i++;
    }

    if (num >= 900) {
        num -= 900;
        result[i] = 'C';
        i++;
        result[i] = 'M';
        i++;
    }

    if (num >= 500) {
        num -= 500;
        result[i] = 'D';
        i++;
    }

    if (num >= 400) {
        num -= 400;
        result[i] = 'C';
        i++;
        result[i] = 'D';
        i++;
    }

    while (num >= 100) {
        num -= 100;
        result[i] = 'C';
        i++;
    }

    if (num >= 90) {
        num -= 90;
        result[i] = 'X';
        i++;
        result[i] = 'C';
        i++;
    }

    if (num >= 50) {
        num -= 50;
        result[i] = 'L';
        i++;
    }

    if (num >= 40) {
        num -= 40;
        result[i] = 'X';
        i++;
        result[i] = 'L';
        i++;
    }

    while (num >= 10) {
        num -= 10;
        result[i] = 'X';
        i++;
    }

    if (num == 9) {
        num -= 9;
        result[i] = 'I';
        i++;
        result[i] = 'X';
        i++;
    }

    if (num >= 5) {
        num -= 5;
        result[i] = 'V';
        i++;
    }

    if (num == 4) {
        num -= 4;
        result[i] = 'I';
        i++;
        result[i] = 'V';
        i++;
    }

    while (num >= 1) {
        num--;
        result[i] = 'I';
        i++;
    }

    result[i] = '\0'; 
    return result;
}