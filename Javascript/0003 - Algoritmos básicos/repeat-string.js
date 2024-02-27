// Repetir uma string n vezes mas sem usar o método
// .repeat(). Montando uma lógica para que retorne 
// o número de repetições repassado. Em caso de valor
// Menor ou igual a zero, deve retornar uma string vazia

function repeatStringNumTimes(str, num) {
  // Cria uma variável com uma string vazia
  // para servir de  holder para armazenar a
  // string final a ser retornada
  let holder = "";
  // Se o numero é positivo
  if (num > 0) {
    // Conta de zero até numero e 
    for (let i = 0; i < num; i++) {
      // Contatena o valor da string na variável holder
      holder += str;
    }
  }

  // Atribui holder a variável str que será retornada.    
  // Qualquer valor menor ou igual a zero retornará str = ""
  // pois holder foi que é atribuido a str foi decalrado como
  // String vazia e a única situação em que seu valor é modificado 
  // é no caso de valores positivos.
  str = holder;
  return str;
}

repeatStringNumTimes("abc", 0);
repeatStringNumTimes("&", 3);

console.log("Passou aqui: " + repeatStringNumTimes("abc", 5));