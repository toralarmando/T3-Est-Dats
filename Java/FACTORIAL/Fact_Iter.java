package fact_iter;
import java.util.Scanner;

//Este programa sirve para calcular el factorial de un numero por el metodo iterativo en JAVA
//PAra detener el programa se debe poner 0, eso te arrojara un mensaje que indica que el numero es invalido

public class Fact_Iter {
    
    public static void main(String[] args) {
       
        Scanner sc = new Scanner (System.in);
        int n;
        do{
            System.out.println("Introduzca un numero: ");
            n =  sc.nextInt();
            if (n != 0) {
                System.out.println("El Factorial de tu numero es: " + FactIterativo(n));
                System.out.println(" ");
            }
        } while (n != 0);
        System.out.println("Numero no valido");
    }
    
    public static int FactIterativo (int n) {
        int r = 1;
        for (int i = 2; i <= n; i++) {
            r = r * i;
        }
        return r;
    }
}
