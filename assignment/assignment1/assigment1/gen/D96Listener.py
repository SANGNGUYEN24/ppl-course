# Generated from C:/development-area/ppl/ppl-course/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#class_declaration.
    def enterClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#class_declaration.
    def exitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
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


    # Enter a parse tree produced by D96Parser#parameter.
    def enterParameter(self, ctx:D96Parser.ParameterContext):
        pass

    # Exit a parse tree produced by D96Parser#parameter.
    def exitParameter(self, ctx:D96Parser.ParameterContext):
        pass


    # Enter a parse tree produced by D96Parser#d96_type.
    def enterD96_type(self, ctx:D96Parser.D96_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#d96_type.
    def exitD96_type(self, ctx:D96Parser.D96_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#attribute_declaration.
    def enterAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        pass

    # Exit a parse tree produced by D96Parser#attribute_declaration.
    def exitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        pass


    # Enter a parse tree produced by D96Parser#attribute_value_list.
    def enterAttribute_value_list(self, ctx:D96Parser.Attribute_value_listContext):
        pass

    # Exit a parse tree produced by D96Parser#attribute_value_list.
    def exitAttribute_value_list(self, ctx:D96Parser.Attribute_value_listContext):
        pass


    # Enter a parse tree produced by D96Parser#identifier_list.
    def enterIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        pass

    # Exit a parse tree produced by D96Parser#identifier_list.
    def exitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        pass


    # Enter a parse tree produced by D96Parser#mixed_identifier_list.
    def enterMixed_identifier_list(self, ctx:D96Parser.Mixed_identifier_listContext):
        pass

    # Exit a parse tree produced by D96Parser#mixed_identifier_list.
    def exitMixed_identifier_list(self, ctx:D96Parser.Mixed_identifier_listContext):
        pass


    # Enter a parse tree produced by D96Parser#expression_list.
    def enterExpression_list(self, ctx:D96Parser.Expression_listContext):
        pass

    # Exit a parse tree produced by D96Parser#expression_list.
    def exitExpression_list(self, ctx:D96Parser.Expression_listContext):
        pass


    # Enter a parse tree produced by D96Parser#element_expression.
    def enterElement_expression(self, ctx:D96Parser.Element_expressionContext):
        pass

    # Exit a parse tree produced by D96Parser#element_expression.
    def exitElement_expression(self, ctx:D96Parser.Element_expressionContext):
        pass


    # Enter a parse tree produced by D96Parser#index_operator.
    def enterIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#index_operator.
    def exitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#relational_operator.
    def enterRelational_operator(self, ctx:D96Parser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#relational_operator.
    def exitRelational_operator(self, ctx:D96Parser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#expression.
    def enterExpression(self, ctx:D96Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by D96Parser#expression.
    def exitExpression(self, ctx:D96Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by D96Parser#relational_expr.
    def enterRelational_expr(self, ctx:D96Parser.Relational_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#relational_expr.
    def exitRelational_expr(self, ctx:D96Parser.Relational_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#and_or_expr.
    def enterAnd_or_expr(self, ctx:D96Parser.And_or_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#and_or_expr.
    def exitAnd_or_expr(self, ctx:D96Parser.And_or_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#add_sub_expr.
    def enterAdd_sub_expr(self, ctx:D96Parser.Add_sub_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#add_sub_expr.
    def exitAdd_sub_expr(self, ctx:D96Parser.Add_sub_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#mul_add_mol_expr.
    def enterMul_add_mol_expr(self, ctx:D96Parser.Mul_add_mol_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#mul_add_mol_expr.
    def exitMul_add_mol_expr(self, ctx:D96Parser.Mul_add_mol_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#not_expr.
    def enterNot_expr(self, ctx:D96Parser.Not_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#not_expr.
    def exitNot_expr(self, ctx:D96Parser.Not_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#sign_expr.
    def enterSign_expr(self, ctx:D96Parser.Sign_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#sign_expr.
    def exitSign_expr(self, ctx:D96Parser.Sign_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#index_operator_expr.
    def enterIndex_operator_expr(self, ctx:D96Parser.Index_operator_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#index_operator_expr.
    def exitIndex_operator_expr(self, ctx:D96Parser.Index_operator_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#instance_access.
    def enterInstance_access(self, ctx:D96Parser.Instance_accessContext):
        pass

    # Exit a parse tree produced by D96Parser#instance_access.
    def exitInstance_access(self, ctx:D96Parser.Instance_accessContext):
        pass


    # Enter a parse tree produced by D96Parser#static_access.
    def enterStatic_access(self, ctx:D96Parser.Static_accessContext):
        pass

    # Exit a parse tree produced by D96Parser#static_access.
    def exitStatic_access(self, ctx:D96Parser.Static_accessContext):
        pass


    # Enter a parse tree produced by D96Parser#object_creation.
    def enterObject_creation(self, ctx:D96Parser.Object_creationContext):
        pass

    # Exit a parse tree produced by D96Parser#object_creation.
    def exitObject_creation(self, ctx:D96Parser.Object_creationContext):
        pass


    # Enter a parse tree produced by D96Parser#atom_expr.
    def enterAtom_expr(self, ctx:D96Parser.Atom_exprContext):
        pass

    # Exit a parse tree produced by D96Parser#atom_expr.
    def exitAtom_expr(self, ctx:D96Parser.Atom_exprContext):
        pass


    # Enter a parse tree produced by D96Parser#var_val_statement.
    def enterVar_val_statement(self, ctx:D96Parser.Var_val_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#var_val_statement.
    def exitVar_val_statement(self, ctx:D96Parser.Var_val_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#var_val_value_list.
    def enterVar_val_value_list(self, ctx:D96Parser.Var_val_value_listContext):
        pass

    # Exit a parse tree produced by D96Parser#var_val_value_list.
    def exitVar_val_value_list(self, ctx:D96Parser.Var_val_value_listContext):
        pass


    # Enter a parse tree produced by D96Parser#lhs.
    def enterLhs(self, ctx:D96Parser.LhsContext):
        pass

    # Exit a parse tree produced by D96Parser#lhs.
    def exitLhs(self, ctx:D96Parser.LhsContext):
        pass


    # Enter a parse tree produced by D96Parser#assign_statement.
    def enterAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#assign_statement.
    def exitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#if_statement.
    def enterIf_statement(self, ctx:D96Parser.If_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#if_statement.
    def exitIf_statement(self, ctx:D96Parser.If_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#if_part.
    def enterIf_part(self, ctx:D96Parser.If_partContext):
        pass

    # Exit a parse tree produced by D96Parser#if_part.
    def exitIf_part(self, ctx:D96Parser.If_partContext):
        pass


    # Enter a parse tree produced by D96Parser#else_if_part.
    def enterElse_if_part(self, ctx:D96Parser.Else_if_partContext):
        pass

    # Exit a parse tree produced by D96Parser#else_if_part.
    def exitElse_if_part(self, ctx:D96Parser.Else_if_partContext):
        pass


    # Enter a parse tree produced by D96Parser#else_part.
    def enterElse_part(self, ctx:D96Parser.Else_partContext):
        pass

    # Exit a parse tree produced by D96Parser#else_part.
    def exitElse_part(self, ctx:D96Parser.Else_partContext):
        pass


    # Enter a parse tree produced by D96Parser#for_in_statement.
    def enterFor_in_statement(self, ctx:D96Parser.For_in_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#for_in_statement.
    def exitFor_in_statement(self, ctx:D96Parser.For_in_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#loop_part.
    def enterLoop_part(self, ctx:D96Parser.Loop_partContext):
        pass

    # Exit a parse tree produced by D96Parser#loop_part.
    def exitLoop_part(self, ctx:D96Parser.Loop_partContext):
        pass


    # Enter a parse tree produced by D96Parser#break_statement.
    def enterBreak_statement(self, ctx:D96Parser.Break_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#break_statement.
    def exitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#continue_statement.
    def enterContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#continue_statement.
    def exitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#return_statement.
    def enterReturn_statement(self, ctx:D96Parser.Return_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#return_statement.
    def exitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#member_access.
    def enterMember_access(self, ctx:D96Parser.Member_accessContext):
        pass

    # Exit a parse tree produced by D96Parser#member_access.
    def exitMember_access(self, ctx:D96Parser.Member_accessContext):
        pass


    # Enter a parse tree produced by D96Parser#method_invocation_statement.
    def enterMethod_invocation_statement(self, ctx:D96Parser.Method_invocation_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#method_invocation_statement.
    def exitMethod_invocation_statement(self, ctx:D96Parser.Method_invocation_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#block_statement.
    def enterBlock_statement(self, ctx:D96Parser.Block_statementContext):
        pass

    # Exit a parse tree produced by D96Parser#block_statement.
    def exitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        pass


    # Enter a parse tree produced by D96Parser#statement.
    def enterStatement(self, ctx:D96Parser.StatementContext):
        pass

    # Exit a parse tree produced by D96Parser#statement.
    def exitStatement(self, ctx:D96Parser.StatementContext):
        pass


    # Enter a parse tree produced by D96Parser#literal.
    def enterLiteral(self, ctx:D96Parser.LiteralContext):
        pass

    # Exit a parse tree produced by D96Parser#literal.
    def exitLiteral(self, ctx:D96Parser.LiteralContext):
        pass


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



del D96Parser