#!/usr/bin/perl   
=for comment
/***************************************************************
*   Fecha: Octubre 2023
*   Autor: J. Corredor
*   Modificado por: Alejandro Castro Martinez
*   Materia: Computación de Alto Rendimiento
*   Maestría en Ingenieria de Sistemas y Computación
*   Pontificia Universidad Javeriana
*   Objetivo: Herramienta para automatizar proceso de ejecución
*             por lotes los dos programas de multiplicacion de matrices. 
****************************************************************/
=cut


# Verifica si se proporciona un argumento en la línea de comandos
if(@ARGV[0]){
		$numRep = "$ARGV[0]";
}else{
		usage(); # Llama a la función 'usage' si no se proporciona un argumento
}

# Imprime el número de repeticiones
print "\n Repeticiones de la experimentación: $numRep \n\n";


# Obtiene el directorio actual y lo asigna a la variable $path0
$path0 = `pwd`;
chomp($path0);

# Encuentra la posición de la subcadena "/scripts" en el directorio actual
$T = index($path0,"/scripts");
# Obtiene una subcadena desde el inicio hasta la posición encontrada
$Path = substr($path0,0,$T);

# Definición de listas de ejecutables, núcleos y tamaños de vector
@Ejecutables = ("MM1c","MM1f"); 
@cores = ("1","2","4","8","10","14","16");
@VectorSize= ("100","200","400","600","800","1000","1500","2000","3000","4000");

# Bucles anidados para iterar sobre ejecutables, tamaños de vector y núcleos
foreach $exe (@Ejecutables){ 
    foreach $ves (@VectorSize){
        foreach $c (@cores) {
            # Construye el nombre del archivo de salida
            $file = "$Path/"."Soluciones/"."$exe"."-Size"."$ves"."-core"."$c";
            # Ejecuta el comando y redirige la salida al archivo
            for($i=0; $i<$numRep;  $i++){
                system("$Path/BIN/$exe $ves $c 0   >> $file");
                print "$Path/BIN/$exe $ves $c 0  \n" ;
            }
            # Se cierra el archivo
            close($file);
        }
    }
}

# Finaliza el script
exit(1);

# Subrutina para imprimir mensaje de uso incorrecto y salir del script
sub usage()
	{
		print "\n tst.pl: Uso incorrecto\n\n";
		print "\t revisar entradas o directorio de almacenaje \n\n\n";
		exit(1);
	}
       


