import java.util.Scanner;

public class OperacoesMatematicasEmJava {
	public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
		
		System.out.println("Digite o primeiro número: ");
		int n1 = input.nextInt();		
	    System.out.println("Digite o segundo número: ");
	    int n2 = input.nextInt();
				
		int soma = n1 + n2;
		int multip = n1 * n2;
		int divisao = n1 / n2;
		int subtracao = n1 - n2;
		int resto = n1 % n2;

		System.out.println("A soma é igual a: " + soma);
		System.out.println("A multiplicação é igual a: " + multip);
		System.out.println("A divisão é igual a: " + divisao);
		System.out.println("A subtração é igual a: " + subtracao);
		System.out.println("O resto da divisão é igual a: " + resto);
		
		input.close();
	}

}
