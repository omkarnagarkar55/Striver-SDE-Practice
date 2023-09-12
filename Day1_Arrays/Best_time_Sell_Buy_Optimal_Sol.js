/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
   let minBuy = prices[0];
   let profit = 0;
   for(let i of prices){
       if(i < minBuy)
           minBuy = i;

        if(i- minBuy > profit)
            profit = i- minBuy;
   }
   return profit;
};
