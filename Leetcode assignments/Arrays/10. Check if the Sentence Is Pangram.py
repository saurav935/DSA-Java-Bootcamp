

def checkIfPangram(self, sentence: str) -> bool:
    return set(string.ascii_lowercase) == set(sentence)


#  OR


def checkIfPangram(self, sentence: str) -> bool:
    return len(set(sentence)) == 26