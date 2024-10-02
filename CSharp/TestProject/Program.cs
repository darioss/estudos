using System;

namespace TestProject
{
    class Program
    {
        static void Main(string[] args)
        {
            //Exercício 1
            string[] names = {"Alex", "Eddie", "David", "Michael"};
            
            foreach(var name in names)
            {
                Console.WriteLine(name);
            }
            
            for( int i = names.Length - 1; i >=0; i--)
            {
                if(names[i]=="David") names[i] ="Sammy";
            }

            Console.WriteLine("-------------------------------------");

            foreach(var name in names)
            {
                Console.WriteLine(name);
            }

            //Exercício 2
            bool flag = true;
            int value = 0;
            if(flag)
            {
                Console.WriteLine($"Dentro do Bloco de código: {value}");
            }

            value = 10;
            Console.WriteLine($"Fora do Bloco de código: {value}");

            //Exercício 3
            int x=5;
            if(x>0)
            {
                int y = 6;
                x +=y;
            }
            Console.WriteLine(x);

            //Exercício 4
            if(flag) 
                Console.WriteLine(flag);

            //Exercicio 5
            Console.WriteLine("Exercício 5");
            Console.WriteLine("a" == "a"); //true
            Console.WriteLine("a" == "A"); //False
            Console.WriteLine(1 == 2); //False
            Console.WriteLine('a' == 'A'); //False    

            string MeuValor = "a";
            Console.WriteLine(MeuValor == "a"); //True
            Console.WriteLine(MeuValor == "A"); //False

            //Exercício 6
            Console.WriteLine("Exercício 6");
            string Valor1 = "Hoje é Quarta-feira!";
            string Valor2 = "hoje é Quarta-feira! ";
            Console.WriteLine(Valor1.ToLower().Trim() == Valor2.ToLower().Trim()); //True
            Console.WriteLine("a" != "a"); //False
            Console.WriteLine("a" != "a "); //true

            //Exercício 7
            Console.WriteLine(Valor1.ToLower().Contains("quarta"));

            //Exeercício 8
            Console.WriteLine("Cara ou Coroa");
            Random random = new Random();
            int numeroAleatario = random.Next(0, 2);
            Console.WriteLine(numeroAleatario == 0 ? "Cara" : "Coroa");

            //Exercício 9
            Console.WriteLine("Gerenciamento de acesso");

            string permissao = "Administrador|Gerente";
            int nivel = 56;

            if(permissao.ToLower().Contains("administrador"))
            {
                if(nivel > 55)
                {
                    Console.WriteLine("Bem-vindo Super Administrador!");
                }
                else
                {
                    Console.WriteLine("Bem-vindo Administrador!");
                }
            }
            else if(permissao.ToLower().Contains("gerente"))
            {
                if(nivel >= 20)
                {
                    Console.WriteLine("Entre em contato com o Administrador!");
                }
                else
                {
                    Console.WriteLine("Você não tem privilégios suficientes!");
                }
            }
            else
            {
                Console.WriteLine("Você não tem privilégios suficientes!");
            }

            //Exercício 10
            Random Aleatorio = new Random(); 
            int Aposta = 3;
            int Sorteado = 0;
            int Tentativas = 1;
            bool Venceu = false;

            Console.WriteLine($"Você apostou no número {Aposta}");
            do{
                if(Tentativas < 4)
                {
                    Sorteado = Aleatorio.Next(1,11); //Um número aleatório de 1 a 10
                    Console.WriteLine($"Sorteio {Tentativas}:");
                    Console.WriteLine($"O número sorteado foi {Sorteado}");
                    Tentativas++;

                    if(Aposta == Sorteado)
                        Venceu = true;
                }
                else
                {
                    Console.WriteLine("Você perdeu");
                    break;
                }
                
            }while(Sorteado != Aposta);

            if(Venceu)
                Console.WriteLine("Você venceu");


            // Exercício 11
            Random randomico = new Random();
            int current = randomico.Next(1,11);
            int counter = 0;
            while(current >= 3){
                current = randomico.Next(1, 11);
                counter++;
            }
            Console.WriteLine($"Passou no laço {counter} vezes!");
            Console.WriteLine($"Current atual é: {current}");
        }
    }
}
