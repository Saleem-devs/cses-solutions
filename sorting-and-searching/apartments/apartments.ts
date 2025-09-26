function apartments(
  nApplicants: number,
  nApartments: number,
  maxAllowedDifference: number,
  desiredSizes: number[],
  availableSizes: number[]
): void {
  if (nApplicants < 1 || nApplicants > 200000) {
    console.log("number of applicants must be between 1 and 200000");
    return;
  }
  if (nApartments < 1 || nApartments > 200000) {
    console.log("number of apartments must be between 1 and 200000");
    return;
  }
  if (maxAllowedDifference < 0 || maxAllowedDifference > 1000000000) {
    console.log("maximum allowed difference must be between 0 and 1e9");
    return;
  }
  if (nApplicants !== desiredSizes.length) {
    console.log("number of applicants must match length of desired sizes");
    return;
  }
  if (nApartments !== availableSizes.length) {
    console.log("number of apartments must match length of available sizes");
    return;
  }

  desiredSizes.sort((a, b) => a - b);
  availableSizes.sort((a, b) => a - b);

  let i = 0;
  let j = 0;
  let success = 0;

  while (i < nApplicants && j < nApartments) {
    if (Math.abs(desiredSizes[i] - availableSizes[j]) <= maxAllowedDifference) {
      success++;
      i++;
      j++;
    } else if (availableSizes[j] < desiredSizes[i] - maxAllowedDifference) {
      j++;
    } else {
      i++;
    }
  }

  console.log(success);
}

apartments(4, 3, 5, [60, 45, 80, 60], [30, 60, 75]);
