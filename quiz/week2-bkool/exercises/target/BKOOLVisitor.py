# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#many_declaration.
    def visitMany_declaration(self, ctx:BKOOLParser.Many_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declaration_list.
    def visitDeclaration_list(self, ctx:BKOOLParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#one_declaration.
    def visitOne_declaration(self, ctx:BKOOLParser.One_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variable_declaration.
    def visitVariable_declaration(self, ctx:BKOOLParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#identifer_list.
    def visitIdentifer_list(self, ctx:BKOOLParser.Identifer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#identifer_list_tail.
    def visitIdentifer_list_tail(self, ctx:BKOOLParser.Identifer_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#function_declaration.
    def visitFunction_declaration(self, ctx:BKOOLParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter_list.
    def visitParameter_list(self, ctx:BKOOLParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter_list_tail.
    def visitParameter_list_tail(self, ctx:BKOOLParser.Parameter_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#one_parameter.
    def visitOne_parameter(self, ctx:BKOOLParser.One_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typeVar.
    def visitTypeVar(self, ctx:BKOOLParser.TypeVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKOOLParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call.
    def visitCall(self, ctx:BKOOLParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_list.
    def visitExpression_list(self, ctx:BKOOLParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_list_tail.
    def visitExpression_list_tail(self, ctx:BKOOLParser.Expression_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression.
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operand.
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#sub_expression.
    def visitSub_expression(self, ctx:BKOOLParser.Sub_expressionContext):
        return self.visitChildren(ctx)



del BKOOLParser