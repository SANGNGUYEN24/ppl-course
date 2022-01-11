# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#globdeclpart.
    def visitGlobdeclpart(self, ctx:BKITParser.GlobdeclpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdeclspart.
    def visitFuncdeclspart(self, ctx:BKITParser.FuncdeclspartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecls.
    def visitVardecls(self, ctx:BKITParser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varlist.
    def visitVarlist(self, ctx:BKITParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#tailvar.
    def visitTailvar(self, ctx:BKITParser.TailvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variableinit.
    def visitVariableinit(self, ctx:BKITParser.VariableinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraydecls.
    def visitArraydecls(self, ctx:BKITParser.ArraydeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraylit.
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraylit_.
    def visitArraylit_(self, ctx:BKITParser.Arraylit_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimlist.
    def visitDimlist(self, ctx:BKITParser.DimlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#taildim.
    def visitTaildim(self, ctx:BKITParser.TaildimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dim.
    def visitDim(self, ctx:BKITParser.DimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdecls.
    def visitFuncdecls(self, ctx:BKITParser.FuncdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameterlist.
    def visitParameterlist(self, ctx:BKITParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameterlist_.
    def visitParameterlist_(self, ctx:BKITParser.Parameterlist_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relop.
    def visitRelop(self, ctx:BKITParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#functioncall.
    def visitFunctioncall(self, ctx:BKITParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argumentslist.
    def visitArgumentslist(self, ctx:BKITParser.ArgumentslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argumentslist_.
    def visitArgumentslist_(self, ctx:BKITParser.Argumentslist_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignmentstmt.
    def visitAssignmentstmt(self, ctx:BKITParser.AssignmentstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifstmt.
    def visitIfstmt(self, ctx:BKITParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elif_statement.
    def visitElif_statement(self, ctx:BKITParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_statement.
    def visitElse_statement(self, ctx:BKITParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forstmt.
    def visitForstmt(self, ctx:BKITParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whilestmt.
    def visitWhilestmt(self, ctx:BKITParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhilestmt.
    def visitDowhilestmt(self, ctx:BKITParser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakstmt.
    def visitBreakstmt(self, ctx:BKITParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continuestmt.
    def visitContinuestmt(self, ctx:BKITParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callstmt.
    def visitCallstmt(self, ctx:BKITParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnstmt.
    def visitReturnstmt(self, ctx:BKITParser.ReturnstmtContext):
        return self.visitChildren(ctx)



del BKITParser