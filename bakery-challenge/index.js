const salesData = [];
let bankPayments = [];
const days = [];
const input =
  'F 1 4 2357 F 2 4 9353 F 3 4 8627 F 4 4 487 F 5 4 3887 F 6 4 7146 F 7 4 6135 F 8 4 1982 F 9 4 5183 F 10 4 8717 F 11 4 7707 F 12 4 4786 F 13 4 6902 F 14 4 852 F 15 4 5589 F 17 4 2139 F 16 4 4851 F 19 4 1817 F 18 4 2593 F 21 4 1163 F 20 4 7962 F 23 4 4457 F 22 4 6636 F 25 4 4406 F 24 4 3412 F 27 4 6239 F 26 4 2004 F 29 4 7435 F 28 4 1651 F 31 4 2545 F 30 4 1847 F 34 4 8705 F 35 4 8783 F 32 4 6008 F 33 4 5504 F 38 4 6374 F 39 4 8840 F 36 4 7527 F 37 4 1184 B 1 1178 B 2 590 B 2 4676 B 3 4313 B 4 4677 B 4 243 B 5 4314 B 5 122 B 5 1943 B 6 589 B 6 122 B 6 972 B 6 3573 B 7 972 B 7 3067 B 8 3573 B 8 1534 B 8 991 B 9 1534 B 9 2591 B 10 991 B 10 4358 B 11 2592 B 11 3853 B 12 4359 B 12 2393 B 13 1936 B 13 3451 B 14 2393 B 14 1726 B 14 426 B 15 1725 B 15 2794 B 17 1397 B 17 1213 B 17 1069 B 16 426 B 16 1398 B 16 2425 B 19 535 B 19 908 B 18 1213 B 18 535 B 18 1296 B 21 454 B 21 581 B 20 1297 B 20 455 B 20 3981 B 23 582 B 23 2228 B 22 3981 B 22 3318 B 25 1114 B 25 2203 B 24 3318 B 24 1026 B 24 1706 B 27 1101 B 27 3119 B 26 1706 B 26 1102 B 26 1002 B 29 3120 B 29 413 B 29 3717 B 28 1002 B 28 825 B 31 1859 B 31 1272 B 30 413 B 30 1859 B 30 923 B 34 1502 B 34 4352 B 35 2752 B 35 2177 B 35 4391 B 32 924 B 32 3004 B 33 1273 B 33 1502 B 33 2752 B 38 1882 B 38 296 B 38 3187 B 39 296 B 39 1594 B 39 4420 B 36 2176 B 36 2196 B 36 3763 B 37 2196 B 37 159 B 37 592 B 40 1593 B 41 4420';

// parse string
const inputArray = input.split(' ');

// initialise salesdata array with all the daily sales
for (let i = 0; i < inputArray.length; i++) {
  if (inputArray[i] === 'F') {
    salesData.push({
      day: Number(inputArray[i + 1]),
      timeFrame: Number(inputArray[i + 2]),
      sales: Number(inputArray[i + 3]),
    });
    days.push(Number(inputArray[i + 1]));
  }
}

console.log('sales data');
console.log(salesData);

// create bank payments dataset
for (let i = 0; i < inputArray.length; i++) {
  if (inputArray[i] === 'B') {
    bankPayments.push({
      day: Number(inputArray[i + 1]),
      amount: Number(inputArray[i + 2]),
    });
  }
}

console.log('bank payments');
console.log(bankPayments);

function getAllSubsets(array) {
  const subsets = [[]];

  for (const el of array) {
    const last = subsets.length - 1;
    for (let i = 0; i <= last; i++) {
      if (subsets[i].length < 4) {
        subsets.push([...subsets[i], el]);
      }
    }
  }
  return subsets;
}

function getAllPaymentCombinations(day, payments, maxDay) {
  const array = [];
  /* console.log('getallpaymentcombos');
  console.log(`day: ${day}`);
  console.log(`maxday: ${maxDay}`);
  console.log('payments');
  console.log(payments); */
  for (let n = 0; n < payments.length; n++) {
    if (payments[n].day >= day && payments[n].day <= maxDay) {
      array.push(payments[n]);
    }
  }
  /* console.log('array for subsets');
  console.log(array); */
  return getAllSubsets(array);
}

function removeUsedPayments(paymentsToRemove, payments) {
  for (let i = 0; i < payments.length; i++) {
    for (let j = 0; j < paymentsToRemove[0].length; j++) {
      if (paymentsToRemove[j] === payments[i].amount) {
        payments.splice(i, 1);
        // reset iterations since array is mutated
        i = 0;
        j = 0;
        console.log('success');
      }
    }
  }
  return payments;
}

function deleteDay(daysArray, dayToDelete) {
  for (let p = 0; p < daysArray.length; p++) {
    if (daysArray[p] === dayToDelete) {
      daysArray.splice(p, 1);
    }
  }
}

for (let i = 0; i < salesData.length; i++) {
  let updatedBankPayments;
  const maxDay = salesData[i].day + salesData[i].timeFrame;
  /* console.log(
    `day: ${salesData[i].day}, timeframe: ${salesData[i].timeFrame}, maxday: ${maxDay}`,
  ); */
  const combinations = getAllPaymentCombinations(
    salesData[i].day,
    bankPayments,
    maxDay,
  );

  for (let j = 0; j < combinations.length; j++) {
    //sum the bits inside a combination element
    let total = 0;
    const paymentsToDelete = [[]];
    for (let m = 0; m < combinations[j].length; m++) {
      total += combinations[j][m].amount;
      paymentsToDelete[m] = combinations[j][m].amount;
    }
    if (total === salesData[i].sales) {
      deleteDay(days, salesData[i].day);
      updatedBankPayments = removeUsedPayments(paymentsToDelete, bankPayments);

      bankPayments = updatedBankPayments;
    }
  }
}

for (let i = 0; i < days.length; i++) {
  process.stdout.write(`${days[i]} `);
}
