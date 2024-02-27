// gcc -fno-stack-protector -o main main.c -w
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define BUF_SIZE 0x80
typedef struct payload{
	char name[0x400];
    int size;
    char buf[0x80];
} payload;
void win(){
    system("/bin/sh");
}
void vul(char *chunk){
    int size = BUF_SIZE;
    payload input;
    read(0,&input,sizeof(input));
    if(input.size > size)
        printf("Overflow!\n");
    else{
        memcpy(chunk,input.buf,input.size); // Overflow 0x40 bytes
    }
}
int main(int argc, char* argv[]){
    setvbuf(stdout,0,2,0);
    printf("%p\n",win);
    char * chunk[BUF_SIZE];
    vul(chunk);
}