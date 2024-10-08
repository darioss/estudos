using System;

namespace ErrosDePadrao
{
    class Program
    {
        static void Main(string[] args)
        {
            /************************************************************
            *********           ANALISE DE PADRAO           *************
            ************************************************************/
            string orderStream = "B123,C234,A345,C15,B177,G3003,C235,B179";
            string[] codes = orderStream.Split(',');

            for (int i = 0; i < codes.Length; i++)
            {
                if (codes[i].Length != 4)
                {
                    Console.WriteLine($"{codes[i]}\t - Pattern Error");
                }
                else
                {
                    Console.WriteLine(codes[i]);
                }
            }

            /************************************************************
            ***********            JOGO DO PIN              *************
            ************************************************************/
            int counter = 0;
            for (int i = 1; i <= 100; i++)
            {
                if (counter == 3)
                {
                    Console.WriteLine("Pin");
                    if (i < 100)
                        Console.WriteLine(i);
                    counter = 1;
                }
                else
                {
                    Console.WriteLine(i);
                    counter++;
                }
            }

            /************************************************************
            ************            PA PA PA               **************
            ************************************************************/
            Random random = new Random();
            int aleatorio = random.Next(0, 9);
            int contador = 1;
            while (aleatorio != 3)
            {
                Console.WriteLine($"É {contador} pá pá pá");
                aleatorio = random.Next(0, 9);
                contador++;
            }
            Console.WriteLine("Achou o 3!");

            /************************************************************
            *********            BUBLE SORTING              *************
            ************************************************************/
            int[] numeros = { 6, 5, 3, 1, 8, 7, 2, 4, 0, 21, 17, 11, 150, -3 };
            Console.WriteLine("Buble Sorting");

            //Faz a reordenação dos números com Buble Sorting
            foreach (int numero in numeros)
            {
                for (int passos = 0; passos <= numeros.Length - 1; passos++)
                {
                    if ((passos + 1) < numeros.Length)
                    {
                        if (numeros[passos] > numeros[passos + 1])
                        {
                            int holder = numeros[passos];
                            numeros[passos] = numeros[passos + 1];
                            numeros[passos + 1] = holder;
                        }
                    }
                }
            }
            //Imprime o resultado na tela
            string sorted = string.Join(',', numeros);
            Console.WriteLine($"Buble sorted: {sorted}");

        }
    }
}
