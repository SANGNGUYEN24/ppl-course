# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\6\138\n\13\r\13\16\139\3\13\7\13=\n\13\f\13\16\13@\13")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2I\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\37\3\2")
        buf.write("\2\2\7%\3\2\2\2\t*\3\2\2\2\13,\3\2\2\2\r.\3\2\2\2\17\60")
        buf.write("\3\2\2\2\21\62\3\2\2\2\23\64\3\2\2\2\25\67\3\2\2\2\27")
        buf.write("A\3\2\2\2\31E\3\2\2\2\33\34\7k\2\2\34\35\7p\2\2\35\36")
        buf.write("\7v\2\2\36\4\3\2\2\2\37 \7h\2\2 !\7n\2\2!\"\7q\2\2\"#")
        buf.write("\7c\2\2#$\7v\2\2$\6\3\2\2\2%&\7d\2\2&\'\7q\2\2\'(\7f\2")
        buf.write("\2()\7{\2\2)\b\3\2\2\2*+\7=\2\2+\n\3\2\2\2,-\7.\2\2-\f")
        buf.write("\3\2\2\2./\7*\2\2/\16\3\2\2\2\60\61\7+\2\2\61\20\3\2\2")
        buf.write("\2\62\63\7}\2\2\63\22\3\2\2\2\64\65\7\177\2\2\65\24\3")
        buf.write("\2\2\2\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\2")
        buf.write("9:\3\2\2\2:>\3\2\2\2;=\t\3\2\2<;\3\2\2\2=@\3\2\2\2><\3")
        buf.write("\2\2\2>?\3\2\2\2?\26\3\2\2\2@>\3\2\2\2AB\t\4\2\2BC\3\2")
        buf.write("\2\2CD\b\f\2\2D\30\3\2\2\2EF\13\2\2\2FG\b\r\3\2G\32\3")
        buf.write("\2\2\2\5\29>\4\b\2\2\3\r\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    SEMI_COLON = 4
    COMMA = 5
    LEFT_PAREN = 6
    RIGHT_PAREN = 7
    LEFT_CURLY_BRACKET = 8
    RIGHT_CURLY_BRACKET = 9
    ID = 10
    WS = 11
    ERROR_CHAR = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'body'", "';'", "','", "'('", "')'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI_COLON", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "SEMI_COLON", "COMMA", "LEFT_PAREN", 
                  "RIGHT_PAREN", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


