#include "../include/ieee-c.h"
#include <stdio.h>
#include <stdlib.h>

int sendGpib(char * message, int address)
{
	int status;

	send(address, message, &status);
	
	return status;
}

int main(int argc, char *argv[])
{	
	// Check if number of parameter are ok
	if(!(argc==3))
	{
		printf("ERROR: 2 parameter are required and %d were given.\n", argc-1);
		return 0;
	}
	
	//Send string
	int status = sendGpib(argv[1], atoi(argv[2]));
	
	if(status==0)
		printf("%s", argv[1]);
	else if(status==8)
		printf("TIMEOUT ERROR");
	
	return 0;
}