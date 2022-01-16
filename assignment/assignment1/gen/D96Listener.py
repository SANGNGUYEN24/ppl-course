# Generated from D:/Study2/HCMUT/semester212/PPL/code/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#literal.
    def enterLiteral(self, ctx:D96Parser.LiteralContext):
        pass

    # Exit a parse tree produced by D96Parser#literal.
    def exitLiteral(self, ctx:D96Parser.LiteralContext):
        pass


    # Enter a parse tree produced by D96Parser#identifer.
    def enterIdentifer(self, ctx:D96Parser.IdentiferContext):
        pass

    # Exit a parse tree produced by D96Parser#identifer.
    def exitIdentifer(self, ctx:D96Parser.IdentiferContext):
        pass


    # Enter a parse tree produced by D96Parser#indexedArray.
    def enterIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
        pass

    # Exit a parse tree produced by D96Parser#indexedArray.
    def exitIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
        pass


    # Enter a parse tree produced by D96Parser#multiDimentionalArray.
    def enterMultiDimentionalArray(self, ctx:D96Parser.MultiDimentionalArrayContext):
        pass

    # Exit a parse tree produced by D96Parser#multiDimentionalArray.
    def exitMultiDimentionalArray(self, ctx:D96Parser.MultiDimentionalArrayContext):
        pass


    # Enter a parse tree produced by D96Parser#allTest.
    def enterAllTest(self, ctx:D96Parser.AllTestContext):
        pass

    # Exit a parse tree produced by D96Parser#allTest.
    def exitAllTest(self, ctx:D96Parser.AllTestContext):
        pass



del D96Parser