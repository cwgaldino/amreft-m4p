#include "../include/ieee-c.h"
#include <stdio.h>
#include <stdlib.h>

int receiveGpib(char * deviceAnswer, short int address)
{
	int readMessageLength;
	int status;
	
	enter(deviceAnswer, 100, &readMessageLength, address, &status);
	return status;
}

int main(int argc, char *argv[])
{
	char* deviceAnswer = malloc(100*sizeof(char));
	
	// Check if number of parameter are ok
	if(!(argc==2))
	{
		printf("ERROR: 1 parameter are required and %d were given.\n", argc-1);
		free(deviceAnswer);
		return 0;
	}
	
	//Send string
	int status = receiveGpib(deviceAnswer, atoi(argv[1]));
	
	if(status==0)
		printf("%s", deviceAnswer);
	else if(status==8)
		printf("TIMEOUT ERROR");
	
	free(deviceAnswer);
	return 0;
}