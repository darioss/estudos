function checkBooleanPrimitive(bool) {
  // Se o valor repassado na função for um valor 
  // Booleano primitivo, deve retornar true, caso 
  // contrário deve retornar false
  if (bool === true || bool === false) {
    bool = true;
  } else {
    bool = false;
  }
  return bool;
}
checkBooleanPrimitive(null);
console.log(checkBooleanPrimitive(false));