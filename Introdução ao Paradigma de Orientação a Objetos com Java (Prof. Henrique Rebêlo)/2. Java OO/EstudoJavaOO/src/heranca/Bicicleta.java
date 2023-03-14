package heranca;

public class Bicicleta extends Veiculo{
	
	private boolean possuiAssento;
	
	public Bicicleta(String marca, String modelo, int ano, boolean possuiAssento) {
		super(marca, modelo, ano);
		this.possuiAssento = possuiAssento;
	}
	
	public boolean getPossuiAssento() {
		return possuiAssento;
	}
	
	public void setPossuiAssento(boolean possuiAssento) {
		this.possuiAssento = possuiAssento;
	}
	
	public static void main(String[] args) {
		Bicicleta minhaBike = new Bicicleta("Xtreme", "esporte", 2023, true);
		System.out.printf("A bicicleta da marca " + minhaBike.getMarca() + " é do modelo " + minhaBike.getModelo() + " e " + (minhaBike.getPossuiAssento() ? "possui assento" : "não possui assento"));
	}

}
