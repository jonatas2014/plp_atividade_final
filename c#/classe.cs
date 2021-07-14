using System;

namespace Examplo{
    //Construtor
    public struct Pessoa{
        public string Nome;
        public int Idade;
        public Pessoa(string nome, int idade){
            Nome = nome;
            Idade = idade;
        }
    }

    public class Application{
        static void Main(){
            // Crie uma instância de struct e inicialize usando "new".
            // A memória está alocada na pilha de threads.
            Pessoa p1 = new Pessoa("Alex", 9);
            Console.WriteLine("p1 Nome = {0} / Idade = {1}", p1.Nome, p1.Idade);

            // Crie um novo objeto de estrutura. Observe que a estrutura pode ser inicializada
            // Semusar o "new".
            Pessoa p2 = p1;

            // Atribuir valores a membros p2.
            p2.Nome = "Spencer";
            p2.Idade = 7;
            Console.WriteLine("p2 Nome = {0} / Idade = {1}", p2.Nome, p2.Idade);

            // Os valores de p1 permanecem inalterados porque p2 é uma cópia.
            Console.WriteLine("p1 Nome = {0} / Idade = {1}", p1.Nome, p1.Idade);
        }
    }
    /*
        Output:
        p1 Nome = Alex / Idade = 9
        p2 Nome = Spencer / Idade = 7
        p1 Nome = Alex / Idade = 9
    */
}
