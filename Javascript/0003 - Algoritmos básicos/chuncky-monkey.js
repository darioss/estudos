// A função recebe dois parâmetros. O primeiro e um array
// O segundo é um numero de colunas que o array bidimensional
// deve ter
function chunkArrayInGroups(arr, size) {
  // Divide a quantidade de elementos do array pelo numero desejado
  // de colunas e arredonda o resultado para cima. Assim obtemos o
  // número de linhas da matriz. Para arredondar para cima é usada a 
  // função Math.ceil e fixado em zero a quantidade de casas demimais com
  // .toFixed.
  let lines = (Math.ceil((arr.length) / size).toFixed(0));
  // Variável que receberá o resultado a ser retornado
  let result = [];
  // Guarda a posição do ponteiro na interação sobre o array
  // passado como argumento
  let position = 0;

  //Monta o array bidimensional lines x size
  // Cria uma variável para contar as linhas
  let countLines = 0;
  //Monta cada linha
  while (countLines < lines) {
    // A cada interação é criada uma nova linha a ser incluída no array final
    let newLine = [];
    // popula as posições no array newLine
    for (let i = 0; i < size; i++) {
      // Se position é diferente do tamanho do array original e o valor nessa posição
      // É diferente de undefined, o valor dessa posição é adicionado ao array newLine
      if (arr[position] != arr.length && arr[position] != undefined) {
        newLine.push(arr[position]);
      }
      // Incrementa a posição do ponteiro que percorre o arr recebido como argumento
      position++;
    }
    // inclui o array newLine no array result
    result.push(newLine);
    // incrementa o contador de linhas
    countLines++;
  }
  console.log(result)
  // retorna o array bidimensional  
  return result;
}

chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4);