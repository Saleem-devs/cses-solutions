function findDistinctValues(numOfValues: number, values: number[]) {
  if (numOfValues < 1 || numOfValues > 200000) {
    console.log("number of values must be at least 1 and not more than 200000");
    return;
  }

  if (numOfValues !== values.length) {
    console.log("number of values and length of values do not match");
    return;
  }

  const distinct = new Set<number>();

  values.forEach((value, index) => {
    if (value < 1 || value > 1000000000) {
      console.log(
        `x${index + 1} must be at least 1 and not more than 1000000000`
      );
      return;
    }
    distinct.add(value);
  });

  console.log(distinct.size);
}

findDistinctValues(5, [2, 3, 2, 2, 3]);
