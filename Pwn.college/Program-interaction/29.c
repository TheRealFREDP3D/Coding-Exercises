#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

void pwncollege(char *argv[], char *env[])
{
    execve("/challenge/embryoio_level29", argv, env);
}

int main(int argc, char *argv[], char *env[])
{
    pid_t fpid;

    fpid = fork();
// Create a fork and save the PID, PID 0 will be child process which is what we want to wait on

        if (fpid == 0)
    { // If we are onto the child process
        pwncollege(argv, env);
    }
    else
    {
        waitpid(fpid, NULL, 0); // Wait for child process to run before parent terminates *HINT* wait literally waits for the child process before terminating the parent.. that is what it does
    }
    return 0;
}
