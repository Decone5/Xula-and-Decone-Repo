#include <stdio.h>
#include <windows.h>
#include "headers/xunix.h"


int main(int argc, char const *argv[])
{
	printf("%s XUNIX DRIVE %d\n%s XUNIX PARTSIZE %d\n%s XUNISMS1 AT %d\n", OK, DRIVE, OK, PARTSIZE, OK, XUNIXMS1);
	printf("%s REDIR >> X.PY\n", OK);
	system("python x.py");
	return 0;
}
