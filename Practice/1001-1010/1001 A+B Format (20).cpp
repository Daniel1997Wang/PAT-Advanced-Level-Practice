/*
Calculate a + b and output the sum in standard format -- that is,
        the digits must be separated into groups of three by commas
        (unless there are less than four digits).

Input

        Each input file contains one test case. Each case contains
        a pair of integers a and b where -1000000 <= a, b <= 1000000.
The numbers are separated by a space.

Output

        For each test case, you should output the sum of a and b in one line.
The sum must be written in the standard format.

Sample Input
-1000000 9
Sample Output
-999,991
*/

#include <stdio.h>

void format_print(int sum);

int main(void)
{
	//calculate a + b
	int a,b;
	int sum;
	
	scanf("%d %d",&a,&b);
	
	sum = a + b; 
	format_print(sum);
	
	return 0;
}
 
void format_print(int number)
{
	int number_Low,number_Mid,number_Hight;
	if(number < 1000 && number > -1000)
	{
		printf("%d",number);
	} 
	else if(number >= 1000 && number < 1000000)
	{
		number_Low = number % 1000;
		number_Hight = number / 1000;
		printf("%d,%03d",number_Hight,number_Low);
	}
	else if(number > -1000000 && number <= -1000)
	{
		number = -1 * number ; 
		number_Low = number % 1000;
		number_Hight = number / 1000;
		printf("-%d,%03d",number_Hight,number_Low);
	}
	else
	{
		if(number > 0)
		{
			number_Low = number % 1000;
			number_Mid = ((number - number_Low) / 1000) % 1000;
			number_Hight = number / 1000000;
			printf("%d,%03d,%03d",number_Hight,number_Mid,number_Low);
		}
		else
		{
			number = -1 * number ; 
			number_Low = number % 1000;
			number_Mid = ((number - number_Low) / 1000) % 1000;
			number_Hight = number / 1000000;
			printf("-%d,%03d,%03d",number_Hight,number_Mid,number_Low);
		}
	} 
}
