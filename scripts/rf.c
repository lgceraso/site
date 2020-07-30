#include <stdio.h>
int main(int argc,char **argv){
    char c;
    FILE *fp;
    if ((fp = fopen(argv[1],"r")) == NULL){
        printf("-> Error while opening the file!\n");
        return 1;
    }
    while((c = fgetc(fp)) != EOF)
        putchar(c);
    fclose(fp);
}
