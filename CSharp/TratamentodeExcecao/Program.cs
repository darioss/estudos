using System;
using System.Diagnostics;
using System.Globalization;

namespace TratamentodeExcecao
{
    class Program
    {
        static void Main(string[] args)
        {

            string numberOne = "7";
            string numberTwo = "5";

            int sum = int.Parse(numberOne) + int.Parse(numberTwo);
            Console.WriteLine(sum);

            string value = "102";
            int result = 0;

            if (int.TryParse(value, out result))
            {
                Console.WriteLine($"O valor é: {result}");
            }
            else
            {
                Console.WriteLine("Impossível obter o valor");
            }
            Console.WriteLine($"O valor é (w/offset): {50 + result}");

            string[] valores = {"12.3", "45", "ABC", "11", "DEF"};
            decimal total = 0m;
            string message = "";

            foreach(var valor in valores)
            {
                decimal valorCorrente;
                //Para transformar de string para decimal, é necessário incluir NumberStyle e Cultureinfo
                if(decimal.TryParse(valor, NumberStyles.Any, CultureInfo.InvariantCulture, out valorCorrente))
                {
                    total += valorCorrente;
                }
                else
                {
                    message += valor;
                }
            }

            Console.WriteLine($"Message: {message}");
            Console.WriteLine($"Total: {total}");

            int numero1 = 11;
            decimal numero2 = 6.2m;
            float numero3 = 4.3f;
            decimal resultado1 = (decimal)numero1/numero2;
            resultado1 = Convert.ToInt32(resultado1);
            Console.WriteLine(resultado1);
            decimal resultado2 = numero2/Convert.ToDecimal(numero3);
            Console.WriteLine(resultado2);
            float resultado3 = numero3/numero1;
            Console.WriteLine(resultado3);


            string[] pallets = {"B14", "A11", "B12", "A13"};
            Console.WriteLine("Sorted...");
            Array.Sort(pallets);
            foreach(var pallet in pallets)
            {
                Console.WriteLine($"-- {pallet}");
            }
            Console.WriteLine("Reversed");
            Array.Reverse(pallets);
            foreach(var pallet in pallets)
            {
                Console.WriteLine($"-- {pallet}");
            }

            Console.WriteLine("Resizing --------------------------");
            Array.Resize(ref pallets, 6);
            Console.WriteLine($"Resizing 6 ... count {pallets.Length}");
            pallets[4] = "C01";
            pallets[5] = "C02";
            foreach(var pallet in pallets)
            {
                Console.WriteLine($"--{pallet}");
            }

            Console.WriteLine("Clearing --------------------------");
            Array.Clear(pallets, 0, 2);
            Console.WriteLine($"Clearing 2 ... Count: {pallets.Length}");
            foreach(var pallet in pallets)
            {
                Console.WriteLine($"--{pallet}");
            }

            Console.WriteLine("Converter string em array de caracteres");
            string listaString = "abc123";
            char[] valueArray = listaString.ToCharArray();
            foreach(var caracter in listaString)
            {
                Console.WriteLine($"{caracter}\n");
            }

            Console.WriteLine("Reverter a matriz de caracteres e criar uma string");
            Array.Reverse(valueArray);
            string novaString = new string (valueArray);
            string novaString2 = string.Join(", ", valueArray); //Cria uma string de caracteres separados por vírgula
            Console.WriteLine(novaString);
            Console.WriteLine(novaString2);

            Console.WriteLine("Split()");
            string frase = "a, b, c, 1, 2, 3";
            string[] palavras = frase.Split(',');
            foreach(string palavra in palavras)
            {
                Console.WriteLine($"{palavra}");
            }

            Console.WriteLine("Signed integral types:");
            Console.WriteLine($"sbyte  : {sbyte.MinValue} to {sbyte.MaxValue}");
            Console.WriteLine($"short  : {short.MinValue} to {short.MaxValue}");
            Console.WriteLine($"int    : {int.MinValue} to {int.MaxValue}");
            Console.WriteLine($"long   : {long.MinValue} to {long.MaxValue}");
            Console.WriteLine("");
            Console.WriteLine("Unsigned integral types:");
            Console.WriteLine($"byte   : {byte.MinValue} to {byte.MaxValue}");
            Console.WriteLine($"ushort : {ushort.MinValue} to {ushort.MaxValue}");
            Console.WriteLine($"uint   : {uint.MinValue} to {uint.MaxValue}");
            Console.WriteLine($"ulong  : {ulong.MinValue} to {ulong.MaxValue}");
            Console.WriteLine("");
            Console.WriteLine("Floating point types:");
            Console.WriteLine($"float  : {float.MinValue} to {float.MaxValue} (with ~6-9 digits of precision)");
            Console.WriteLine($"double : {double.MinValue} to {double.MaxValue} (with ~15-17 digits of precision)");
            Console.WriteLine($"decimal: {decimal.MinValue} to {decimal.MaxValue} (with 28-29 digits of precision)");
            //Funciona em modo Debug
            Debug.WriteLine("Testando Debug");
            Trace.WriteLine("Testando Trace");

            int n2 = 3;
            Debug.Assert(n2 == 5, "The return value is not 5 and it should be.");
            Debug.WriteIf(n2 == 3, "Count should not be 0.");
        }
    }
}
