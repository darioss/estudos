using System;

namespace TestProject
{
    class Program
    {
        static void Main(string[] args)
        {
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
        }
    }
}
