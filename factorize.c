#include "factors.h"

int factorize(char *buffer)
{
	u_int32_t num, i;

	num = atoi(buffer);

	for (i = 2; i < num; i++)
	{
		if (num % i == 0)
		{
			printf("%d=%d*%d",num,num/i,i);
			break;
		}
	}
	return (0);
}
