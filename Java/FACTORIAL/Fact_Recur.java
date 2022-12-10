package fact_recur;
import java.util.Scanner;

//Este programa es para calcular un numero factorial por metodo recursivo en JAVA
//PAra detener el programa se debe poner 0 ya que eso arroja un mensaje que indica que tu numero es invalido

public class Fact_Recur {

    public static void main(String[] args) {
      
        Scanner sc = new Scanner (System.in);
        int n;
        do{
            System.out.println("Introduzca un numero: ");
            n =  sc.nextInt();
            if (n != 0) {
                System.out.println("El Factorial de tu numero es: " + FactorialRecursivo(n));
                System.out.println(" ");
            }
        } while (n != 0);
        System.out.println("Numero no valido");
    }
        
    public static int FactorialRecursivo (int n) {
        if (n > 2){
            return n * FactorialRecursivo(n - 1);
        } else {
            return 2;
        }
    }
}
