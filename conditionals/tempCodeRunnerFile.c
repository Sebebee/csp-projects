
int main (void){
 int age[80];
printf("What is your age?\n:");
scanf("%d", age);
if (age>=18){
    printf("You are old enough to vote");
}else if (age<18 && age>=16){
    printf("You are old enough to drive");
}else if (age<16 && age==15){
    printf("You are old enough for a learners permit");
}else if (age<15 && age>=5){
    printf("You are old enough to go to school");
}else{
    printf("you too young bro");
}


    return 0;