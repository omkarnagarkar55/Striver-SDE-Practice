/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let ind = -1
    let size = nums.length;
    for(let i = size-2;i>=0;i--){
        if(nums[i]<nums[i+1]){
            ind = i;
            break
        }
    }
    if(ind == -1)
        nums.reverse()
    else{
        let j;
        for(j = size-1;j>ind;j--){
            if(nums[ind]<nums[j]){
                let temp = nums[ind];
                nums[ind] = nums[j];
                nums[j] = temp;
                break;
            }
        }
        nums.splice(ind+1,size - (ind+1),...nums.slice(ind+1,size).reverse().slice())
        
    }


};
