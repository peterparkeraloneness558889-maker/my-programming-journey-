def sum_even_fibonacci(limit):
    prev_even = 0
    curr_even = 2
    total_sum = 0 
   
    while curr_even <= limit:

       total_sum =+ curr_even


       next_even =  (4 * curr_even ) + prev_even


       prev_even = curr_even
       curr_even = next_even

    return total_sum
 
limit = 4000000 
tassnime_answer = sum_even_fibonacci(limit)

print("the final_sum is:",tassnime_answer) 
