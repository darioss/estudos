using System;

namespace ErrosDePadrao
{
    class Program
    {
        static void Main(string[] args)
        {
            /************************************************************
            *********             BUBLE SORTING            **************
            ************************************************************/
            int[] numeros = { 6, 5, 3, 1, 8, 7, 2, 4, 0, 21, 17, 11, 150,
            658, 12587, -658, 9875, 7, 10, 97, 9875685, -365874, -3 };
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
            Console.WriteLine($"Sorted: {sorted}");

            /************************************************************
            ************         PADRES E CANIBAIS          *************
            ************************************************************/
            
            /*
                OBJETIVO: Atravessar 3 padres e 3 canibais de barco para
                a outra margem do rio.
                Limitação: O número de padres nunca poderá ser menor que 
                o de canibais, caso contrário os canibais comerão o padre. 

                ---------------------- PASSO A PASSO -----------------------
                Passo 1: Um padre e um canibal entram no barco e atravessam
                Passo 2: O canibal desce do barco e o padre volta
                Passo 3: O padre desce e embarcam 2 canibais
                Passo 4: Um canibal desce na outra margem e o outro volta
                Passo 5: O canibal desce e sobem dois padres (ficando do
                lado de cá um padre e um canibal)
                Passo 6: Do lado de lá, um padre desce e sobe um canibal
                Passo 7: do lado de cá um padre sobe e um canibal desce
                Passo 8: do lado de lá descem os dois padres e sobe um canibal
                Passo 9: do lado de cá sobe um canibal e desce do outro lado
                passo 10: o barco volta com um canibal e pega o último canibal
            */
        }
    }
}

