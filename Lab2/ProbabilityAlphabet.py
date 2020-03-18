class ProbabilityAlphabet:
    probability = 0
    symbol = ""
    code = ""

    def __str__(self) -> str:
        return "Вероятность = " + str(self.probability) + " Символ = " + self.symbol + " Code = " + self.code

    def __init__(self, probability, symbol):
        self.probability = probability
        self.symbol = symbol

    def compare(self, probabilityAlphabet):
        if probabilityAlphabet.probability > probabilityAlphabet:
            return True
        else:
            return False
