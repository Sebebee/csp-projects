#include <stdio.h>
#include <string.h>
#include <time.h>
int i, usr;
char one[50],two[50],three[50];

void delay(int sec){
    int milli = 1000*sec;

    clock_t start =  clock();

    while(clock()< start+milli);
}

int main(){
    printf("Give me a number: \n");
    scanf("%d",&usr);
    printf("Give me a word: \n");
    scanf("%s",one);
     printf("Give me another word: \n");
    scanf("%s",two);
    strcat(three,one);
    strcat(three,two);
    //create a loop counts to 50
for(i=1;i<=usr;i++){
   
    //replace numbers divislbe by 3&5 with "FizzBuzz"
    if (i%3==0 && i%5==0){
        printf("%s\n", three);
    }else if (i%3==0){
        printf("%s\n",one);
     // replace numbers divisible by 3 with "Fizz"
    }else if(i%5==0){
        printf("%s\n",two);
    //replace nubmers divisible by 5 with "buzz"
    }else{
        printf("%d\n",i);
    }
   delay(300);
    }
    
    return 0;
}
