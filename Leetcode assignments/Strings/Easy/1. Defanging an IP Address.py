class Solution:
    def defangIPaddr(self, address: str) -> str:
        add = list(address)

        for i in range(0, len(address)):
            if add[i] == ".":
                add[i] = "[.]"

        return "".join(add)

