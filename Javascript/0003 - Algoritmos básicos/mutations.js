// A função mutation recebe um array contendo duas strings
// E verifica se a primeira contem todas as letras da segunda
function mutation(arr) {
  // Como abaixo será usada a função .includes() que diferencia
  // Maiúscula de minúscula, as duas posições são transformadas
  // para lowercase
  let target = arr[0].toLowerCase();
  let dart = arr[1].toLowerCase();

  // Variável onde será montado o resultado da comparação
  let result = "";
  //Para cada letra da segunda string
  for (let i = 0; i < dart.length; i++) {
    // Se essa letra (de dart) estiver incluida na primeira 
    // string (target), é incluída na variável result
    if (target.includes(dart[i])) {
      result += dart[i];
    }
  }
  console.log("Segunda string: " + dart);
  console.log("Resultado: " + result);
  console.log("São iguais?");
  console.log(result == dart ? true : false);
  // retorna verdadeiro se result for exatamente igual a dart
  // ou false se forem diferentes.
  return result == dart ? true : false;
}

mutation(["hello", "Hello"]);