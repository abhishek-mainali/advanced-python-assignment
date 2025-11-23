#include <stdlib.h>
#include <string.h>

char* reverse_string(const char* s) {
    if (!s) return NULL;
    size_t n = strlen(s);
    char* r = (char*)malloc(n + 1);
    if (!r) return NULL;
    for (size_t i = 0; i < n; ++i) r[i] = s[n - 1 - i];
    r[n] = '\0';
    return r;
}

void free_string(char* s) {
    free(s);
}
