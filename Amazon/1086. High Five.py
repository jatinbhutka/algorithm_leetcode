class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        score = {}
        for item in items:
            if item[0] in score:        
                score.setdefault(item[0],[]).append(item[1])
            else:
                score[item[0]] = [item[1]]
        res = []
        for key, val in score.items():
            if len(val) > 5:
                val.sort()
                print(val)
                avg = sum(val[len(val)-5:len(val)])//5
            else:
                avg = sum(val)//len(val)
            r = [key, avg]
            res.append(r)
        return res
        

        
        
import math
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        map = {}

        items.sort()

        for item in items:
            id = item[0]
            score = item[1]
            if id not in map:
                map[id] = []
            map[id].append(score)

        result = []

        for k,v in map.items():
            temp = v.copy()
            temp.sort()
            temp = temp[::-1]
            average = 0.0
            for i in range(5):
                average += temp[i]
            average = average / 5
            result.append([k,math.floor(average)])

        return result        
