// Recebe a string e o valor a ser buscado
function confirmEnding(str, target) {
  // Cria uma variável com o tamanho da busca
  let search = target.length;
  // Usa a função substring com o valor do tamanho da busca
  // Só que negativo. Como queremos sabere se o padrão buscado
  // Está no final da string, usando o negativo ele busca a partir
  // do final do array até atingir o tamanho da busca.
  if (str.substr(-search) == target) {
    return true;
  } else {
    return false;
  }
}

// A função .endsWidth() faz o mesmo trabalho da função 
// acima, mas a intenção desse exercício é treinar lógica
// E algoritmo 
/*function confirmEnding(str, target) {
  if(str.endsWith(target)){
    return true;
  }else{
    return false;
  }
}*/

confirmEnding("Bastian", "n");