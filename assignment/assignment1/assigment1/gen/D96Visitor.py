# Generated from D:/Study2/HCMUT/semester212/PPL/code/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimentional_array.
    def visitMulti_dimentional_array(self, ctx:D96Parser.Multi_dimentional_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operator_boolean.
    def visitOperator_boolean(self, ctx:D96Parser.Operator_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operator_integer.
    def visitOperator_integer(self, ctx:D96Parser.Operator_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operator_float.
    def visitOperator_float(self, ctx:D96Parser.Operator_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operator_string.
    def visitOperator_string(self, ctx:D96Parser.Operator_stringContext):
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


    # Visit a parse tree produced by D96Parser#parameter_list_tail.
    def visitParameter_list_tail(self, ctx:D96Parser.Parameter_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_body.
    def visitMethod_body(self, ctx:D96Parser.Method_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list.
    def visitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list_tail.
    def visitIdentifier_list_tail(self, ctx:D96Parser.Identifier_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list.
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list_tail.
    def visitExpression_list_tail(self, ctx:D96Parser.Expression_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return.
    def visitReturn(self, ctx:D96Parser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operation.
    def visitOperation(self, ctx:D96Parser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#unary_operation.
    def visitUnary_operation(self, ctx:D96Parser.Unary_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#binary_operation.
    def visitBinary_operation(self, ctx:D96Parser.Binary_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_operation.
    def visitInt_operation(self, ctx:D96Parser.Int_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_operation.
    def visitFloat_operation(self, ctx:D96Parser.Float_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_operand.
    def visitInt_operand(self, ctx:D96Parser.Int_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_operand.
    def visitFloat_operand(self, ctx:D96Parser.Float_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_float_operand.
    def visitInt_float_operand(self, ctx:D96Parser.Int_float_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#function_call.
    def visitFunction_call(self, ctx:D96Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_operation.
    def visitBoolean_operation(self, ctx:D96Parser.Boolean_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_operand.
    def visitBoolean_operand(self, ctx:D96Parser.Boolean_operandContext):
        return self.visitChildren(ctx)



del D96Parser