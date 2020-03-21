from Lab2.ProbabilityAlphabet import ProbabilityAlphabet


class ProbabilityAlphabetKhartli(ProbabilityAlphabet):
    LeftSide = None
    RightSide = None
    TemporaryNode = False

    def __init__(self, probability, symbol, leftSide, rightSide):
        super().__init__(probability, symbol)
        self.LeftSide = leftSide
        self.RightSide = rightSide

    def __init__(self, downElement, upperElement, temporaryNode):
        super().__init__(downElement.probability + upperElement.probability, "")
        self.LeftSide = downElement
        self.RightSide = upperElement
        self.TemporaryNode = temporaryNode
