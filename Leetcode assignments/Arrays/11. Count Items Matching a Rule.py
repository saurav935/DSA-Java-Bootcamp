
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for i in items if i[d[ruleKey]] == ruleValue)



#################################  OR  ######################################



class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            key_idx = 0
        elif ruleKey == "color":
            key_idx = 1
        elif ruleKey == "name":
            key_idx = 2
        return self.match(items ,key_idx ,ruleValue)


    def match(self ,items ,key_idx, value):
        count = 0
        for i in items:
            if i[key_idx] == value:
                count += 1
        return count


#################################  OR  ######################################


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        i = 0
        if ruleKey == "type":
            i = 0
        if ruleKey == "color":
            i = 1
        if ruleKey == "name":
            i = 2

        for j in items:
            while j[i] == ruleValue:
                count += 1
                break
        return count


#################################  OR  ######################################

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        i = 0

        if ruleKey == "type":
            for j in items:
                if j[0] == ruleValue:
                    count += 1

        if ruleKey == "color":
            for j in items:
                if j[1] == ruleValue:
                    count += 1

        if ruleKey == "name":
            for j in items:
                if j[2] == ruleValue:
                    count += 1

        return count