import random
import copy
result = []
for i in range(3,100):
    r = 0
    best_r = 0
    for c in range(100000):
        best = 0
        chosen = 0
        cond = True
        for j in range(100):
            candidate = random.random()
            if candidate > best:
                best = copy.copy(candidate)
                if j > i and cond:
                    chosen = copy.copy(candidate)
                    cond = False
            if j == 99 and chosen == 0:
                chosen = copy.copy(candidate)
        if best == chosen:
            best_r = (c*best_r + 1)/(c+1)
        else:
            best_r = (c*best_r)/(c+1)
        r = (c*r+chosen)/(c+1)
    result.append(str(i)+","+str(10*r)+","+str(100*best_r)+"%")
    print(result[i-3])
with open("optimal_stop_results.csv","w+") as f:
    f.write("\n".join(result))