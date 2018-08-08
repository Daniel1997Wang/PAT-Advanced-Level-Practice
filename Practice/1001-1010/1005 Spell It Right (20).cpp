#include "stdio.h"

int sum_dight(int number);

int main(void)
{
	int num,sum;
	char sum_in_English[10] = ["zero","one","two","three","four","five","six","seven","eight","nine"];
	//scanf("%d",&num);
	num = 12345;
	sum = sum_dight(num);
	while(sum != 0)
	{
		printf("%c",sum_in_English[sum % 10]);
	}
	printf("%d",sum);
	return 0;
} 


int sum_dight(int number)
{
	int sum = 0;
	while(number != 0)
	{
		sum = sum + number % 10;
		number = number / 10;
	}
	return sum;
}
