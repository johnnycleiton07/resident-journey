package heranca;

public class Carro extends Veiculo{
	private int numeroDePortas;

	// Construtor
	public Carro(String nome, String modelo, int ano, int numeroDePortas) {
		super(nome, modelo, ano);
		this.numeroDePortas = numeroDePortas;
	}
	
	// Gets -> obter valores
	public int getNumeroDePortas(){
		return numeroDePortas;
	}
	
	// Método Main
	public static void main(String[] args) {
		// Criando o objeto carro e instanciando a classe
		Carro fiatUno = new Carro("Fiat", "Uno", 2012, 4);
		System.out.printf("A marca do carro é %s%n", fiatUno.getMarca());
		System.out.printf("A quantidade de portas desse carro é %d", fiatUno.getNumeroDePortas());
		
	}
	

}
