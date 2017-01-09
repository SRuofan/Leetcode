# Leetcode
This is a dairy for leetcode problems

Palindrome:
  1) find how many digits the input contains
  2) if the number is odd, then middle location is i/2+1
     if the number is even, then middle location is i/2
  3) Use pointer j, starting at zero 
     For the highest digits on the left: int(x/(10**i))%10 then i+=1
     For the lower digits on the right: int(x/(10**j))%10 then j-= 1
     if there is a difference between the two digits mentioned above, return false. else return true
