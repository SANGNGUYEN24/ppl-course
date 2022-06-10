;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Apr 19 15:43:35 ICT 2022

.source test.java
.class public test
.super java/lang/Object

.field static a I

.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this Ltest; from Label0 to Label1

Label0:
.line 1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 3
.limit locals 2
.var 0 is arg0 [Ljava/lang/String; from Label2 to Label3

Label2:
.line 4
	iconst_0
	istore_1
.line 5
	getstatic java.lang.System.out Ljava/io/PrintStream;
	iload_1
	getstatic test.a I
	if_icmpge Label0
	iconst_1
	goto Label1
Label0:
	iconst_0
Label1:
	invokevirtual java/io/PrintStream/println(Z)V
Label3:
.line 6
	return

.end method

.method static <clinit>()V
.limit stack 1
.limit locals 0

.line 2
	iconst_1
	putstatic test.a I
	return

.end method
