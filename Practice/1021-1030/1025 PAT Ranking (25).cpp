#include <stdio.h>


//定义结构体 
struct stu
{
	char ID[20];
	int grade;
	int Tag;
	int final_rank;
	int local_rank;
};

stu students[30000];


int main(void)
{
	//初始化变量
	int i,j,k,n,n_SUM;
	
	int count = 0;
	//输入
	scanf("%d",&n);
	printf("组数：%d\n",n);
	for(i=0; i<n; i++){
		scanf("%d",&n_SUM);
		printf("人数：%d\n",n_SUM);
		for(j=0; j<n_SUM; j++){
			scanf("%s %d",students[count].ID,&students[count].grade);
			students[count].Tag = i + 1;
			count ++;
			printf("ID: %s,     grade:%d,     tag:%d\n",students[count].ID,students[count].grade,students[count].Tag);
		}
	}
	


	//操作 



	//输出 

		
	return 0;
 } 
