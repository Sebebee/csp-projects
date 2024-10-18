#include <stdio.h>

int main (void){
 int time;
printf("what time is it?(24 hour format)\n:");
scanf("%d", &time);
if (time>=2000 && time<=2359){
    printf("good evening!");
}else if (time<2000 && time>=1200){
    printf("Good afternoon!");
}else if (time>=800 && time<1200){
    printf("good morning!");
}else if (time<800 && time>0){
    printf("its pretty early!");
}else{
    printf("hmm, I dont know that time. Are you sure you used the correct format?");
}


    return 0;
}