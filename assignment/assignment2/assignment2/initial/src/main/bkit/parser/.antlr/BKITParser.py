# Generated from /home/ngoctho/Documents/PPL/assignment/assignment2/assignment2/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u01a9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\7\2b\n\2\f\2\16\2e\13\2\3\2\7\2h\n")
        buf.write("\2\f\2\16\2k\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\7\4w\n\4\f\4\16\4z\13\4\3\5\3\5\3\5\3\5\7\5\u0080")
        buf.write("\n\5\f\5\16\5\u0083\13\5\3\5\3\5\5\5\u0087\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u008f\n\6\3\6\3\6\3\7\3\7\3\7\7\7")
        buf.write("\u0096\n\7\f\7\16\7\u0099\13\7\3\b\3\b\3\b\3\b\7\b\u009f")
        buf.write("\n\b\f\b\16\b\u00a2\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\7")
        buf.write("\n\u00ab\n\n\f\n\16\n\u00ae\13\n\3\n\7\n\u00b1\n\n\f\n")
        buf.write("\16\n\u00b4\13\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00bc")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00c5\n\r\3\r\7")
        buf.write("\r\u00c8\n\r\f\r\16\r\u00cb\13\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\7\16\u00d6\n\16\f\16\16\16\u00d9")
        buf.write("\13\16\3\16\3\16\5\16\u00dd\n\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\5\17\u00e5\n\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\5\21\u00f3\n\21\3\21\3")
        buf.write("\21\5\21\u00f7\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\5\27\u0111\n\27\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\5\33\u011f\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\7\34\u0129\n\34\f\34\16\34\u012c\13\34\3\35\3\35\5")
        buf.write("\35\u0130\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u0139\n\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \7 \u0144\n")
        buf.write(" \f \16 \u0147\13 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7")
        buf.write("\"\u0152\n\"\f\"\16\"\u0155\13\"\3#\3#\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\7$\u0160\n$\f$\16$\u0163\13$\3%\3%\3&\3&\3&\5&")
        buf.write("\u016a\n&\3\'\3\'\3\'\3\'\5\'\u0170\n\'\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\7)\u0179\n)\f)\16)\u017c\13)\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\5+\u0188\n+\3,\3,\3,\3,\3,\3,\3,\5,\u0191")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u0198\n-\3.\3.\3/\3/\3/\3/\7/\u01a0")
        buf.write("\n/\f/\16/\u01a3\13/\3/\3/\3\60\3\60\3\60\2\7\66>BFP\61")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^\2\b\3\2%/\3\2#$\5\2\31\32")
        buf.write("\36\36  \5\2\33\35\37\37!!\4\2\32\32\36\36\4\2\23\23\30")
        buf.write("\30\2\u01a4\2c\3\2\2\2\4n\3\2\2\2\6s\3\2\2\2\b{\3\2\2")
        buf.write("\2\n\u0088\3\2\2\2\f\u0092\3\2\2\2\16\u009a\3\2\2\2\20")
        buf.write("\u00a3\3\2\2\2\22\u00ac\3\2\2\2\24\u00bb\3\2\2\2\26\u00bd")
        buf.write("\3\2\2\2\30\u00c4\3\2\2\2\32\u00cc\3\2\2\2\34\u00e4\3")
        buf.write("\2\2\2\36\u00e6\3\2\2\2 \u00ef\3\2\2\2\"\u00f8\3\2\2\2")
        buf.write("$\u00fc\3\2\2\2&\u00fe\3\2\2\2(\u0100\3\2\2\2*\u0107\3")
        buf.write("\2\2\2,\u0110\3\2\2\2.\u0112\3\2\2\2\60\u0115\3\2\2\2")
        buf.write("\62\u0118\3\2\2\2\64\u011b\3\2\2\2\66\u0122\3\2\2\28\u012d")
        buf.write("\3\2\2\2:\u0138\3\2\2\2<\u013a\3\2\2\2>\u013c\3\2\2\2")
        buf.write("@\u0148\3\2\2\2B\u014a\3\2\2\2D\u0156\3\2\2\2F\u0158\3")
        buf.write("\2\2\2H\u0164\3\2\2\2J\u0169\3\2\2\2L\u016f\3\2\2\2N\u0171")
        buf.write("\3\2\2\2P\u0173\3\2\2\2R\u017d\3\2\2\2T\u0187\3\2\2\2")
        buf.write("V\u0190\3\2\2\2X\u0197\3\2\2\2Z\u0199\3\2\2\2\\\u019b")
        buf.write("\3\2\2\2^\u01a6\3\2\2\2`b\5\4\3\2a`\3\2\2\2be\3\2\2\2")
        buf.write("ca\3\2\2\2cd\3\2\2\2di\3\2\2\2ec\3\2\2\2fh\5\n\6\2gf\3")
        buf.write("\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2")
        buf.write("\2lm\7\2\2\3m\3\3\2\2\2no\7\b\2\2op\7\64\2\2pq\5\6\4\2")
        buf.write("qr\78\2\2r\5\3\2\2\2sx\5\b\5\2tu\7\67\2\2uw\5\b\5\2vt")
        buf.write("\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y\7\3\2\2\2zx\3")
        buf.write("\2\2\2{\u0081\7\3\2\2|}\7\62\2\2}~\7<\2\2~\u0080\7\63")
        buf.write("\2\2\177|\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0086\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\7;\2\2\u0085\u0087\5X-\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\t\3\2\2\2\u0088\u0089")
        buf.write("\7\26\2\2\u0089\u008a\7\64\2\2\u008a\u008e\7\3\2\2\u008b")
        buf.write("\u008c\7\r\2\2\u008c\u008d\7\64\2\2\u008d\u008f\5\f\7")
        buf.write("\2\u008e\u008b\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090")
        buf.write("\3\2\2\2\u0090\u0091\5\20\t\2\u0091\13\3\2\2\2\u0092\u0097")
        buf.write("\5\16\b\2\u0093\u0094\7\67\2\2\u0094\u0096\5\16\b\2\u0095")
        buf.write("\u0093\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\r\3\2\2\2\u0099\u0097\3\2\2")
        buf.write("\2\u009a\u00a0\7\3\2\2\u009b\u009c\7\62\2\2\u009c\u009d")
        buf.write("\7<\2\2\u009d\u009f\7\63\2\2\u009e\u009b\3\2\2\2\u009f")
        buf.write("\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\17\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\7\4")
        buf.write("\2\2\u00a4\u00a5\7\64\2\2\u00a5\u00a6\5\22\n\2\u00a6\u00a7")
        buf.write("\7\20\2\2\u00a7\u00a8\7\65\2\2\u00a8\21\3\2\2\2\u00a9")
        buf.write("\u00ab\5\4\3\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b2\3")
        buf.write("\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\5\24\13\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\23\3\2\2\2\u00b4\u00b2\3\2")
        buf.write("\2\2\u00b5\u00bc\5\26\f\2\u00b6\u00bc\5\34\17\2\u00b7")
        buf.write("\u00bc\5,\27\2\u00b8\u00bc\5\62\32\2\u00b9\u00bc\58\35")
        buf.write("\2\u00ba\u00bc\5\32\16\2\u00bb\u00b5\3\2\2\2\u00bb\u00b6")
        buf.write("\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\25\3\2\2\2\u00bd")
        buf.write("\u00be\5\30\r\2\u00be\u00bf\7;\2\2\u00bf\u00c0\5:\36\2")
        buf.write("\u00c0\u00c1\78\2\2\u00c1\27\3\2\2\2\u00c2\u00c5\7\3\2")
        buf.write("\2\u00c3\u00c5\5\64\33\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c9\3\2\2\2\u00c6\u00c8\5R*\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\31\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write("\u00cd\7\7\2\2\u00cd\u00ce\5:\36\2\u00ce\u00cf\7\27\2")
        buf.write("\2\u00cf\u00d7\5\22\n\2\u00d0\u00d1\7\13\2\2\u00d1\u00d2")
        buf.write("\5:\36\2\u00d2\u00d3\7\27\2\2\u00d3\u00d4\5\22\n\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d6\u00d9\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00dc\3")
        buf.write("\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7\5\2\2\u00db\u00dd")
        buf.write("\5\22\n\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00df\7\25\2\2\u00df\u00e0\7\65\2")
        buf.write("\2\u00e0\33\3\2\2\2\u00e1\u00e5\5\36\20\2\u00e2\u00e5")
        buf.write("\5(\25\2\u00e3\u00e5\5*\26\2\u00e4\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\35\3\2\2\2\u00e6")
        buf.write("\u00e7\7\21\2\2\u00e7\u00e8\7\60\2\2\u00e8\u00e9\5 \21")
        buf.write("\2\u00e9\u00ea\7\61\2\2\u00ea\u00eb\7\24\2\2\u00eb\u00ec")
        buf.write("\5\22\n\2\u00ec\u00ed\7\6\2\2\u00ed\u00ee\7\65\2\2\u00ee")
        buf.write("\37\3\2\2\2\u00ef\u00f0\5\"\22\2\u00f0\u00f2\7\67\2\2")
        buf.write("\u00f1\u00f3\5$\23\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3")
        buf.write("\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\7\67\2\2\u00f5")
        buf.write("\u00f7\5&\24\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7!\3\2\2\2\u00f8\u00f9\7\3\2\2\u00f9\u00fa\7;\2\2")
        buf.write("\u00fa\u00fb\5:\36\2\u00fb#\3\2\2\2\u00fc\u00fd\5:\36")
        buf.write("\2\u00fd%\3\2\2\2\u00fe\u00ff\5:\36\2\u00ff\'\3\2\2\2")
        buf.write("\u0100\u0101\7\16\2\2\u0101\u0102\5:\36\2\u0102\u0103")
        buf.write("\7\24\2\2\u0103\u0104\5\22\n\2\u0104\u0105\7\f\2\2\u0105")
        buf.write("\u0106\7\65\2\2\u0106)\3\2\2\2\u0107\u0108\7\24\2\2\u0108")
        buf.write("\u0109\5\22\n\2\u0109\u010a\7\16\2\2\u010a\u010b\5:\36")
        buf.write("\2\u010b\u010c\7\t\2\2\u010c\u010d\7\65\2\2\u010d+\3\2")
        buf.write("\2\2\u010e\u0111\5.\30\2\u010f\u0111\5\60\31\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u010f\3\2\2\2\u0111-\3\2\2\2\u0112\u0113")
        buf.write("\7\n\2\2\u0113\u0114\78\2\2\u0114/\3\2\2\2\u0115\u0116")
        buf.write("\7\17\2\2\u0116\u0117\78\2\2\u0117\61\3\2\2\2\u0118\u0119")
        buf.write("\5\64\33\2\u0119\u011a\78\2\2\u011a\63\3\2\2\2\u011b\u011c")
        buf.write("\7\3\2\2\u011c\u011e\7\60\2\2\u011d\u011f\5\66\34\2\u011e")
        buf.write("\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0121\7\61\2\2\u0121\65\3\2\2\2\u0122\u0123\b\34")
        buf.write("\1\2\u0123\u0124\5:\36\2\u0124\u012a\3\2\2\2\u0125\u0126")
        buf.write("\f\4\2\2\u0126\u0127\7\67\2\2\u0127\u0129\5:\36\2\u0128")
        buf.write("\u0125\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\67\3\2\2\2\u012c\u012a\3\2")
        buf.write("\2\2\u012d\u012f\7\22\2\2\u012e\u0130\5:\36\2\u012f\u012e")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u0132\78\2\2\u01329\3\2\2\2\u0133\u0134\5> \2\u0134\u0135")
        buf.write("\5<\37\2\u0135\u0136\5> \2\u0136\u0139\3\2\2\2\u0137\u0139")
        buf.write("\5> \2\u0138\u0133\3\2\2\2\u0138\u0137\3\2\2\2\u0139;")
        buf.write("\3\2\2\2\u013a\u013b\t\2\2\2\u013b=\3\2\2\2\u013c\u013d")
        buf.write("\b \1\2\u013d\u013e\5B\"\2\u013e\u0145\3\2\2\2\u013f\u0140")
        buf.write("\f\4\2\2\u0140\u0141\5@!\2\u0141\u0142\5B\"\2\u0142\u0144")
        buf.write("\3\2\2\2\u0143\u013f\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146?\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0148\u0149\t\3\2\2\u0149A\3\2\2\2\u014a")
        buf.write("\u014b\b\"\1\2\u014b\u014c\5F$\2\u014c\u0153\3\2\2\2\u014d")
        buf.write("\u014e\f\4\2\2\u014e\u014f\5D#\2\u014f\u0150\5F$\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014d\3\2\2\2\u0152\u0155\3\2\2\2")
        buf.write("\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154C\3\2\2")
        buf.write("\2\u0155\u0153\3\2\2\2\u0156\u0157\t\4\2\2\u0157E\3\2")
        buf.write("\2\2\u0158\u0159\b$\1\2\u0159\u015a\5J&\2\u015a\u0161")
        buf.write("\3\2\2\2\u015b\u015c\f\4\2\2\u015c\u015d\5H%\2\u015d\u015e")
        buf.write("\5J&\2\u015e\u0160\3\2\2\2\u015f\u015b\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("G\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\t\5\2\2\u0165")
        buf.write("I\3\2\2\2\u0166\u0167\7\"\2\2\u0167\u016a\5J&\2\u0168")
        buf.write("\u016a\5L\'\2\u0169\u0166\3\2\2\2\u0169\u0168\3\2\2\2")
        buf.write("\u016aK\3\2\2\2\u016b\u016c\5N(\2\u016c\u016d\5L\'\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u0170\5P)\2\u016f\u016b\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170M\3\2\2\2\u0171\u0172\t\6\2\2\u0172")
        buf.write("O\3\2\2\2\u0173\u0174\b)\1\2\u0174\u0175\5T+\2\u0175\u017a")
        buf.write("\3\2\2\2\u0176\u0177\f\4\2\2\u0177\u0179\5R*\2\u0178\u0176")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017bQ\3\2\2\2\u017c\u017a\3\2\2\2\u017d")
        buf.write("\u017e\7\62\2\2\u017e\u017f\5:\36\2\u017f\u0180\7\63\2")
        buf.write("\2\u0180S\3\2\2\2\u0181\u0182\5V,\2\u0182\u0183\7\62\2")
        buf.write("\2\u0183\u0184\5:\36\2\u0184\u0185\7\63\2\2\u0185\u0188")
        buf.write("\3\2\2\2\u0186\u0188\5V,\2\u0187\u0181\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188U\3\2\2\2\u0189\u0191\7\3\2\2\u018a\u0191")
        buf.write("\5X-\2\u018b\u0191\5\64\33\2\u018c\u018d\7\60\2\2\u018d")
        buf.write("\u018e\5:\36\2\u018e\u018f\7\61\2\2\u018f\u0191\3\2\2")
        buf.write("\2\u0190\u0189\3\2\2\2\u0190\u018a\3\2\2\2\u0190\u018b")
        buf.write("\3\2\2\2\u0190\u018c\3\2\2\2\u0191W\3\2\2\2\u0192\u0198")
        buf.write("\7<\2\2\u0193\u0198\7=\2\2\u0194\u0198\7>\2\2\u0195\u0198")
        buf.write("\5Z.\2\u0196\u0198\5\\/\2\u0197\u0192\3\2\2\2\u0197\u0193")
        buf.write("\3\2\2\2\u0197\u0194\3\2\2\2\u0197\u0195\3\2\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198Y\3\2\2\2\u0199\u019a\t\7\2\2\u019a")
        buf.write("[\3\2\2\2\u019b\u019c\79\2\2\u019c\u01a1\5X-\2\u019d\u019e")
        buf.write("\7\67\2\2\u019e\u01a0\5X-\2\u019f\u019d\3\2\2\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7")
        buf.write(":\2\2\u01a5]\3\2\2\2\u01a6\u01a7\7;\2\2\u01a7_\3\2\2\2")
        buf.write("#cix\u0081\u0086\u008e\u0097\u00a0\u00ac\u00b2\u00bb\u00c4")
        buf.write("\u00c9\u00d7\u00dc\u00e4\u00f2\u00f6\u0110\u011e\u012a")
        buf.write("\u012f\u0138\u0145\u0153\u0161\u0169\u016f\u017a\u0187")
        buf.write("\u0190\u0197\u01a1")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Else'", "'EndFor'", 
                     "'If'", "'Var'", "'EndDo'", "'Break'", "'ElseIf'", 
                     "'EndWhile'", "'Parameter'", "'While'", "'Continue'", 
                     "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
                     "'EndIf'", "'Function'", "'Then'", "'False'", "'+'", 
                     "'-'", "'*'", "'%'", "'\\'", "'-.'", "'\\.'", "'+.'", 
                     "'*.'", "'!'", "'||'", "'&&'", "'=='", "'<='", "'>.'", 
                     "'!='", "'>='", "'<=.'", "'<'", "'=/='", "'>=.'", "'>'", 
                     "'<.'", "'('", "')'", "'['", "']'", "':'", "'.'", "'_'", 
                     "','", "';'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "Identifier", "BODY", "ELSE", "ENDFOR", 
                      "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
                      "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
                      "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", 
                      "FALSE", "ADD", "SUB", "MUL", "MOD", "DIV", "SUBF", 
                      "DIVF", "ADDF", "MULF", "NOT", "OR", "AND", "EQ", 
                      "LE", "GTF", "NE", "GE", "LEF", "LT", "NEF", "GEF", 
                      "GT", "LTF", "LB", "RB", "LSB", "RSB", "COLON", "DOT", 
                      "UNDERSCORE", "COMMA", "SEMI", "LP", "RP", "ASSIGN", 
                      "IntegerConstant", "FloatingConstant", "String", "COMMENT", 
                      "WS", "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_variableStatement = 1
    RULE_varList = 2
    RULE_varDeclaration = 3
    RULE_funcDeclaration = 4
    RULE_paraList = 5
    RULE_parameters = 6
    RULE_funcBody = 7
    RULE_statementList = 8
    RULE_statement = 9
    RULE_assignmentStatement = 10
    RULE_assignDeclaration = 11
    RULE_ifStatement = 12
    RULE_iterationStatement = 13
    RULE_forStatement = 14
    RULE_forCondition = 15
    RULE_forDeclaration = 16
    RULE_conditionExpr = 17
    RULE_updateExpr = 18
    RULE_whileStatement = 19
    RULE_doWhileStatement = 20
    RULE_jumpStatement = 21
    RULE_breakStatement = 22
    RULE_continueStatement = 23
    RULE_callStatement = 24
    RULE_functionCall = 25
    RULE_argumentList = 26
    RULE_returnStatement = 27
    RULE_expression = 28
    RULE_relationalOperator = 29
    RULE_logicalOrAndExpression = 30
    RULE_logicalOrAndOperator = 31
    RULE_additiveExpression = 32
    RULE_additiveOperator = 33
    RULE_multiplicativeExpression = 34
    RULE_multiplicativeOperator = 35
    RULE_logicalNotExpression = 36
    RULE_signExpression = 37
    RULE_signOperator = 38
    RULE_indexExpression = 39
    RULE_indexOperator = 40
    RULE_funcExpression = 41
    RULE_primaryExpression = 42
    RULE_literals = 43
    RULE_boolean = 44
    RULE_array = 45
    RULE_assignmentOperator = 46

    ruleNames =  [ "program", "variableStatement", "varList", "varDeclaration", 
                   "funcDeclaration", "paraList", "parameters", "funcBody", 
                   "statementList", "statement", "assignmentStatement", 
                   "assignDeclaration", "ifStatement", "iterationStatement", 
                   "forStatement", "forCondition", "forDeclaration", "conditionExpr", 
                   "updateExpr", "whileStatement", "doWhileStatement", "jumpStatement", 
                   "breakStatement", "continueStatement", "callStatement", 
                   "functionCall", "argumentList", "returnStatement", "expression", 
                   "relationalOperator", "logicalOrAndExpression", "logicalOrAndOperator", 
                   "additiveExpression", "additiveOperator", "multiplicativeExpression", 
                   "multiplicativeOperator", "logicalNotExpression", "signExpression", 
                   "signOperator", "indexExpression", "indexOperator", "funcExpression", 
                   "primaryExpression", "literals", "boolean", "array", 
                   "assignmentOperator" ]

    EOF = Token.EOF
    Identifier=1
    BODY=2
    ELSE=3
    ENDFOR=4
    IF=5
    VAR=6
    ENDDO=7
    BREAK=8
    ELSEIF=9
    ENDWHILE=10
    PARAMETER=11
    WHILE=12
    CONTINUE=13
    ENDBODY=14
    FOR=15
    RETURN=16
    TRUE=17
    DO=18
    ENDIF=19
    FUNCTION=20
    THEN=21
    FALSE=22
    ADD=23
    SUB=24
    MUL=25
    MOD=26
    DIV=27
    SUBF=28
    DIVF=29
    ADDF=30
    MULF=31
    NOT=32
    OR=33
    AND=34
    EQ=35
    LE=36
    GTF=37
    NE=38
    GE=39
    LEF=40
    LT=41
    NEF=42
    GEF=43
    GT=44
    LTF=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    COLON=50
    DOT=51
    UNDERSCORE=52
    COMMA=53
    SEMI=54
    LP=55
    RP=56
    ASSIGN=57
    IntegerConstant=58
    FloatingConstant=59
    String=60
    COMMENT=61
    WS=62
    UNTERMINATED_COMMENT=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def variableStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VariableStatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.VariableStatementContext,i)


        def funcDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.FuncDeclarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.FuncDeclarationContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 94
                self.variableStatement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 100
                self.funcDeclaration()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def varList(self):
            return self.getTypedRuleContext(BKITParser.VarListContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_variableStatement




    def variableStatement(self):

        localctx = BKITParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BKITParser.VAR)
            self.state = 109
            self.match(BKITParser.COLON)
            self.state = 110
            self.varList()
            self.state = 111
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.VarDeclarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_varList




    def varList(self):

        localctx = BKITParser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.varDeclaration()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 114
                self.match(BKITParser.COMMA)
                self.state = 115
                self.varDeclaration()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def IntegerConstant(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.IntegerConstant)
            else:
                return self.getToken(BKITParser.IntegerConstant, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_varDeclaration




    def varDeclaration(self):

        localctx = BKITParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(BKITParser.Identifier)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 122
                self.match(BKITParser.LSB)
                self.state = 123
                self.match(BKITParser.IntegerConstant)
                self.state = 124
                self.match(BKITParser.RSB)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 130
                self.match(BKITParser.ASSIGN)
                self.state = 131
                self.literals()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def funcBody(self):
            return self.getTypedRuleContext(BKITParser.FuncBodyContext,0)


        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def paraList(self):
            return self.getTypedRuleContext(BKITParser.ParaListContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_funcDeclaration




    def funcDeclaration(self):

        localctx = BKITParser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKITParser.FUNCTION)
            self.state = 135
            self.match(BKITParser.COLON)
            self.state = 136
            self.match(BKITParser.Identifier)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 137
                self.match(BKITParser.PARAMETER)
                self.state = 138
                self.match(BKITParser.COLON)
                self.state = 139
                self.paraList()


            self.state = 142
            self.funcBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ParametersContext)
            else:
                return self.getTypedRuleContext(BKITParser.ParametersContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_paraList




    def paraList(self):

        localctx = BKITParser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.parameters()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 145
                self.match(BKITParser.COMMA)
                self.state = 146
                self.parameters()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def IntegerConstant(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.IntegerConstant)
            else:
                return self.getToken(BKITParser.IntegerConstant, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameters




    def parameters(self):

        localctx = BKITParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BKITParser.Identifier)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 153
                self.match(BKITParser.LSB)
                self.state = 154
                self.match(BKITParser.IntegerConstant)
                self.state = 155
                self.match(BKITParser.RSB)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(BKITParser.StatementListContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_funcBody




    def funcBody(self):

        localctx = BKITParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(BKITParser.BODY)
            self.state = 162
            self.match(BKITParser.COLON)
            self.state = 163
            self.statementList()
            self.state = 164
            self.match(BKITParser.ENDBODY)
            self.state = 165
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VariableStatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.VariableStatementContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_statementList




    def statementList(self):

        localctx = BKITParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 167
                self.variableStatement()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self.statement() 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(BKITParser.AssignmentStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(BKITParser.IterationStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(BKITParser.JumpStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(BKITParser.CallStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(BKITParser.ReturnStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(BKITParser.IfStatementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.iterationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.jumpStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.callStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 183
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 184
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignDeclaration(self):
            return self.getTypedRuleContext(BKITParser.AssignDeclarationContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignmentStatement




    def assignmentStatement(self):

        localctx = BKITParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.assignDeclaration()
            self.state = 188
            self.match(BKITParser.ASSIGN)
            self.state = 189
            self.expression()
            self.state = 190
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def functionCall(self):
            return self.getTypedRuleContext(BKITParser.FunctionCallContext,0)


        def indexOperator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.IndexOperatorContext)
            else:
                return self.getTypedRuleContext(BKITParser.IndexOperatorContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_assignDeclaration




    def assignDeclaration(self):

        localctx = BKITParser.AssignDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(BKITParser.Identifier)
                pass

            elif la_ == 2:
                self.state = 193
                self.functionCall()
                pass


            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 196
                self.indexOperator()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementListContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementListContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_ifStatement




    def ifStatement(self):

        localctx = BKITParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BKITParser.IF)
            self.state = 203
            self.expression()
            self.state = 204
            self.match(BKITParser.THEN)
            self.state = 205
            self.statementList()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 206
                self.match(BKITParser.ELSEIF)
                self.state = 207
                self.expression()
                self.state = 208
                self.match(BKITParser.THEN)
                self.state = 209
                self.statementList()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 216
                self.match(BKITParser.ELSE)
                self.state = 217
                self.statementList()


            self.state = 220
            self.match(BKITParser.ENDIF)
            self.state = 221
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forStatement(self):
            return self.getTypedRuleContext(BKITParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BKITParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(BKITParser.DoWhileStatementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_iterationStatement




    def iterationStatement(self):

        localctx = BKITParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iterationStatement)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.forStatement()
                pass
            elif token in [BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.whileStatement()
                pass
            elif token in [BKITParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.doWhileStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def forCondition(self):
            return self.getTypedRuleContext(BKITParser.ForConditionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statementList(self):
            return self.getTypedRuleContext(BKITParser.StatementListContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_forStatement




    def forStatement(self):

        localctx = BKITParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BKITParser.FOR)
            self.state = 229
            self.match(BKITParser.LB)
            self.state = 230
            self.forCondition()
            self.state = 231
            self.match(BKITParser.RB)
            self.state = 232
            self.match(BKITParser.DO)
            self.state = 233
            self.statementList()
            self.state = 234
            self.match(BKITParser.ENDFOR)
            self.state = 235
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forDeclaration(self):
            return self.getTypedRuleContext(BKITParser.ForDeclarationContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def conditionExpr(self):
            return self.getTypedRuleContext(BKITParser.ConditionExprContext,0)


        def updateExpr(self):
            return self.getTypedRuleContext(BKITParser.UpdateExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_forCondition




    def forCondition(self):

        localctx = BKITParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.forDeclaration()
            self.state = 238
            self.match(BKITParser.COMMA)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 239
                self.conditionExpr()


            self.state = 242
            self.match(BKITParser.COMMA)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 243
                self.updateExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_forDeclaration




    def forDeclaration(self):

        localctx = BKITParser.ForDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BKITParser.Identifier)
            self.state = 247
            self.match(BKITParser.ASSIGN)
            self.state = 248
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_conditionExpr




    def conditionExpr(self):

        localctx = BKITParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_updateExpr




    def updateExpr(self):

        localctx = BKITParser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statementList(self):
            return self.getTypedRuleContext(BKITParser.StatementListContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_whileStatement




    def whileStatement(self):

        localctx = BKITParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKITParser.WHILE)
            self.state = 255
            self.expression()
            self.state = 256
            self.match(BKITParser.DO)
            self.state = 257
            self.statementList()
            self.state = 258
            self.match(BKITParser.ENDWHILE)
            self.state = 259
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statementList(self):
            return self.getTypedRuleContext(BKITParser.StatementListContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_doWhileStatement




    def doWhileStatement(self):

        localctx = BKITParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(BKITParser.DO)
            self.state = 262
            self.statementList()
            self.state = 263
            self.match(BKITParser.WHILE)
            self.state = 264
            self.expression()
            self.state = 265
            self.match(BKITParser.ENDDO)
            self.state = 266
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def breakStatement(self):
            return self.getTypedRuleContext(BKITParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(BKITParser.ContinueStatementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_jumpStatement




    def jumpStatement(self):

        localctx = BKITParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_jumpStatement)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.breakStatement()
                pass
            elif token in [BKITParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.continueStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_breakStatement




    def breakStatement(self):

        localctx = BKITParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BKITParser.BREAK)
            self.state = 273
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continueStatement




    def continueStatement(self):

        localctx = BKITParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKITParser.CONTINUE)
            self.state = 276
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(BKITParser.FunctionCallContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_callStatement




    def callStatement(self):

        localctx = BKITParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.functionCall()
            self.state = 279
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def argumentList(self):
            return self.getTypedRuleContext(BKITParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_functionCall




    def functionCall(self):

        localctx = BKITParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKITParser.Identifier)
            self.state = 282
            self.match(BKITParser.LB)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 283
                self.argumentList(0)


            self.state = 286
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(BKITParser.ArgumentListContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_argumentList



    def argumentList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ArgumentListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_argumentList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.ArgumentListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argumentList)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 292
                    self.match(BKITParser.COMMA)
                    self.state = 293
                    self.expression() 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_returnStatement




    def returnStatement(self):

        localctx = BKITParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.RETURN)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 300
                self.expression()


            self.state = 303
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LogicalOrAndExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.LogicalOrAndExpressionContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(BKITParser.RelationalOperatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.logicalOrAndExpression(0)
                self.state = 306
                self.relationalOperator()
                self.state = 307
                self.logicalOrAndExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.logicalOrAndExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def NE(self):
            return self.getToken(BKITParser.NE, 0)

        def NEF(self):
            return self.getToken(BKITParser.NEF, 0)

        def LE(self):
            return self.getToken(BKITParser.LE, 0)

        def LEF(self):
            return self.getToken(BKITParser.LEF, 0)

        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def LTF(self):
            return self.getToken(BKITParser.LTF, 0)

        def GE(self):
            return self.getToken(BKITParser.GE, 0)

        def GEF(self):
            return self.getToken(BKITParser.GEF, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def GTF(self):
            return self.getToken(BKITParser.GTF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relationalOperator




    def relationalOperator(self):

        localctx = BKITParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ) | (1 << BKITParser.LE) | (1 << BKITParser.GTF) | (1 << BKITParser.NE) | (1 << BKITParser.GE) | (1 << BKITParser.LEF) | (1 << BKITParser.LT) | (1 << BKITParser.NEF) | (1 << BKITParser.GEF) | (1 << BKITParser.GT) | (1 << BKITParser.LTF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrAndExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(BKITParser.AdditiveExpressionContext,0)


        def logicalOrAndExpression(self):
            return self.getTypedRuleContext(BKITParser.LogicalOrAndExpressionContext,0)


        def logicalOrAndOperator(self):
            return self.getTypedRuleContext(BKITParser.LogicalOrAndOperatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_logicalOrAndExpression



    def logicalOrAndExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.LogicalOrAndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_logicalOrAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.LogicalOrAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrAndExpression)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    self.logicalOrAndOperator()
                    self.state = 319
                    self.additiveExpression(0) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalOrAndOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_logicalOrAndOperator




    def logicalOrAndOperator(self):

        localctx = BKITParser.LogicalOrAndOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_logicalOrAndOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            _la = self._input.LA(1)
            if not(_la==BKITParser.OR or _la==BKITParser.AND):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(BKITParser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(BKITParser.AdditiveExpressionContext,0)


        def additiveOperator(self):
            return self.getTypedRuleContext(BKITParser.AdditiveOperatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_additiveExpression



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    self.additiveOperator()
                    self.state = 333
                    self.multiplicativeExpression(0) 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADDF(self):
            return self.getToken(BKITParser.ADDF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_additiveOperator




    def additiveOperator(self):

        localctx = BKITParser.AdditiveOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_additiveOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.ADDF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalNotExpression(self):
            return self.getTypedRuleContext(BKITParser.LogicalNotExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(BKITParser.MultiplicativeExpressionContext,0)


        def multiplicativeOperator(self):
            return self.getTypedRuleContext(BKITParser.MultiplicativeOperatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_multiplicativeExpression



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.logicalNotExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 345
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 346
                    self.multiplicativeOperator()
                    self.state = 347
                    self.logicalNotExpression() 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MULF(self):
            return self.getToken(BKITParser.MULF, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIVF(self):
            return self.getToken(BKITParser.DIVF, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplicativeOperator




    def multiplicativeOperator(self):

        localctx = BKITParser.MultiplicativeOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_multiplicativeOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.MOD) | (1 << BKITParser.DIV) | (1 << BKITParser.DIVF) | (1 << BKITParser.MULF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalNotExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def logicalNotExpression(self):
            return self.getTypedRuleContext(BKITParser.LogicalNotExpressionContext,0)


        def signExpression(self):
            return self.getTypedRuleContext(BKITParser.SignExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_logicalNotExpression




    def logicalNotExpression(self):

        localctx = BKITParser.LogicalNotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_logicalNotExpression)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(BKITParser.NOT)
                self.state = 357
                self.logicalNotExpression()
                pass
            elif token in [BKITParser.Identifier, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBF, BKITParser.LB, BKITParser.LP, BKITParser.IntegerConstant, BKITParser.FloatingConstant, BKITParser.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.signExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signOperator(self):
            return self.getTypedRuleContext(BKITParser.SignOperatorContext,0)


        def signExpression(self):
            return self.getTypedRuleContext(BKITParser.SignExpressionContext,0)


        def indexExpression(self):
            return self.getTypedRuleContext(BKITParser.IndexExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_signExpression




    def signExpression(self):

        localctx = BKITParser.SignExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_signExpression)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.signOperator()
                self.state = 362
                self.signExpression()
                pass
            elif token in [BKITParser.Identifier, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.LP, BKITParser.IntegerConstant, BKITParser.FloatingConstant, BKITParser.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.indexExpression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_signOperator




    def signOperator(self):

        localctx = BKITParser.SignOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_signOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not(_la==BKITParser.SUB or _la==BKITParser.SUBF):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcExpression(self):
            return self.getTypedRuleContext(BKITParser.FuncExpressionContext,0)


        def indexExpression(self):
            return self.getTypedRuleContext(BKITParser.IndexExpressionContext,0)


        def indexOperator(self):
            return self.getTypedRuleContext(BKITParser.IndexOperatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_indexExpression



    def indexExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.IndexExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_indexExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.funcExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.IndexExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexExpression)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    self.indexOperator() 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IndexOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_indexOperator




    def indexOperator(self):

        localctx = BKITParser.IndexOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_indexOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(BKITParser.LSB)
            self.state = 380
            self.expression()
            self.state = 381
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(BKITParser.PrimaryExpressionContext,0)


        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_funcExpression




    def funcExpression(self):

        localctx = BKITParser.FuncExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_funcExpression)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.primaryExpression()
                self.state = 384
                self.match(BKITParser.LSB)
                self.state = 385
                self.expression()
                self.state = 386
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.primaryExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(BKITParser.FunctionCallContext,0)


        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primaryExpression




    def primaryExpression(self):

        localctx = BKITParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_primaryExpression)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(BKITParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self.match(BKITParser.LB)
                self.state = 395
                self.expression()
                self.state = 396
                self.match(BKITParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerConstant(self):
            return self.getToken(BKITParser.IntegerConstant, 0)

        def FloatingConstant(self):
            return self.getToken(BKITParser.FloatingConstant, 0)

        def String(self):
            return self.getToken(BKITParser.String, 0)

        def boolean(self):
            return self.getTypedRuleContext(BKITParser.BooleanContext,0)


        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literals




    def literals(self):

        localctx = BKITParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literals)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IntegerConstant]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(BKITParser.IntegerConstant)
                pass
            elif token in [BKITParser.FloatingConstant]:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(BKITParser.FloatingConstant)
                pass
            elif token in [BKITParser.String]:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.match(BKITParser.String)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.boolean()
                pass
            elif token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 404
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean




    def boolean(self):

        localctx = BKITParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def literals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralsContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralsContext,i)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(BKITParser.LP)
            self.state = 410
            self.literals()
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 411
                self.match(BKITParser.COMMA)
                self.state = 412
                self.literals()
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignmentOperator




    def assignmentOperator(self):

        localctx = BKITParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assignmentOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(BKITParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.argumentList_sempred
        self._predicates[30] = self.logicalOrAndExpression_sempred
        self._predicates[32] = self.additiveExpression_sempred
        self._predicates[34] = self.multiplicativeExpression_sempred
        self._predicates[39] = self.indexExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def argumentList_sempred(self, localctx:ArgumentListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def logicalOrAndExpression_sempred(self, localctx:LogicalOrAndExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def indexExpression_sempred(self, localctx:IndexExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




