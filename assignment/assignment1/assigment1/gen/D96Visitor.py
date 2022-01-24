# Generated from D:/Study2/HCMUT/semester212/PPL/code/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
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


    # Visit a parse tree produced by D96Parser#expression_list.
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)



del D96Parser