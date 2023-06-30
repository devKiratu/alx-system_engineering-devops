#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int infinite_while(void);

/**
 * main - entry point
 * Creates 5 zombie processes
 * Return: 0 on success
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);

		i++;
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - keeps the parent process up
 * Return: void
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
