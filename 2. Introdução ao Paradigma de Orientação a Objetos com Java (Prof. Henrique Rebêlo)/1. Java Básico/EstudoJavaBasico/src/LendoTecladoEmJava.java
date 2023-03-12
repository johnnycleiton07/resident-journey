import java.util.Scanner;
public class LendoTecladoEmJava {
	public static void main(String[] args) {
		Scanner texto = new Scanner(System.in);
		
		System.out.print("Digite seu nome: "); 
		String name = texto.nextLine();
		  
		System.out.println("Qual a sua idade?"); 
		int age = texto.nextInt();
		  
		System.out.printf("%s, você tem %d anos!", name, age);
		
		texto.close();
	}
}

