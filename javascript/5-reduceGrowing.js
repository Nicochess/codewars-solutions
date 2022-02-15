function grow(x){
    return x.reduce((total, num )=> {
      return total *= num
    })
}