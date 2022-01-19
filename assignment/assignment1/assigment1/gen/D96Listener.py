# Generated from D:/Study2/HCMUT/semester212/PPL/code/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#indexed_array.
    def enterIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        pass

    # Exit a parse tree produced by D96Parser#indexed_array.
    def exitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        pass


    # Enter a parse tree produced by D96Parser#multi_dimentional_array.
    def enterMulti_dimentional_array(self, ctx:D96Parser.Multi_dimentional_arrayContext):
        pass

    # Exit a parse tree produced by D96Parser#multi_dimentional_array.
    def exitMulti_dimentional_array(self, ctx:D96Parser.Multi_dimentional_arrayContext):
        pass


    # Enter a parse tree produced by D96Parser#operator_boolean.
    def enterOperator_boolean(self, ctx:D96Parser.Operator_booleanContext):
        pass

    # Exit a parse tree produced by D96Parser#operator_boolean.
    def exitOperator_boolean(self, ctx:D96Parser.Operator_booleanContext):
        pass


    # Enter a parse tree produced by D96Parser#operator_integer.
    def enterOperator_integer(self, ctx:D96Parser.Operator_integerContext):
        pass

    # Exit a parse tree produced by D96Parser#operator_integer.
    def exitOperator_integer(self, ctx:D96Parser.Operator_integerContext):
        pass


    # Enter a parse tree produced by D96Parser#operator_float.
    def enterOperator_float(self, ctx:D96Parser.Operator_floatContext):
        pass

    # Exit a parse tree produced by D96Parser#operator_float.
    def exitOperator_float(self, ctx:D96Parser.Operator_floatContext):
        pass


    # Enter a parse tree produced by D96Parser#operator_string.
    def enterOperator_string(self, ctx:D96Parser.Operator_stringContext):
        pass

    # Exit a parse tree produced by D96Parser#operator_string.
    def exitOperator_string(self, ctx:D96Parser.Operator_stringContext):
        pass


    # Enter a parse tree produced by D96Parser#primitive_type.
    def enterPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#primitive_type.
    def exitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#array_type.
    def enterArray_type(self, ctx:D96Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#array_type.
    def exitArray_type(self, ctx:D96Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#class_type.
    def enterClass_type(self, ctx:D96Parser.Class_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#class_type.
    def exitClass_type(self, ctx:D96Parser.Class_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#many_class.
    def enterMany_class(self, ctx:D96Parser.Many_classContext):
        pass

    # Exit a parse tree produced by D96Parser#many_class.
    def exitMany_class(self, ctx:D96Parser.Many_classContext):
        pass


    # Enter a parse tree produced by D96Parser#class_declaration.
    def enterClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#class_declaration.
    def exitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        pass


    # Enter a parse tree produced by D96Parser#class_body.
    def enterClass_body(self, ctx:D96Parser.Class_bodyContext):
        pass

    # Exit a parse tree produced by D96Parser#class_body.
    def exitClass_body(self, ctx:D96Parser.Class_bodyContext):
        pass


    # Enter a parse tree produced by D96Parser#class_body_unit.
    def enterClass_body_unit(self, ctx:D96Parser.Class_body_unitContext):
        pass

    # Exit a parse tree produced by D96Parser#class_body_unit.
    def exitClass_body_unit(self, ctx:D96Parser.Class_body_unitContext):
        pass


    # Enter a parse tree produced by D96Parser#super_class_group.
    def enterSuper_class_group(self, ctx:D96Parser.Super_class_groupContext):
        pass

    # Exit a parse tree produced by D96Parser#super_class_group.
    def exitSuper_class_group(self, ctx:D96Parser.Super_class_groupContext):
        pass


    # Enter a parse tree produced by D96Parser#program_class_declaration.
    def enterProgram_class_declaration(self, ctx:D96Parser.Program_class_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#program_class_declaration.
    def exitProgram_class_declaration(self, ctx:D96Parser.Program_class_declarationContext):
        pass


    # Enter a parse tree produced by D96Parser#program_class_body.
    def enterProgram_class_body(self, ctx:D96Parser.Program_class_bodyContext):
        pass

    # Exit a parse tree produced by D96Parser#program_class_body.
    def exitProgram_class_body(self, ctx:D96Parser.Program_class_bodyContext):
        pass


    # Enter a parse tree produced by D96Parser#main_method_declaration.
    def enterMain_method_declaration(self, ctx:D96Parser.Main_method_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#main_method_declaration.
    def exitMain_method_declaration(self, ctx:D96Parser.Main_method_declarationContext):
        pass


    # Enter a parse tree produced by D96Parser#method_declaration.
    def enterMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#method_declaration.
    def exitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        pass


    # Enter a parse tree produced by D96Parser#constructor.
    def enterConstructor(self, ctx:D96Parser.ConstructorContext):
        pass

    # Exit a parse tree produced by D96Parser#constructor.
    def exitConstructor(self, ctx:D96Parser.ConstructorContext):
        pass


    # Enter a parse tree produced by D96Parser#destructor.
    def enterDestructor(self, ctx:D96Parser.DestructorContext):
        pass

    # Exit a parse tree produced by D96Parser#destructor.
    def exitDestructor(self, ctx:D96Parser.DestructorContext):
        pass


    # Enter a parse tree produced by D96Parser#parameter_list.
    def enterParameter_list(self, ctx:D96Parser.Parameter_listContext):
        pass

    # Exit a parse tree produced by D96Parser#parameter_list.
    def exitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        pass


    # Enter a parse tree produced by D96Parser#parameter_list_tail.
    def enterParameter_list_tail(self, ctx:D96Parser.Parameter_list_tailContext):
        pass

    # Exit a parse tree produced by D96Parser#parameter_list_tail.
    def exitParameter_list_tail(self, ctx:D96Parser.Parameter_list_tailContext):
        pass


    # Enter a parse tree produced by D96Parser#parameter.
    def enterParameter(self, ctx:D96Parser.ParameterContext):
        pass

    # Exit a parse tree produced by D96Parser#parameter.
    def exitParameter(self, ctx:D96Parser.ParameterContext):
        pass


    # Enter a parse tree produced by D96Parser#method_body.
    def enterMethod_body(self, ctx:D96Parser.Method_bodyContext):
        pass

    # Exit a parse tree produced by D96Parser#method_body.
    def exitMethod_body(self, ctx:D96Parser.Method_bodyContext):
        pass


    # Enter a parse tree produced by D96Parser#attribute_declaration.
    def enterAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#attribute_declaration.
    def exitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        pass


    # Enter a parse tree produced by D96Parser#identifier_list.
    def enterIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        pass

    # Exit a parse tree produced by D96Parser#identifier_list.
    def exitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        pass


    # Enter a parse tree produced by D96Parser#identifier_list_tail.
    def enterIdentifier_list_tail(self, ctx:D96Parser.Identifier_list_tailContext):
        pass

    # Exit a parse tree produced by D96Parser#identifier_list_tail.
    def exitIdentifier_list_tail(self, ctx:D96Parser.Identifier_list_tailContext):
        pass


    # Enter a parse tree produced by D96Parser#statement.
    def enterStatement(self, ctx:D96Parser.StatementContext):
        pass

    # Exit a parse tree produced by D96Parser#statement.
    def exitStatement(self, ctx:D96Parser.StatementContext):
        pass


    # Enter a parse tree produced by D96Parser#expression_list.
    def enterExpression_list(self, ctx:D96Parser.Expression_listContext):
        pass

    # Exit a parse tree produced by D96Parser#expression_list.
    def exitExpression_list(self, ctx:D96Parser.Expression_listContext):
        pass


    # Enter a parse tree produced by D96Parser#expression_list_tail.
    def enterExpression_list_tail(self, ctx:D96Parser.Expression_list_tailContext):
        pass

    # Exit a parse tree produced by D96Parser#expression_list_tail.
    def exitExpression_list_tail(self, ctx:D96Parser.Expression_list_tailContext):
        pass


    # Enter a parse tree produced by D96Parser#return.
    def enterReturn(self, ctx:D96Parser.ReturnContext):
        pass

    # Exit a parse tree produced by D96Parser#return.
    def exitReturn(self, ctx:D96Parser.ReturnContext):
        pass


    # Enter a parse tree produced by D96Parser#expression.
    def enterExpression(self, ctx:D96Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by D96Parser#expression.
    def exitExpression(self, ctx:D96Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by D96Parser#operation.
    def enterOperation(self, ctx:D96Parser.OperationContext):
        pass

    # Exit a parse tree produced by D96Parser#operation.
    def exitOperation(self, ctx:D96Parser.OperationContext):
        pass


    # Enter a parse tree produced by D96Parser#unary_operation.
    def enterUnary_operation(self, ctx:D96Parser.Unary_operationContext):
        pass

    # Exit a parse tree produced by D96Parser#unary_operation.
    def exitUnary_operation(self, ctx:D96Parser.Unary_operationContext):
        pass


    # Enter a parse tree produced by D96Parser#binary_operation.
    def enterBinary_operation(self, ctx:D96Parser.Binary_operationContext):
        pass

    # Exit a parse tree produced by D96Parser#binary_operation.
    def exitBinary_operation(self, ctx:D96Parser.Binary_operationContext):
        pass


    # Enter a parse tree produced by D96Parser#int_operation.
    def enterInt_operation(self, ctx:D96Parser.Int_operationContext):
        pass

    # Exit a parse tree produced by D96Parser#int_operation.
    def exitInt_operation(self, ctx:D96Parser.Int_operationContext):
        pass


    # Enter a parse tree produced by D96Parser#float_operation.
    def enterFloat_operation(self, ctx:D96Parser.Float_operationContext):
        pass

    # Exit a parse tree produced by D96Parser#float_operation.
    def exitFloat_operation(self, ctx:D96Parser.Float_operationContext):
        pass


    # Enter a parse tree produced by D96Parser#int_operand.
    def enterInt_operand(self, ctx:D96Parser.Int_operandContext):
        pass

    # Exit a parse tree produced by D96Parser#int_operand.
    def exitInt_operand(self, ctx:D96Parser.Int_operandContext):
        pass


    # Enter a parse tree produced by D96Parser#float_operand.
    def enterFloat_operand(self, ctx:D96Parser.Float_operandContext):
        pass

    # Exit a parse tree produced by D96Parser#float_operand.
    def exitFloat_operand(self, ctx:D96Parser.Float_operandContext):
        pass


    # Enter a parse tree produced by D96Parser#int_float_operand.
    def enterInt_float_operand(self, ctx:D96Parser.Int_float_operandContext):
        pass

    # Exit a parse tree produced by D96Parser#int_float_operand.
    def exitInt_float_operand(self, ctx:D96Parser.Int_float_operandContext):
        pass


    # Enter a parse tree produced by D96Parser#function_call.
    def enterFunction_call(self, ctx:D96Parser.Function_callContext):
        pass

    # Exit a parse tree produced by D96Parser#function_call.
    def exitFunction_call(self, ctx:D96Parser.Function_callContext):
        pass


    # Enter a parse tree produced by D96Parser#boolean_operation.
    def enterBoolean_operation(self, ctx:D96Parser.Boolean_operationContext):
        pass

    # Exit a parse tree produced by D96Parser#boolean_operation.
    def exitBoolean_operation(self, ctx:D96Parser.Boolean_operationContext):
        pass


    # Enter a parse tree produced by D96Parser#boolean_operand.
    def enterBoolean_operand(self, ctx:D96Parser.Boolean_operandContext):
        pass

    # Exit a parse tree produced by D96Parser#boolean_operand.
    def exitBoolean_operand(self, ctx:D96Parser.Boolean_operandContext):
        pass



del D96Parser