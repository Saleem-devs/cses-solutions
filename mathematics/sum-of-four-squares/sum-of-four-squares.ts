function sumOfFourSquares(input: Array<number>) {
  const numTestCases = input[0];
  const nValues = input.slice(1);

  if (numTestCases < 1 || numTestCases > 1000) {
    console.log("The number of test cases must be at least 1 and at most 1000");
    return;
  }

  if (numTestCases !== nValues.length) {
    console.log("The num_of_test_cases must equal the available test cases");
    return;
  }

  for (const n of nValues) {
    if (n === 0) {
      console.log(`0 0 0 0`);
      continue;
    }

    const sqrt = findPerfectSquare(n);
    if (sqrt !== false) {
      console.log(`${sqrt} 0 0 0`);
      continue;
    }

    let found = false;
    for (let a = Math.floor(Math.sqrt(n)); a >= 0 && !found; a--) {
      const r = n - a * a;
      const threeSquares = findThreeSquares(r);
      if (threeSquares) {
        console.log(
          `${threeSquares[0]} ${threeSquares[1]} ${threeSquares[2]} ${a}`
        );
        found = true;
      }
    }
  }
}

function findPerfectSquare(num: number): number | false {
  const sqrt = Math.floor(Math.sqrt(num));
  return sqrt * sqrt === num ? sqrt : false;
}

function findThreeSquares(num: number): Array<number> | false {
  // Legendre's three-square theorem
  let m = num;
  while (m % 4 === 0) m /= 4;
  if (m % 8 === 7) return false;

  for (let a = 0; a * a <= num; a++) {
    for (let b = 0; b * b <= num - a * a; b++) {
      const c2 = num - a * a - b * b;
      if (c2 >= 0) {
        const c = Math.floor(Math.sqrt(c2));
        if (c * c === c2) {
          return [a, b, c];
        }
      }
    }
  }
  return false;
}

sumOfFourSquares([5, 5, 30, 74, 17, 322266]);
