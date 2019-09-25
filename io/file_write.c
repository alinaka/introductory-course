#include <stdio.h>
#include <stdlib.h>

void set_num(int *num){
	scanf("%d", num);
}

int main(){
	int num;
	FILE *fptr;

	fptr = fopen("file.txt", "w");

	printf("Enter num:");
	set_num(&num);

	fprintf(fptr, "%d", num);
	fclose(fptr);

	return 0;
}
