#include<stdio.h>
#include<stdlib.h>

int main(){
	
	FILE* file;
	char buffer[256];
	file = fopen("/proc/meminfo","r");

	fgets(buffer,sizeof(buffer),file);
	printf("memory: %s", buffer);
	fclose(file);

	return 0;
}
