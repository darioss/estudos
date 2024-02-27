// Deve varrer o array passado como argumennto
// e retirar todos os tipos de valores que são
// falsos em javascript false, null , o, "", undefined e NaN
// o Array original não deve ser modificado

function bouncer(arr) {
  // Cria um array vazio para receber os a serem retornados
  let result = [];
  // Varre o array
  for (let i = 0; i < arr.length; i++) {
    // Verifica se o valor guardado na posição é verdadeiro
    if (arr[i]) {
      // Se for verdadeiro adiciona ao array result
      result.push(arr[i]);
    }
  }
  console.log(result)
  // retorna o novo array apenas com dados verdadeiros em javascript
  return result;
}
bouncer([7, "ate", "", false, 9]);