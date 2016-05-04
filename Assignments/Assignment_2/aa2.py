    i = -2
    j = -2
    while i < len(A_colour)-2:
        while j < len(B_colour)-2:
            ab = Vector(A_colour[i], A_colour[i+1])
            cd = Vector(B_colour[j], B_colour[j+1])
       #     print(cross_product(ab, cd))
            if cross_product(ab, cd) == 0:
                min_ab = min(A_colour[i].x, A_colour[i+1].x)
                max_ab = max(A_colour[i].x, A_colour[i+1].x)
# 存疑，有可能出现错误排序#
                if min_ab < B_colour[j].x < max_ab and min_ab < B_colour[j+1].x < max_ab:
                    if abs(A_colour[i].x - B_colour[j].x) < abs(A_colour[i].x - B_colour[j+1].x):
                        A_colour = A_colour[0:i] + B_colour[j] + B_colour[j+1] + A_colour[i:]
                        
                    else:
                        A_colour = A_colour[0:i] + [B_colour[j]] + [B_colour[j+1]] + A_colour[i:]
                        
                elif min_ab < B_colour[j].x < max_ab:                        
                    A_colour = A_colour[0:i] + [B_colour[j]]  + A_colour[i:]
                    

                elif min_ab < B_colour[j+1].x < max_ab:
                    A_colour = A_colour[0:i] + [B_colour[j+1]] + A_colour[i:]
                    
                j = j+1
        i = i+1

##                print(A_colour[i].x,B_colour[j].x,A_colour[i+1].x)
##                print(A_colour[i+1].x,B_colour[j].x,A_colour[i+1].x)
##                if min(A_colour[i].x, A_colour[i+1].x) < B_colour[j].x < \
##                   max(A_colour[i].x, A_colour[i+1].x):
##                    A_colour = A[0:i] + B[j] + A[i:]
##                if min(A_colour[i+2].x, A_colour[i+1].x) < B_colour[j].x < \
##                   min(A_colour[i+1].x, A_colour[i+2].x):
##                    A_colour = A[0:i+1] + B[j+1] + A[i+1:]
        return A_colour
