function findLongestWordLength(str) {
  let list_str = str.split(" ");
  let major = "";
  for (let i = 0; i < list_str.length; i++) {
    if (major.length < list_str[i].length) {
      major = list_str[i];
    }
  }
  str = major;
  return str.length;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));