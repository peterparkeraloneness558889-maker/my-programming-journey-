def sum_multiples_of(target,limit):
    last_term = (limit - 1) // target
    n = last_term
    first_term = target 
    final_term = last_term * target
    return (n * (first_term + final_term)) // 2

limitlimit = 1000


tassnime_3 = sum_multiples_of(3,limit)
tassnime_5 = sum_multiples_of(5,limit)
tassnime_15 = sum_multiples_of(15,limit)


final_term = tassnime_3 + tassnime_5 - tassnime_15

print("mathematical result:",final_answer)
