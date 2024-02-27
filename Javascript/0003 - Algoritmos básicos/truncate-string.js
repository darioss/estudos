// Se a str for maior que num, deve cortar a string quando atingir 
// o tamanho num e adicionar ...
// Se a string for menor ou igual a num, simplesmente retorna a str

function truncateString(str, num) {
  let holder = str.substr(0, num);
  if (str.length > num) {
    holder += "...";
  }
  str = holder;
  return str;
}

truncateString("A-tisket a-tasket A green and yellow basket", 8);
console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8));