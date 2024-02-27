function reverseString(str) {
  // Atribui o tamanho da string a variável count
  let count = str.length;
  // Cria uma variável de apoio como uma string vazia
  let holder = "";
  // Enquanto count for maior que zero o laço continua rodando
  while (count > 0) {
    // Concatena o valor da variável holder com o valor existente
    // na posição (count-1) da str, lembrando que o valor começa
    // com o tamanho da string e diminui em 1 a cada vez que o 
    // laço executa.
    holder += str[count - 1];
    // Diminui em 1 o valor do count
    count--;
  }
  // atribui o valor final de holder a string str
  str = holder;
  // retorna o valor final de str contendo a string invertida
  return str;
}

reverseString("hello");

console.log(reverseString("O encontro do noivo com a igreja será, tão lindo. Aleluia! E ali nós o adoraremos, será tão lindo. Aleluia!"));