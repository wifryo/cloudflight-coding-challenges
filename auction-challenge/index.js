const args = process.argv.slice(2);

const input = args[0];
const inputArray = input.split(',');
let maxBid = 0;
let currentBid = 0;
let maxBidBidder = '-';
let currentPrice = Number(inputArray[0]);
const buyNowPrice = Number(inputArray[1]);
const output = [];

output.push('-', currentPrice);

for (let i = 2; i < inputArray.length; i++) {
  if (i % 2 === 0) {
    const currentBidder = inputArray[i];
    currentBid = Number(inputArray[i + 1]);
    if (maxBidBidder === '-') {
      maxBidBidder = currentBidder;
      maxBid = currentBid;
      output.push(maxBidBidder, currentPrice);
    }

    if (currentBid > maxBid && maxBidBidder !== currentBidder) {
      currentPrice = maxBid + 1;
      maxBidBidder = currentBidder;
      maxBid = currentBid;
      output.push(maxBidBidder, currentPrice);
    }
    if (currentBid < maxBid && maxBidBidder !== currentBidder) {
      currentPrice = currentBid + 1;
      if (currentPrice > buyNowPrice) {
        currentPrice = buyNowPrice;
        output.push(maxBidBidder, currentPrice);
        break;
      }
      output.push(maxBidBidder, currentPrice);
    }
    if (currentBid > maxBid && maxBidBidder === currentBidder) {
      maxBid = currentBid;
    }
    if (currentBid === maxBid && maxBidBidder !== currentBidder) {
      currentPrice = currentBid;
      output.push(maxBidBidder, currentPrice);
    }

    if (currentPrice >= buyNowPrice && buyNowPrice !== 0) {
      output.push(maxBidBidder, buyNowPrice);
      break;
    }
  }
}

output.forEach(function (output) {
  process.stdout.write(`${output},`);
});
