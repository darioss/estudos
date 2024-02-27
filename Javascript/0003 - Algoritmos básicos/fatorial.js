function factorialize(num) {
  let result = 1;
  for (let i = 1; i <= num; i++) {
    result *= i;
  }
  num = result;
  return num;
}
factorialize(5);
console.log(factorialize(5));