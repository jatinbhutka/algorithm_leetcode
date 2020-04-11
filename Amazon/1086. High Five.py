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
        
        
        
