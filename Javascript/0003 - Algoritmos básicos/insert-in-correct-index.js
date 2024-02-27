function getIndexToIns(arr, num) {
  if (!arr.includes(num)) {
    arr.push(num);
  }
  arr = sortAlphabetic(arr);
  num = arr.indexOf(num);
  console.log(num);
  return num;
}

// A função .sort() do javascript considera 10 < 5, por exemplo,
// pois o 1 vem antes do 5. Essa função que escrevi ordena em ordem crescente
// de forma correta.
function sortAlphabetic(arr) {
  for (let i = 0; i < arr.length; i++) {
    let x, y = 0;
    for (let j = 0; j < arr.length; j++) {
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

//sortAlphabetic([40, 60 ,3, 5, 10]);
console.log(sortAlphabetic([10, 20, 30, 40, 50, 35]))
//getIndexToIns([10, 20, 30, 40, 50], 35)

getIndexToIns([40, 60], 50);