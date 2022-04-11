# Trieu Minh Sang - 1852717
from initial.target.BKITVisitor import BKITVisitor
from initial.target.BKITParser import BKITParser
from functools import reduce

from initial.src.main.bkit.utils.BKitAST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Program(ctx.globdeclpart().accept(self) + ctx.funcdeclspart().accept(self))

    def visitGlobdeclpart(self, ctx: BKITParser.GlobdeclpartContext):
        if ctx.getChildCount() == 2:
            return ctx.vardecls().accept(self) + ctx.globdeclpart().accept(self)
        else:
            return []

    def visitFuncdeclspart(self, ctx: BKITParser.FuncdeclspartContext):
        if ctx.getChildCount() == 2:
            return [ctx.funcdecls().accept(self)] + ctx.funcdeclspart().accept(self)
        else:
            return []

    def visitVardecls(self, ctx: BKITParser.VardeclsContext):
        return ctx.varlist().accept(self)

    def visitVarlist(self, ctx: BKITParser.VarlistContext):
        if ctx.getChildCount() == 2:
            return ctx.variableinit().accept(self) + ctx.tailvar().accept(self)
        else:
            return ctx.variableinit().accept(self)

    def visitTailvar(self, ctx: BKITParser.TailvarContext):
        if ctx.getChildCount() == 3:
            return ctx.variableinit().accept(self) + ctx.tailvar().accept(self)
        else:
            return []

    def visitVariableinit(self, ctx: BKITParser.VariableinitContext):
        if ctx.getChildCount() == 4:
            return [VarDecl(Id(ctx.ID().getText()), ctx.dimlist().accept(self), ctx.literals().accept(self))]
        elif ctx.getChildCount() == 2:
            return [VarDecl(Id(ctx.ID().getText()), ctx.dimlist().accept(self), None)]
        elif ctx.getChildCount() == 3:
            return [VarDecl(Id(ctx.ID().getText()), [], ctx.literals().accept(self))]
        else:
            return [VarDecl(Id(ctx.ID().getText()), [], None)]

    def visitLiterals(self, ctx: BKITParser.LiteralsContext):
        if ctx.INTLIT():
            if ctx.INTLIT().getText().isnumeric():
                return IntLiteral(int(ctx.INTLIT().getText()))
            else:
                return IntLiteral(int(ctx.INTLIT().getText(), 0))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return ctx.arraydecls().accept(self)

    def visitArraydecls(self, ctx: BKITParser.ArraydeclsContext):
        return ctx.arraylit().accept(self)

    def visitArraylit(self, ctx: BKITParser.ArraylitContext):
        if ctx.getChildCount() == 0:
            return ArrayLiteral([])
        else:
            return ArrayLiteral([ctx.literals().accept(self)] + ctx.arraylit_().accept(self))

    def visitArraylit_(self, ctx: BKITParser.Arraylit_Context):
        if ctx.getChildCount() == 3:
            return [ctx.literals().accept(self)] + ctx.arraylit_().accept(self)
        else:
            return []

    def visitDimlist(self, ctx: BKITParser.DimlistContext):
        if ctx.getChildCount() == 2:
            return [ctx.dim().accept(self)] + ctx.taildim().accept(self)
        else:
            return [ctx.dim().accept(self)]

    def visitTaildim(self, ctx: BKITParser.TaildimContext):
        if ctx.getChildCount() == 2:
            return [ctx.dim().accept(self)] + ctx.taildim().accept(self)
        else:
            return []

    def visitDim(self, ctx: BKITParser.DimContext):
        if ctx.INTLIT().getText().isnumeric():
            return int(ctx.INTLIT().getText())
        else:
            return int(ctx.INTLIT().getText(), 0)

    def visitFuncdecls(self, ctx: BKITParser.FuncdeclsContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        if ctx.parameterlist():
            return FuncDecl(Id(ctx.ID().getText()), ctx.parameterlist().accept(self), (
            reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
            filter(lambda x: not (isinstance(x, list)), statements)))
        else:
            return FuncDecl(Id(ctx.ID().getText()), [], (
            reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
            filter(lambda x: not (isinstance(x, list)), statements)))

    def visitParameterlist(self, ctx: BKITParser.ParameterlistContext):
        if ctx.getChildCount() == 2:
            return [ctx.parameter().accept(self)] + ctx.parameterlist_().accept(self)
        else:
            return [ctx.parameter().accept(self)]

    def visitParameterlist_(self, ctx: BKITParser.Parameterlist_Context):
        if ctx.getChildCount() == 3:
            return [ctx.parameter().accept(self)] + ctx.parameterlist_().accept(self)
        else:
            return []

    def visitParameter(self, ctx: BKITParser.ParameterContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), ctx.dimlist().accept(self), None)
        else:
            return VarDecl(Id(ctx.ID().getText()), [], None)

    def visitRelop(self, ctx: BKITParser.RelopContext):
        return ctx.getChild(0).getText()

    def visitExpr(self, ctx: BKITParser.ExprContext):
        if ctx.getChildCount() == 1:
            return ctx.expr1(0).accept(self)
        else:
            return BinaryOp(ctx.relop().accept(self), ctx.expr1(0).accept(self), ctx.expr1(1).accept(self))

    def visitExpr1(self, ctx: BKITParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return ctx.expr2().accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr1().accept(self), ctx.expr2().accept(self))

    def visitExpr2(self, ctx: BKITParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return ctx.expr3().accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr2().accept(self), ctx.expr3().accept(self))

    def visitExpr3(self, ctx: BKITParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return ctx.expr4().accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr3().accept(self), ctx.expr4().accept(self))

    def visitExpr4(self, ctx: BKITParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return ctx.expr5().accept(self)
        else:
            return UnaryOp(ctx.NOT().getText(), ctx.expr4().accept(self))

    def visitExpr5(self, ctx: BKITParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return ctx.expr6().accept(self)
        else:
            return UnaryOp(ctx.getChild(0).getText(), ctx.expr5().accept(self))

    def visitExpr6(self, ctx: BKITParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return ctx.expr7().accept(self)
        else:
            return ArrayCell(ctx.expr6().accept(self), list(map(lambda x: x.accept(self), ctx.expr())))

    def visitExpr7(self, ctx: BKITParser.Expr7Context):
        if ctx.literals():
            return ctx.literals().accept(self)
        elif ctx.functioncall():
            return ctx.functioncall().accept(self)
        elif ctx.getChildCount() == 3:
            return ctx.expr().accept(self)
        else:
            return Id(ctx.ID().getText())

    def visitFunctioncall(self, ctx: BKITParser.FunctioncallContext):
        return CallExpr(Id(ctx.ID().getText()), ctx.argumentslist().accept(self))

    def visitArgumentslist(self, ctx: BKITParser.ArgumentslistContext):
        if ctx.getChildCount() == 2:
            return [ctx.expr().accept(self)] + ctx.argumentslist_().accept(self)
        else:
            return []

    def visitArgumentslist_(self, ctx: BKITParser.Argumentslist_Context):
        if ctx.getChildCount() == 3:
            return [ctx.expr().accept(self)] + ctx.argumentslist_().accept(self)
        else:
            return []

    def visitStatement(self, ctx: BKITParser.StatementContext):
        return ctx.getChild(0).accept(self)

    def visitAssignmentstmt(self, ctx: BKITParser.AssignmentstmtContext):
        return Assign(ctx.expr(0).accept(self), ctx.expr(1).accept(self))

    def visitIfstmt(self, ctx: BKITParser.IfstmtContext):
        i = ctx.if_statement().accept(self)
        if ctx.ELSE():
            if ctx.ELSEIF():
                j = list(map(lambda a: a.accept(self), ctx.elif_statement()))
                e = list(map(lambda a: a.accept(self), ctx.expr()))
                v = list(map(lambda a: a[0], j))
                s = list(map(lambda a: a[1], j))
                return If([(e[0], i[0], i[1])] + list(zip(e[1:], v, s)), ctx.else_statement().accept(self))
            else:
                return If([(ctx.expr(0).accept(self), i[0], i[1])], ctx.else_statement().accept(self))
        else:
            if ctx.ELSEIF():
                j = list(map(lambda a: a.accept(self), ctx.elif_statement()))
                e = list(map(lambda a: a.accept(self), ctx.expr()))
                v = list(map(lambda a: a[0], j))
                s = list(map(lambda a: a[1], j))
                return If([(e[0], i[0], i[1])] + list(zip(e[1:], v, s)), ([], []))
            else:
                return If([(ctx.expr(0).accept(self), i[0], i[1])], ([], []))

    def visitIf_statement(self, ctx: BKITParser.If_statementContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        return [reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
                filter(lambda x: not (isinstance(x, list)), statements)]

    def visitElif_statement(self, ctx: BKITParser.Elif_statementContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        return [reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
                filter(lambda x: not (isinstance(x, list)), statements)]

    def visitElse_statement(self, ctx: BKITParser.Else_statementContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        return (reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
                filter(lambda x: not (isinstance(x, list)), statements))

    def visitForstmt(self, ctx: BKITParser.ForstmtContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        return For(Id(ctx.ID().getText()), ctx.expr(0).accept(self), ctx.expr(1).accept(self), ctx.expr(2).accept(self),
                   (reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
                    filter(lambda x: not (isinstance(x, list)), statements)))

    def visitWhilestmt(self, ctx: BKITParser.WhilestmtContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        return While(ctx.expr().accept(self), (
        reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
        filter(lambda x: not (isinstance(x, list)), statements)))

    def visitDowhilestmt(self, ctx: BKITParser.DowhilestmtContext):
        statements = list(map(lambda x: x.accept(self), ctx.statement()))
        return Dowhile((reduce(lambda a, b: a + b, filter(lambda x: isinstance(x, list), statements), []),
                        filter(lambda x: not (isinstance(x, list)), statements)), ctx.expr().accept(self))

    def visitBreakstmt(self, ctx: BKITParser.BreakstmtContext):
        return Break()

    def visitContinuestmt(self, ctx: BKITParser.ContinuestmtContext):
        return Continue()

    def visitCallstmt(self, ctx: BKITParser.CallstmtContext):
        return CallStmt(Id(ctx.ID().getText()), ctx.argumentslist().accept(self))

    def visitReturnstmt(self, ctx: BKITParser.ReturnstmtContext):
        if ctx.expr():
            return Return(ctx.expr().accept(self))
        else:
            return Return(None)
