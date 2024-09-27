#include <stdio.h>
#include <string.h>
int main(void){
   char name[20];
   printf("what is your name???:");
   scanf("%s",name);
   char prefix[50]="(((";
   char afterfix[]=")))";
   strcat(prefix,name);
 strcat(prefix,afterfix);
  printf("%s\n",prefix);



    return 0;
   
}