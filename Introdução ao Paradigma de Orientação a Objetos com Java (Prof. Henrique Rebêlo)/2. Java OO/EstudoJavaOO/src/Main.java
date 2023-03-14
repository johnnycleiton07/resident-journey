
public class Main {
	
	public static void main(String[] args) {
		
		int num = 0;
		
		// new é o que faz a instanciação da classe
		Jogador j1 = new Jogador(++num);
		Jogador j2 = new Jogador(++num);
		
		System.out.printf("O jogador número 1 possui %d vidas%n", j1.getVidas());
		System.out.printf("O jogador número 2 possui %d vidas%n", j2.getVidas());
		
	}

}
