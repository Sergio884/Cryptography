n = 26

int main(void){
	int n;
	printf("Ingresa el tamaño del alfabeto: ");
	scanf("%d",&n);
	llave(n);
	return 0;
}

i = 0
j = 0

#Se crea una matriz  3X3 inversa vacia
key = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        k[i][j]= random.randint(0,n)%a

int llave(int a){
	int i, j;
	int k[3][3];
	printf("Matriz propuesta:\n");
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			k[i][j]=rand()%a;
			printf("\t%d", k[i][j]);
		}
		printf("\n");
	}
	if(gcd(det(k[i][j])%a,a)==1)){
		llave(a);
	}
	return k[i][j];
}

int det(int m[i][j]){
	int d;
	d = (m[0][0]*m[1][1]*m[2][2])+(m[0][1]*m[1][2]*m[2][0])+(m[0][2]*m[1][0]+m[2][1])-(m[0][0]*m[1][2]*m[2][1])+(m[0][1]*m[1][2]*m[2][2])+(m[0][2]*m[1][1]*m[2][2]);
	return d;
}

int gcd (int n, int d){
	int temporal;
    while (d != 0) {
        temporal = d;
        d = n % d;
        d = temporal;
    }
    return d;
}