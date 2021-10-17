class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        if ruleKey == "type":
            return self.helper(0, items, ruleValue)

        elif ruleKey == "color":
            return self.helper(1, items, ruleValue)

        elif ruleKey == "name":
            return self.helper(2, items, ruleValue)

    def helper(self, idx, arr, value):
        count = 0
        for i in arr:
            if i[idx] == value:
                count += 1

        return count

