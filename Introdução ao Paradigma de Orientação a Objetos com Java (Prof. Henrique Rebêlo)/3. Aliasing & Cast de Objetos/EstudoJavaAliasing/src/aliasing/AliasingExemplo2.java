package aliasing;

public class AliasingExemplo2 {
	
	public static void main(String[] args) {
		//Utilize tipos de dados imutáveis (Integer e String)
		int x = 10;
		Integer y = x;
		
		System.out.println("O valor de x é: " + x);
		System.out.println("O valor de y é: " + y);
		
		x++;
		
		System.out.println("Depois da alteração em X:");
		System.out.println("O valor de x é: " + x);
		System.out.println("O valor de y é: " + y);
		
	}

}
