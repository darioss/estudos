using System;

namespace SistemaDeNotas
{
    class Program
    {
        static void Main(string[] args)
        {
            // Numero padrão de avaliações, sem notas de trabalhos extras
            int currentAssignments = 5;
            int alunoCorrente = 0;

            int[] notasSophia = new int[] { 90, 86, 87, 98, 100, 85, 68, 90 };
            int[] notasAndrew = new int[] { 92, 89, 81, 96, 90 };
            int[] notasEmma = new int[] { 90, 85, 87, 98, 68, 89, 62, 17 };
            int[] notasLogan = new int[] { 90, 95, 87, 88, 96 };
            string[] alunos = new string[] { "Sophia", "Andrew", "Emma", "Logan" };
            // Inclui a quantidade de avaliações padrões e mais notas extras, tatalozando 
            // no máximo 10 notas
            int[] notasEstudante = new int[10];
            string letraNota ="";
            decimal mediaAluno;
            decimal notasProvas = 0;
            int creditosExtra = 0;
            int pontos = 0;

            Console.WriteLine("Student\t\tExamScore\tOverall\t\tGrade\t\tExtra Credit");
            Console.WriteLine("----------------------------------------------------------------------------");
            foreach (var aluno in alunos)
            {
                if (aluno == "Sophia")
                {
                    notasEstudante = notasSophia;
                }
                else if (aluno == "Andrew")
                {
                    notasEstudante = notasAndrew;
                }
                else if (aluno == "Emma")
                {
                    notasEstudante = notasEmma;
                }
                else if (aluno == "Logan")
                {
                    notasEstudante = notasLogan;
                }


                foreach (var nota in notasEstudante)
                {
                    alunoCorrente += nota;
                }

                if(notasEstudante.Length==currentAssignments)
                {
                    mediaAluno = (decimal)alunoCorrente / currentAssignments;
                }else
                {
                    mediaAluno = (decimal)alunoCorrente / notasEstudante.Length;
                }
                
                if(mediaAluno >= 97)
                {
                    letraNota = "A+";
                }
                else if (mediaAluno >= 93)
                {
                    letraNota = "A";
                }
                else if (mediaAluno >= 90)
                {
                    letraNota = "A-";
                }
                else if (mediaAluno >= 87)
                {
                    letraNota = "B+";
                }
                else if (mediaAluno >= 83)
                {
                    letraNota = "B";
                }
                else if (mediaAluno >= 80)
                {
                    letraNota = "B-";
                }
                else if (mediaAluno >= 77)
                {
                    letraNota = "C+";
                }
                else if (mediaAluno >= 73)
                {
                    letraNota = "C";
                }
                else if (mediaAluno >= 70)
                {
                    letraNota = "C-";
                }
                else if (mediaAluno >= 67)
                {
                    letraNota = "D+";
                }
                else if (mediaAluno >= 63)
                {
                    letraNota = "D";
                }
                else if (mediaAluno >= 60)
                {
                    letraNota = "D-";
                }
                else
                {
                    letraNota = "F";
                }

                //Define a média somente nas provas
                if(notasEstudante.Length >= currentAssignments)
                {
                    for(int i = 0; i < 5; i++)
                    {
                        notasProvas += notasEstudante[i];
                    }
                }
                else
                {
                    for(int i = 0; i < notasEstudante.Length; i++)
                    {
                        notasProvas += notasEstudante[i];
                    }
                }

                notasProvas = notasProvas/currentAssignments;


                Console.WriteLine($"{aluno}:\t\t{notasProvas} \t\t {mediaAluno}\t\t{letraNota}\t\t{creditosExtra} ({pontos} pts)");
                
                //Reseta as variáveis antes da próxima iteração
                alunoCorrente = 0;
                notasProvas = 0;

            }

            Console.WriteLine("\nPress the Enter key to continue");
            Console.ReadLine();
            /*
            97 - 100   A+
            93 - 96    A
            90 - 92    A-
            87 - 89    B+
            83 - 86    B
            80 - 82    B-
            77 - 79    C+
            73 - 76    C
            70 - 72    C-
            67 - 69    D+
            63 - 66    D
            60 - 62    D-
            0  - 59    F
            */
        }
    }
}
