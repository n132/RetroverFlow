// gcc -z lazy -o main main.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#define BUF_SIZE 0x80
typedef struct payload{
	char name[0x400];
    int size;
    char buf[0x80];
} payload;
void win(){
	system("/bin/sh");
}

int main(int argc, char* argv[]){
    size_t target = mmap(0xdeadbeef000,0x1000,7,0x21,0,0);
    int size = BUF_SIZE;
    payload input;
    read(0,&input,sizeof(input));
    if(input.size > size)
        printf("Overflow!\n");
    else{
        char * chunk = malloc(BUF_SIZE);
        printf("[+] %p\n",chunk);
        memcpy(chunk,input.buf,input.size);
	if(target==(size_t)malloc(0))
		win();
    }
}
