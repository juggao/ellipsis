# Generated from SimpleArithmetic.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleArithmeticParser import SimpleArithmeticParser
else:
    from SimpleArithmeticParser import SimpleArithmeticParser

# This class defines a complete generic visitor for a parse tree produced by SimpleArithmeticParser.

class SimpleArithmeticVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleArithmeticParser#start.
    def visitStart(self, ctx:SimpleArithmeticParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleArithmeticParser#expr.
    def visitExpr(self, ctx:SimpleArithmeticParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleArithmeticParser#term.
    def visitTerm(self, ctx:SimpleArithmeticParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleArithmeticParser#factor.
    def visitFactor(self, ctx:SimpleArithmeticParser.FactorContext):
        return self.visitChildren(ctx)



del SimpleArithmeticParser