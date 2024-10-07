using System;

namespace InverterPalavrasNumaFrase
{
    class Program
    {
        static void Main(string[] args)
        {
            //Inverter as letras das palavras sem modificar a posição da
            //Palavra na frase abaixo
            string pangram = "The quick brown fox jumps over the lazy dog";
            
            //Cria um array de strings com cada palavra ocupando uma posição
            string[] palavras = pangram.Split(" ");
            
            //Cria um array vazio com o tamanho do array paralavras, 
            //para receber em cada posição a palavra invertida
            string[] invertida = new string[palavras.Length];

            //Itera sobre cada palavra do array
            for (int i = 0; i < palavras.Length; i++)
            {
                //Cria um array de caracteres para armazenar 
                //cada posição da palavra corrente no FOR
                char [] letras = palavras[i].ToCharArray();

                //Inverte o array de letras
                Array.Reverse(letras);

                //Armazena O array letras como string no
                //Array de strings "invertida"
                invertida[i] = new string(letras);
            }
            
            //Cria ums string chamada resultado que recebe os valores 
            //do array de strings "invertida", separados por espaços
            string resultado = String.Join(" ", invertida);
            
            //Imprime no console a frase na posição original,
            //mas com as letras das palavras invertidas
            Console.WriteLine(resultado);
        }
    }
}
