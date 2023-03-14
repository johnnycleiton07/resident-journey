package heranca;

public class Veiculo {
	private String marca;
	private String modelo;
	private int ano;
	
	// Construtor -> atalho ctrl+3 (e digita gtuf + enter)
	public Veiculo(String marca, String modelo, int ano) {
		this.marca = marca;
		this.modelo = modelo;
		this.ano = ano;
	}

	// Gets -> obter valores
	public String getMarca() {
		return marca;
	}
	
	public String getModelo() {
		return modelo;
	}
	
	public int getAno() {
		return ano;
	}	

}
