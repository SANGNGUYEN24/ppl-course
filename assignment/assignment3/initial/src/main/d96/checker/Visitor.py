from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):

    def visit(self, ast, param):
        return ast.accept(self, param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass

    @abstractmethod
    def visitClassDecl(self, ast, param):
        pass

    @abstractmethod
    def visitFuncDecl(self, ast, param):
        pass

    @abstractmethod
    def visitVarDecl(self, ast, param):
        pass

    @abstractmethod
    def visitIntType(self, ast, param):
        pass

    @abstractmethod
    def visitFloatType(self, ast, param):
        pass

    @abstractmethod
    def visitBoolType(self, ast, param):
        pass

    @abstractmethod
    def visitStringType(self, ast, param):
        pass

    @abstractmethod
    def visitArrayType(self, ast, param):
        pass

    @abstractmethod
    def visitArrayCell(self, ast, param):
        pass

    @abstractmethod
    def visitVoidType(self, ast, param):
        pass

    @abstractmethod
    def visitBinaryOp(self, ast, param):
        pass

    @abstractmethod
    def visitUnaryOp(self, ast, param):
        pass

    @abstractmethod
    def visitAssign(self, ast, param):
        pass

    @abstractmethod
    def visitCallExpr(self, ast, param):
        pass

    @abstractmethod
    def visitId(self, ast, param):
        pass

    @abstractmethod
    def visitIf(self, ast, param):
        pass

    @abstractmethod
    def visitFor(self, ast, param):
        pass

    @abstractmethod
    def visitContinue(self, ast, param):
        pass

    @abstractmethod
    def visitBreak(self, ast, param):
        pass

    @abstractmethod
    def visitReturn(self, ast, param):
        pass

    @abstractmethod
    def visitMethodInvocation(self, ast, param):
        pass

    @abstractmethod
    def visitBlock(self, ast, param):
        pass

    @abstractmethod
    def visitIntLiteral(self, ast, param):
        pass

    @abstractmethod
    def visitFloatLiteral(self, ast, param):
        pass

    @abstractmethod
    def visitBooleanLiteral(self, ast, param):
        pass

    @abstractmethod
    def visitStringLiteral(self, ast, param):
        pass


class BaseVisitor(Visitor):

    def visitClassDecl(self, ast, param):
        pass

    def visitVarDecl(self, ast, param):
        pass

    def visitFloatType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitMethodInvocation(self, ast, param):
        pass

    def visitFloatLiteral(self, ast, param):
        pass

    def visitBooleanLiteral(self, ast, param):
        pass

    def visitStringLiteral(self, ast, param):
        pass

    def visitProgram(self, ast, param):
        return None

    def visitFuncDecl(self, ast, param):
        return None

    def visitIntType(self, ast, param):
        return None

    def visitVoidType(self, ast, param):
        return None

    def visitCallExpr(self, ast, param):
        return None

    def visitId(self, ast, param):
        return None

    def visitBlock(self, ast, param):
        return None

    def visitIntLiteral(self, ast, param):
        return None
