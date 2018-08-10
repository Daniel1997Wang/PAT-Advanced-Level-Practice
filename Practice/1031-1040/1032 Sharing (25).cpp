#include <stdio.h>

#define N 100001


int get_index(int list[N],int value,int n)
{
	int i;
	for(i=0; i<n; i++){
		if(list[i] == value){
			return i;
		}
	}
}


int IS_exit(int list[N],int value,int n)
{
	int i;
	for(i=0; i<n; i++){
		if(list[i] == value){
			return 1;
		}
	}
	return 0;
}


int main( )
{
	int address_pre[N],address_next[N];
	int Start1,Start2;
	char msg[N];
	int count,i,index,flag;
	int str[N];
 	

 	//ÊäÈë²Ù×÷ 
	scanf("%d %d %d",&Start1,&Start2,&count);

   	for(i=0; i<count; i++){
   		scanf("%d %c %d",&address_pre[i],&msg[i],&address_next[i]);

   	}

   	
   	for(i=0; i<count; i++){
   		if(Start1 != -1){
   			index = get_index(address_pre,Start1,count);
   			str[i] = Start1;
   			Start1 = address_next[index];
   		}
   	}
   	
   	
   	flag = 1;
   	for(i=0; i<count; i++){
   		if(Start2 != -1){
   			index = get_index(address_pre,Start2,count);
   			if(IS_exit(str,Start2,count)){
   				printf("%05d",Start2);
   				flag = 0;
   				break;
   			}
			Start2 = address_next[index];	
   		}
   	}
   	
   	
   	if(flag == 1){
		printf("-1");
   	}
 	return 0;
}
