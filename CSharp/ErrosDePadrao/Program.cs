using System;

namespace ErrosDePadrao
{
    class Program
    {
        static void Main(string[] args)
        {
            string orderStream = "B123,C234,A345,C15,B177,G3003,C235,B179";
            //string[] codes = string[orderStream.Length];
            string[] codes = orderStream.Split(',');

            for (int i = 0; i < codes.Length; i++)
            {
                if(codes[i].Length != 4)
                {
                    codes[i] = $"{codes[i]}\t - Error";
                }

                Console.WriteLine(codes[i]);
            }
        }
    }
}
