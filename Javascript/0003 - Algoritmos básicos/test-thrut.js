function findElement(arr, func) {
  // Define num como undefined. Essa é a resposta padrão
  // Se não se enquadrar nas condições no if, retornará 
  // undefined para num
  let num = undefined;
  // Percorre o array para verificar cada posição
  for (let i = 0; i < arr.length; i++) {
    // Testa para a posição se o valor existente no array
    // recebido como parâmetro do método retorna true na 
    // função recebida no método.
    // Deve retornar true já na primeira ocorrência de um 
    // valor que satisfaça a função.
    if (func(arr[i]) == true) {
      // Atribui o valor dessa posição a num e quebra
      // interrompe o laço
      num = arr[i];
      break;
    }
  }
  return num;
}
findElement([1, 2, 3, 4], num => num % 2 === 0);
console.log(findElement([-13, 3, 5, 9], num => num % 2 === 0));