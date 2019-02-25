#include "../include/ieee-c.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int computerAddr=21;
	
	//Initialize computer GPIB
	initialize(computerAddr, 0);

	while(1);

	return 0;
}