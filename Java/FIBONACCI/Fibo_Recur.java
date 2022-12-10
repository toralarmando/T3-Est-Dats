package fibo_recur;
import java.util.Scanner;

//PROGRAMA PARA CALCULAR UN NUMERO DE LA SERIE FIBONACCI POR METODO RECURSIVO EN JAVA
//EN ESTE CASO AL INGRESAR EL NUMERO SE DEBE TENER EN CUENTA QUE EL 0 TAMBIEN CUENTA EN LA SERIE
//POR ENDE SI TU NUMERO QUE DESEAS BUSCAR EN LA SERIE ES 10, DEBERAS INGRESAR EL NUMERO 11
//ESTO PARA QUE TE APAREXCA EN LA SERIE FIBONACCI HASTA EL NUMERO 10, QUE SERIA 55

public class Fibo_Recur {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        System.out.println("Introduce el numero: ");
        int numero = teclado.nextInt();
        teclado.close();
        for (int i = 0; i < numero; i++) {
            System.out.print(" " + fibonacci(i));
            System.out.println("");//ESTO SE PONE NADAMAS POR ESTETICA, YA QUE EL PROGRAMA TERMINA EN DONDE SE QUEDA EL ULTIMO NUMERO
        }
    }
    
    public static int fibonacci (int numero) {
        if ((numero == 0) || (numero == 1)) {
            return numero;
        } else 
            return fibonacci(numero - 1) + fibonacci(numero - 2);
    }      
}