package heranca;

public class Moto extends Veiculo{
	
	private int numeroDeRodas;
	
	// Construtor
	public Moto(String marca, String modelo, int ano, int numeroDeRodas) {
		super(marca, modelo, ano);
		this.numeroDeRodas = numeroDeRodas;
	}
	
	// Gets
	public int getNumeroDeRodas() {
		return numeroDeRodas;
	}
	
	// Método Main
	public static void main(String[] args) {
		// Instanciar a classe
		Moto hb20 = new Moto("HB20", "aquela lá", 0, 2);
		System.out.printf("O modelo da moto é %s", hb20.getModelo());
	}
	

}
