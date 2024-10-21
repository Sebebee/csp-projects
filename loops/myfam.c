#include <stdio.h>
char family[5][65] = {"child1","kid2","child3","mom","dad"};
int i;
int main(void) {
for(i=0;i<5;i++){
printf("Hello, %s\n",family[i]);
}
    return 0;
}
