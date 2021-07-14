public class Pai{
    public string Nome = "Roberto";
    public int Idade = 37;
}
public class Filha : Pai{
    public string Nome = "Paula";
    public int Idade = 17;

    public void mostrar(){
        console.WriteLine("Nome Filha: "+ Nome);
        console.WriteLine("Nome Pai: "+ base.Nome);
        console.WriteLine("Idade Filha: "+ Idade);
        console.WriteLine("Idade Pai: "+ base.Idade);
    }
}
