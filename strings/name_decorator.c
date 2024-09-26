#include <stdio.h>
#include <string.h>
int main(void){
   char name[]="sebebee";
   char prefix[]="(((";
   char afterfix[]=")))";
   strcat(prefix,name);
   printf("%s",prefix);
  strcat(prefix,afterfix);
   printf("%s\n",prefix);

    return 0;
   
}