#include <stdio.h>

int main(void){
   float income, rent, utilities, groceries, transportation, expenses, savings, total; 
   float prent, putilities, pgroceries, ptransportation, pexpenses;
   printf ("this is going to calculate your budget for the month.");
   printf ("how much do you make a month?\n: ");
   scanf("%f", &income); //what
  printf ("how much is rent?\n ");
 scanf("%f", &rent);
  printf ("how mucch is utilites?\n ");
scanf("%f", & utilities);
 printf ("how mucch is groceries?\n ");
scanf("%f", & groceries);
printf ("how mucch is transportation?\n ");
scanf("%f", & transportation);

expenses = rent + utilities + groceries + transportation;
total = income - expenses - savings;
savings = income*.2;
prent = rent/income*100;
putilities = utilities/income*100;
pgroceries = groceries/income*100;
ptransportation = transportation/income*100;
pexpenses = expenses/income*100;

   printf("your income is: $%.2f\n", income);
   printf("your expenses is: $%.2f\n", expenses);
   printf("your savings is: $%.2f\n", savings);
   printf("your total left to spend is: $%.2f\n", total);
printf("your rent is %.2f%% of you income", "%d",prent);

    return 0;
}