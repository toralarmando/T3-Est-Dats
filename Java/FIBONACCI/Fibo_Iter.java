package fibo_iter;
import java.util.Scanner;

//PROGRAMA PARA CALCULAR UN NUMERO DE LA SERIE FIBONACCI POR METODO ITERATIVO EN JAVA

public class Fibo_Iter {

    public static void main(String[] args) {
        int n1 = 0;
        int n2 = 1;
        Scanner sc = new Scanner(System.in);
        //SI EL NUMERO DE LA SERIE QUE QUIERES BUSCAR ES 10, EN EL PROGRAMA DEBERA PONER 11
        //ESTO PORQUE EN LA SERIE SE RESPETA EL 0
        //AUNQUE ESTO SE PUEDE ARREGLAR CAMBIADO LA VARIBALE n1 DE LA 8, LA CUAL TENDREMOS QUE CAMBIAR A 1
        //DE ESA FORMA SE VERA HASTA EL NUMERO QUE USTED PIDE EN LA SERIE
        System.out.print("Introduce el número de elementos a mostrar de la serie: ");
        int limite = sc.nextInt();  
 
        System.out.print(n1 + ", ");
        System.out.print(n2 + ", ");
 
        for(int i = 0; i<limite-2; i++){
            n2 = n1 + n2;
            n1 = n2 - n1;
            System.out.print(n2 + ", ");
        }
    }
}