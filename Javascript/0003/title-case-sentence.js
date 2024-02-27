function titleCase(str) {
  // Cria um array e atribui cada string a uma
  // posição desse array
  let holder = str.split(" ");
  // Percorre o array de strings criado
  for (let i = 0; i < holder.length; i++) {
    // Cria uma variável string de apoio que servirá
    // para montar a string tratada que substituirá a
    // original no array holder
    let string = "";
    // Percorre cada letra da string
    for (let j = 0; j < holder[i].length; j++) {
      // Se a posição for a inicial, concatena a letra
      // em caixa alta na variável string
      if (j == 0) {
        string += holder[i][j].toUpperCase();
      } else {
        // Se não, concatena em caixa baixa
        string += holder[i][j].toLowerCase();
      }
    }
    // Atribui a string ao array holder na posição i
    holder[i] = string;
  }
  // Cria a variável finalSring que recebe o conteúdo do 
  // Array holder e através da função .join converte o seu
  // conteúdo numa string
  let finalString = holder.join(" ");
  console.log(finalString);
  // Atrinui finalString a str que é a variável de retorno
  str = finalString;
  return str;
}