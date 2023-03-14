package heranca;

public class Onibus extends Veiculo{
	
	private int quantidadeDeAssentos;
	
	// Construtor
	public Onibus(String marca, String modelo, int ano, int quantidadeDeAssentos) {
		super(marca, modelo, ano);
		this.quantidadeDeAssentos = quantidadeDeAssentos;
	}
	
	// Gets
	public int quantidadeDeAssentos() {
		return quantidadeDeAssentos;
	}
	
	// Método Main
	public static void main(String[] args) {
		// Objeto instancia da Classe
		Onibus progresso = new Onibus("Mercedes", "articulado", 2014, 57);
		System.out.printf("O ônibus é da marca %s", progresso.getMarca());
	}
	

}
