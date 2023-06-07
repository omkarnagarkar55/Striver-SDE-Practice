/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => {
        if(a[0]!==b[0])
            return a[0] - b[0];
        else
            return a[1] - b[1];
    });

    let size = intervals.length;
    let ans = [];
    for(let i=0;i < size; i++){
        if(ans.length ===0 || ans[ans.length - 1][1] < intervals[i][0])
            ans.push(intervals[i]);
        else
            ans[ans.length - 1][1] = Math.max(ans[ans.length - 1][1],intervals[i][1]);
        
    }
    return ans;
};
