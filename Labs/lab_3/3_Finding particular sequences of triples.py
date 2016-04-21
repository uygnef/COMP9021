for i in range(10,100):
    i_digits = {i//10, i%10}
    if len(i_digits) != 2:
        continue   
    for j in range(i+1,100):
        #print(j)
        j_digits = i_digits | {j//10,j%10}      
        if len(j_digits) != 4:
            continue
        #print(j)
        for k in range(j+1,100):
            k_digits = j_digits | {k // 10, k % 10}
            
            if len(k_digits) != 6:
                continue
            product = i * j * k
          #  print(product)
            if k_digits == set(int(d) for d in str(product)):
                print('{} x {} x {} = {}'.format(i, j, k, product))
