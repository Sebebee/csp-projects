   #include <stdio.h>
   #include <string.h>

void hello(char name[400]){
    char greetings[400]="greetings ";
    strcat(greetings,name); 
    printf(greetings,name);

   }

int main(void){
   
   
   hello("john\n");
    hello("Juan francisco pizzaro the 4th\n");
    hello("donkey\n");
    hello("Archallious\n");
    hello("Willy Wonka\n");
    return 0;
}