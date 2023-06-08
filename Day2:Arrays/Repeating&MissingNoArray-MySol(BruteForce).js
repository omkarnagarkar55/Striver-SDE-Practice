module.exports = { 
 //param A : array of integers
 //return a array of integers
	repeatedNumber : function(A){
        A.sort((a,b)=> a-b);
        let size = A.length;
        let A1,B1;
        let a =[];
        for(let i = 0;i<A.length-1;i++){
                if(A[i]==A[i+1]){
                    A1=A[i];
                    A.splice(i+1,1)
                    break
                }
            }
        for(let j = 1;j<size;j++){
            if(!A.includes(j)){
                B1=j;
                break
            }
        }
        
        a.push(...[A1,B1]);
        return a;
	}
};
