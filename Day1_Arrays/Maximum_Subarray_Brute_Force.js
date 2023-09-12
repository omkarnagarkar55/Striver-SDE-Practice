/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let len = nums.length;
    let mSum = nums[0];
        for(let i= 0;i<=len-1;i++){
        let sum = 0;
 
        for(let j=i;j<=len-1;j++){
            sum+=nums[j];
            if(mSum < sum){
                mSum = sum;
            }   
        }
        
    }    

    return mSum;
};
