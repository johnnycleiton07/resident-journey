package heranca;

public class Caminhao extends Veiculo{
	
	private boolean buzina;
	
	public Caminhao(String marca, String modelo, int ano, boolean buzina) {
		super(marca, modelo, ano);
		this.buzina = buzina;
	}
	
	public boolean GetBuzina() {
		return buzina;
	}
	
	public void setBuzina(boolean buzina) {
		this.buzina = buzina;
	}
	
	
	public static void main(String[] args) {
		Caminhao meuCaminhao = new Caminhao("Scania", "AB", 2009, true);
		System.out.printf("O caminhão " + meuCaminhao.getMarca() + " " + meuCaminhao.getModelo() +  " do ano " + meuCaminhao.getAno() + ((meuCaminhao.GetBuzina() ? " tem buzina" : " não tem buzina")));
	}

}
