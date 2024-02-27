// Este método retorna um array contendo os maiores
// Valores dos subarrays passados como parâmetro

function largestOfSubArrays(arr) {
  // Cria um array que receberá o maior valor de
  // cada subarray
  let max = [];
  // Percorre as linhas 
  for (let i = 0; i < arr.length; i++) {
    // Variável que guarda o maior valor do subarray
    let major = 0;
    // Percorre as colunas
    for (let j = 0; j < arr.length; j++) {
      // Atribui o valor à variável major e major
      // estiver zerado ou se o valor for maior que
      // o valor que já existe armazenado na variável
      if (major == 0 || arr[i][j] >= major) {
        major = arr[i][j]
      }
    }
    // Ao terminar de percorrer a linha, major tem o maior
    // valor encontrado na linha. Então esse valor é atribuído
    // ao array max na posição da coluna em que o laço está.
    max[i] = major;
  }
  arr = max;
  return arr;
}

largestOfSubArrays([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);

console.log(largestOfSubArrays([[-1, -23, 0, 12], [17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10], [-78, 7, 9, 150]])); 