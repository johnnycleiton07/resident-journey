import java.util.Scanner;

public class CondicionaisEmJava {
	public static void main(String[] args) {
		Scanner opcao = new Scanner(System.in);
		
		System.out.println("Digite S para sim e N para não:");
		char c = opcao.next().charAt(0);
		
		if (c == 's') {
			System.out.println("Você optou por votar SIM!");
			
		} 
		else if (c == 'n') {
			System.out.println("Você optou por votar NÃO!");
		}
		else {
			System.out.println("Digite uma opção válida!");
		}
		
		opcao.close();
	}

}
