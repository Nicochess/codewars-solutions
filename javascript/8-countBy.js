function countBy(x, n) {
  let z = [];
  let counter = 0;
  for (let i = 0; i != n; i++) {
    counter += x;
    z.push(counter);
  }
  return z;
}