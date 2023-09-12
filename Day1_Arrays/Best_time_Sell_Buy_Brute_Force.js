/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let size = prices.length;
    let maxProf = 0;
    for(let i=0;i<size-1;i++){
        for(let j=i+1;j<size;j++){
            let prof = 0;
            if(prices[i] < prices[j]){
                prof = prices[j] - prices[i];
                if(prof > maxProf)
                    maxProf = prof;
            }
        }
    }
    return maxProf;
};
