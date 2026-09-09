// Teaching source for ret2canteen. Deployed binary is Python emulation (compatible).
// To use real ELF: gcc -no-pie -fno-stack-protector -o vuln vuln.c && chmod 4755 vuln
#include <stdio.h>
#include <unistd.h>
void win() {
  char f[128];
  FILE *fd = fopen("/flag","r");
  if(!fd){printf("no flag\n");return;}
  fgets(f,128,fd);
  printf("WIN: %s\n", f);
}
void vuln() {
  char buf[64];
  printf("Canteen order? ");
  fflush(stdout);
  read(0, buf, 256);
  printf("Got it.\n");
}
int main(){setbuf(stdout,NULL); vuln(); return 0;}
