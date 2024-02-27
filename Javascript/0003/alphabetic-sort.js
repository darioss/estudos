function sortAlphabetic(arr) {
  for (let i = 0; i < arr.length; i++) {
    let x, y = 0;
    for (let j = 0; j < arr.length; j++) {
      // Se mudar para >= ordena na ordem decrescente. 
      // @TODO - implementar um segundo parâmetro ao método para escolha da
      // ordem crescene ou decrescente
      if (arr[i] <= arr[j]) {
        x = arr[i];
        y = arr[j];
        arr[i] = y;
        arr[j] = x;
      }
    }
  }
  console.log(arr);
  if (arr[0] > arr[1]) {
    sortAlphabetic(arr);
  }

  return arr;
}

sortAlphabetic([40, 60, 3, 5, 10, 5]);
sortAlphabetic(['z', 'y', 'j', 'a', 'c']);
sortAlphabetic([10, 20, 30, 40, 50, 35]);