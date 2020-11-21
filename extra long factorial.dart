int factorial(int n){
  if(n==1){
    return n;
  }else if (n<0){
    return n;
  }return n * factorial(n-1);
  
}

void main(int n) {
 //change 5 to whatever value you want to find
 print(factorial(5)); 
}

