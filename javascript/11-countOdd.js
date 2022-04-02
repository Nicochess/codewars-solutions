function oddCount(n){
    let oddNums = 0;
    for(let i = 0; i < n; i++){
      if(i % 2 !== 0){
        oddNums += 1
      }
    }
    
    return oddNums
}