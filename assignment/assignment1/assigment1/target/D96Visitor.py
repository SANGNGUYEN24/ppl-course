# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifer.
    def visitIdentifer(self, ctx:D96Parser.IdentiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexedArray.
    def visitIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiDimentionalArray.
    def visitMultiDimentionalArray(self, ctx:D96Parser.MultiDimentionalArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#test.
    def visitTest(self, ctx:D96Parser.TestContext):
        return self.visitChildren(ctx)



del D96Parser