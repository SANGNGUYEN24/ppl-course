# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
<<<<<<< HEAD
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#many_class.
    def visitMany_class(self, ctx:D96Parser.Many_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body_unit.
    def visitClass_body_unit(self, ctx:D96Parser.Class_body_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#super_class_group.
    def visitSuper_class_group(self, ctx:D96Parser.Super_class_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#program_class_declaration.
    def visitProgram_class_declaration(self, ctx:D96Parser.Program_class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#program_class_body.
    def visitProgram_class_body(self, ctx:D96Parser.Program_class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#main_method_declaration.
    def visitMain_method_declaration(self, ctx:D96Parser.Main_method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_list.
    def visitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_list_tail.
    def visitParameter_list_tail(self, ctx:D96Parser.Parameter_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list.
    def visitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dolar_identifier_list.
    def visitDolar_identifier_list(self, ctx:D96Parser.Dolar_identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list_tail.
    def visitIdentifier_list_tail(self, ctx:D96Parser.Identifier_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dolar_identifier_list_tail.
    def visitDolar_identifier_list_tail(self, ctx:D96Parser.Dolar_identifier_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list.
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list_tail.
    def visitExpression_list_tail(self, ctx:D96Parser.Expression_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_expression.
    def visitElement_expression(self, ctx:D96Parser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_operator.
    def visitRelational_operator(self, ctx:D96Parser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_expr.
    def visitRelational_expr(self, ctx:D96Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#and_or_expr.
    def visitAnd_or_expr(self, ctx:D96Parser.And_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#add_sub_expr.
    def visitAdd_sub_expr(self, ctx:D96Parser.Add_sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_add_mol_expr.
    def visitMul_add_mol_expr(self, ctx:D96Parser.Mul_add_mol_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#not_expr.
    def visitNot_expr(self, ctx:D96Parser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#sign_expr.
    def visitSign_expr(self, ctx:D96Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator_expr.
    def visitIndex_operator_expr(self, ctx:D96Parser.Index_operator_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_attribute_access.
    def visitInstance_attribute_access(self, ctx:D96Parser.Instance_attribute_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instace_method_invocation.
    def visitInstace_method_invocation(self, ctx:D96Parser.Instace_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_invocation.
    def visitStatic_method_invocation(self, ctx:D96Parser.Static_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_attribute_access.
    def visitStatic_attribute_access(self, ctx:D96Parser.Static_attribute_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_creation.
    def visitObject_creation(self, ctx:D96Parser.Object_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#atom_expr.
    def visitAtom_expr(self, ctx:D96Parser.Atom_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#function_call.
    def visitFunction_call(self, ctx:D96Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_val_statement.
    def visitVar_val_statement(self, ctx:D96Parser.Var_val_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement.
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_part.
    def visitIf_part(self, ctx:D96Parser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if_part.
    def visitElse_if_part(self, ctx:D96Parser.Else_if_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_part.
    def visitElse_part(self, ctx:D96Parser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_statement.
    def visitFor_in_statement(self, ctx:D96Parser.For_in_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#loop_part.
    def visitLoop_part(self, ctx:D96Parser.Loop_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation_statement.
    def visitMethod_invocation_statement(self, ctx:D96Parser.Method_invocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statement.
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimentional_array.
    def visitMulti_dimentional_array(self, ctx:D96Parser.Multi_dimentional_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier.
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
=======
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classDeclaration.
    def visitClassDeclaration(self, ctx:D96Parser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normalClassDecl.
    def visitNormalClassDecl(self, ctx:D96Parser.NormalClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#programClassDecl.
    def visitProgramClassDecl(self, ctx:D96Parser.ProgramClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#programClassMemDecl.
    def visitProgramClassMemDecl(self, ctx:D96Parser.ProgramClassMemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mainMethodDecl.
    def visitMainMethodDecl(self, ctx:D96Parser.MainMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:D96Parser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:D96Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameterList.
    def visitParameterList(self, ctx:D96Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#d96Type.
    def visitD96Type(self, ctx:D96Parser.D96TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:D96Parser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifierList.
    def visitIdentifierList(self, ctx:D96Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mixedIdentifier.
    def visitMixedIdentifier(self, ctx:D96Parser.MixedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expressionList.
    def visitExpressionList(self, ctx:D96Parser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elementExpression.
    def visitElementExpression(self, ctx:D96Parser.ElementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexOperator.
    def visitIndexOperator(self, ctx:D96Parser.IndexOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relationalOperator.
    def visitRelationalOperator(self, ctx:D96Parser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relationalExpr.
    def visitRelationalExpr(self, ctx:D96Parser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#andOrExpr.
    def visitAndOrExpr(self, ctx:D96Parser.AndOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#addSubExpr.
    def visitAddSubExpr(self, ctx:D96Parser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mulAddMolExpr.
    def visitMulAddMolExpr(self, ctx:D96Parser.MulAddMolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#notExpr.
    def visitNotExpr(self, ctx:D96Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#signExpr.
    def visitSignExpr(self, ctx:D96Parser.SignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexOperatorExpr.
    def visitIndexOperatorExpr(self, ctx:D96Parser.IndexOperatorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceAccess.
    def visitInstanceAccess(self, ctx:D96Parser.InstanceAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staticAccess.
    def visitStaticAccess(self, ctx:D96Parser.StaticAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#objectCreation.
    def visitObjectCreation(self, ctx:D96Parser.ObjectCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#atomExpr.
    def visitAtomExpr(self, ctx:D96Parser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varValStatement.
    def visitVarValStatement(self, ctx:D96Parser.VarValStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignStatement.
    def visitAssignStatement(self, ctx:D96Parser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifStatement.
    def visitIfStatement(self, ctx:D96Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forInStatement.
    def visitForInStatement(self, ctx:D96Parser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakStatement.
    def visitBreakStatement(self, ctx:D96Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continueStatement.
    def visitContinueStatement(self, ctx:D96Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnStatement.
    def visitReturnStatement(self, ctx:D96Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodInvocationStatement.
    def visitMethodInvocationStatement(self, ctx:D96Parser.MethodInvocationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockStatement.
    def visitBlockStatement(self, ctx:D96Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexedArray.
    def visitIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
>>>>>>> develop
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)



del D96Parser