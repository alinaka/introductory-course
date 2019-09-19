#include <stdlib.h>
#include <stdio.h>

int main(){
	FILE * fp;
	int fd;
	fp = fopen("file.txt", "r");
	fd = fileno(fp);
	printf("%d\n", fd);
	return(0);
}
