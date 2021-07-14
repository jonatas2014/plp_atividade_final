//um pra muitos
public class Dependente{
    public int Id { get; set; }
    public string Nome { get; set; }
}
public class Pessoa{
    public int Id { get; set; }
    public string Nome { get; set; }
    public List<Dependente> Dependentes;

    public void Imprimir(){
        Console.WriteLine(" .: Pessoa :. ");
        Console.WriteLine(" Id      : " + this.Id);
        Console.WriteLine(" Nome : " + this.Nome);
        Console.WriteLine(" ----- Dependentes ----- ");
        
        //foreach não precisadefinir uma condição de parada
        foreach(Dependente d in Dependentes){
            Console.WriteLine("Dependente : " + d.Nome);
        }
    }
}
