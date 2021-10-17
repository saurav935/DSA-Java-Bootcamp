class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(indices)

        for i in range(0, len(indices)):
            ans[indices[i]] = s[i]

        return "".join(ans)

