#include <stdio.h>


//����ṹ�� 
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
	//��ʼ������
	int i,j,k,n,n_SUM;
	
	int count = 0;
	//����
	scanf("%d",&n);
	printf("������%d\n",n);
	for(i=0; i<n; i++){
		scanf("%d",&n_SUM);
		printf("������%d\n",n_SUM);
		for(j=0; j<n_SUM; j++){
			scanf("%s %d",students[count].ID,&students[count].grade);
			students[count].Tag = i + 1;
			count ++;
			printf("ID: %s,     grade:%d,     tag:%d\n",students[count].ID,students[count].grade,students[count].Tag);
		}
	}
	


	//���� 



	//��� 

		
	return 0;
 } 
