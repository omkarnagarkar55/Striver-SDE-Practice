module.exports = { 
 //param A : array of integers
 //return a array of integers
	repeatedNumber : function(a){
    const n = a.length;
    const hash = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        hash[a[i]]++;
    }

    let repeating = -1, missing = -1;
    for (let i = 1; i <= n; i++) {
        if (hash[i] == 2) repeating = i;
        else if (hash[i] == 0) missing = i;

        if (repeating != -1 && missing != -1) break;
    }

    return [repeating, missing];
}
};
