
public class Jogador {
	
	private final int maxVidas = 3;
	private int vidas = 0;
	private int num = 0;
	
	// Construtor da classe
	public Jogador(int num) {
		this.num = num;
		this.vidas = 3;
		System.out.printf("%nJogador número %d criado%n", num);
	}
	
	// Get - obter valores
	public int getVidas() {
		return this.vidas;
	}
	
	public int getNum() {
		return this.num;
	}
	
	// Set - atribuir valores
	public void setVidas() {
		if (this.vidas > maxVidas) {
			this.vidas = maxVidas;
		} else if (this.vidas < 0) {
			this.vidas = 0;
		}
		
	}
}
