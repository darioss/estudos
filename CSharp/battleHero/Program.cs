using System;

namespace battleHero
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            int heroPointsLife = 10;
            int heroAttackPoints = random.Next(1, 8);
            int monsterPointsLife = 10;
            int monsterAttackPoints = random.Next(1, 8);
            int initialAtack = random.Next(0, 2);
            int rodada = 1;

            if (initialAtack == 0)
                Console.WriteLine("O monstro começou atacando:");
            else
                Console.WriteLine("O herói começou atacando:");

            do
            {
                if (heroPointsLife <= 0)
                {
                    Console.WriteLine("O herói está morto!");
                    break;
                }


                Console.WriteLine($"\nRodada {rodada}");
                if (initialAtack == 0)
                {
                    heroPointsLife -= monsterAttackPoints;
                    Console.WriteLine($"O monstro causou um dano de {monsterAttackPoints}. Os pontos de vida do herói são: {heroPointsLife}");

                    if (heroPointsLife > 0)
                    {
                        monsterPointsLife -= heroAttackPoints;
                        Console.WriteLine($"O herói causou um dano de {heroAttackPoints}. Os pontos de vida do monstro são: {monsterPointsLife}\n");
                    }
                    else
                    {
                        Console.WriteLine("O herói está morto!");
                        break;
                    }
                }
                else
                {
                    monsterPointsLife -= heroAttackPoints;
                    Console.WriteLine($"O herói causou um dano de {heroAttackPoints}. Os pontos de vida do monstro são: {monsterPointsLife}\n");
                    if (monsterPointsLife > 0)
                    {
                        heroPointsLife -= monsterAttackPoints;
                        Console.WriteLine($"O monstro causou um dano de {monsterAttackPoints}. Os pontos de vida do herói são: {heroPointsLife}");
                    }
                    else
                    {
                        break;
                    }
                }
                rodada++;

            } while (monsterPointsLife > 0);

            if (monsterPointsLife <= 0)
            {
                Console.WriteLine("O monstro está morto!");
            }

        }
    }
}
