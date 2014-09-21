#include <stdio.h>
#include <readline/readline.h>
#include <readline/history.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
char** str_split(char* a_str, const char a_delim)
{
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result)
    {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token)
        {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}

void fork_ls(){
	pid_t pid;
	/* fork another process */
  	pid = fork();
	char *const parmList[] = {"ls", "-l", NULL};
  	if (pid < 0) {
  	 	/* error occurred */
		fprintf(stderr, "Fork Failed"); 
		exit(-1);
	}else if (pid == 0) { 
		/* child process */ 
		execvp("/bin/ls",parmList);
	}else { 
		/* parent process */
  		/*parent will wait for sthe child to complete*/
    	wait (NULL);
    	printf ("Child Complete");
    	exit(0);
	}
	
}
void check_arg(char* reply, char** token){
	if (strlen(reply) < 2) {
		fprintf(stderr, "Usage: Would like some command-line arguments\n");
	}else{
		int i;
		//printf("------------------------------------------------\n");
		for (i = 0 ; *(token + i ); ++i) {
			//fprintf(stderr, "Argument No %d: %s\n", i, *(token+i));
		//	printf("token =%s\n",*(token+i));
			int ret;
			ret = strcmp(*(token+i), "ls");
			//printf("ret = %d",ret);
			if(ret == 0){
				printf( "in the loop , token = %s\n", *(token+i));
				fork_ls();
			}
			//free(*(token+i));
		}
		printf("------------------------------------------------\n");
	}
	
	printf("\nYou said: %s\n\n", reply);
}
int main()
{
	const char* prompt = "shell> ";
	char ** token;
	char *parmList1[];
	int bailout = 0;
	while (!bailout) {

		char* reply = readline(prompt);
		/* Note that readline strips away the final \n */
		/* For Perl junkies, readline automatically chomps the line read */

		if (!strcmp(reply, "bye")) {
			bailout = 1;
		} else {
			token = str_split(reply,' ');
			check_arg(reply,token);
		}
	
		free(reply);
	}
	printf("Bye Bye\n");
}
