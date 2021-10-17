class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0

        while i < len(command):
            if command[i] == "G":
                ans += "G"
                i += 1

            elif command[i] == "(":
                i += 1
                if command[i] == ")":
                    ans += "o"
                    i += 1
                else:
                    ans += "al"
                    i += 3

        return ans
