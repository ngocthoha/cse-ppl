# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\u01ac\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\7\2d\n\2\f\2\16\2g\13\2\3")
        buf.write("\2\7\2j\n\2\f\2\16\2m\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\7\4y\n\4\f\4\16\4|\13\4\3\5\3\5\3\5\3\5\7")
        buf.write("\5\u0082\n\5\f\5\16\5\u0085\13\5\3\5\3\5\5\5\u0089\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0091\n\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\7\7\u0098\n\7\f\7\16\7\u009b\13\7\3\b\3\b\3\b\3\b")
        buf.write("\7\b\u00a1\n\b\f\b\16\b\u00a4\13\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\7\n\u00ad\n\n\f\n\16\n\u00b0\13\n\3\n\7\n\u00b3")
        buf.write("\n\n\f\n\16\n\u00b6\13\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00be\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00c7")
        buf.write("\n\r\3\r\7\r\u00ca\n\r\f\r\16\r\u00cd\13\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u00d4\n\16\f\16\16\16\u00d7\13\16\3")
        buf.write("\16\3\16\5\16\u00db\n\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\5\20\u00e8\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\5\22")
        buf.write("\u00f6\n\22\3\22\3\22\5\22\u00fa\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\5\30")
        buf.write("\u0114\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\5\34\u0122\n\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\7\35\u012c\n\35\f\35\16\35\u012f")
        buf.write("\13\35\3\36\3\36\5\36\u0133\n\36\3\36\3\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u013c\n\37\3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3!\7!\u0147\n!\f!\16!\u014a\13!\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\7#\u0155\n#\f#\16#\u0158\13#\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\7%\u0163\n%\f%\16%\u0166\13%\3&\3&\3\'\3\'")
        buf.write("\3\'\5\'\u016d\n\'\3(\3(\3(\3(\5(\u0173\n(\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\7*\u017c\n*\f*\16*\u017f\13*\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\5,\u018b\n,\3-\3-\3-\3-\3-\3-\3-\5-\u0194")
        buf.write("\n-\3.\3.\3.\3.\3.\5.\u019b\n.\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\7\60\u01a3\n\60\f\60\16\60\u01a6\13\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\2\78@DHR\62\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2")
        buf.write("\b\3\2%/\3\2#$\5\2\31\32\36\36  \5\2\33\35\37\37!!\4\2")
        buf.write("\32\32\36\36\4\2\23\23\30\30\2\u01a6\2e\3\2\2\2\4p\3\2")
        buf.write("\2\2\6u\3\2\2\2\b}\3\2\2\2\n\u008a\3\2\2\2\f\u0094\3\2")
        buf.write("\2\2\16\u009c\3\2\2\2\20\u00a5\3\2\2\2\22\u00ae\3\2\2")
        buf.write("\2\24\u00bd\3\2\2\2\26\u00bf\3\2\2\2\30\u00c6\3\2\2\2")
        buf.write("\32\u00ce\3\2\2\2\34\u00df\3\2\2\2\36\u00e7\3\2\2\2 \u00e9")
        buf.write("\3\2\2\2\"\u00f2\3\2\2\2$\u00fb\3\2\2\2&\u00ff\3\2\2\2")
        buf.write("(\u0101\3\2\2\2*\u0103\3\2\2\2,\u010a\3\2\2\2.\u0113\3")
        buf.write("\2\2\2\60\u0115\3\2\2\2\62\u0118\3\2\2\2\64\u011b\3\2")
        buf.write("\2\2\66\u011e\3\2\2\28\u0125\3\2\2\2:\u0130\3\2\2\2<\u013b")
        buf.write("\3\2\2\2>\u013d\3\2\2\2@\u013f\3\2\2\2B\u014b\3\2\2\2")
        buf.write("D\u014d\3\2\2\2F\u0159\3\2\2\2H\u015b\3\2\2\2J\u0167\3")
        buf.write("\2\2\2L\u016c\3\2\2\2N\u0172\3\2\2\2P\u0174\3\2\2\2R\u0176")
        buf.write("\3\2\2\2T\u0180\3\2\2\2V\u018a\3\2\2\2X\u0193\3\2\2\2")
        buf.write("Z\u019a\3\2\2\2\\\u019c\3\2\2\2^\u019e\3\2\2\2`\u01a9")
        buf.write("\3\2\2\2bd\5\4\3\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2")
        buf.write("\2\2fk\3\2\2\2ge\3\2\2\2hj\5\n\6\2ih\3\2\2\2jm\3\2\2\2")
        buf.write("ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2no\7\2\2\3o\3")
        buf.write("\3\2\2\2pq\7\b\2\2qr\7\64\2\2rs\5\6\4\2st\78\2\2t\5\3")
        buf.write("\2\2\2uz\5\b\5\2vw\7\67\2\2wy\5\b\5\2xv\3\2\2\2y|\3\2")
        buf.write("\2\2zx\3\2\2\2z{\3\2\2\2{\7\3\2\2\2|z\3\2\2\2}\u0083\7")
        buf.write("\3\2\2~\177\7\62\2\2\177\u0080\7<\2\2\u0080\u0082\7\63")
        buf.write("\2\2\u0081~\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3")
        buf.write("\2\2\2\u0083\u0084\3\2\2\2\u0084\u0088\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0086\u0087\7;\2\2\u0087\u0089\5Z.\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\t\3\2\2\2\u008a\u008b")
        buf.write("\7\26\2\2\u008b\u008c\7\64\2\2\u008c\u0090\7\3\2\2\u008d")
        buf.write("\u008e\7\r\2\2\u008e\u008f\7\64\2\2\u008f\u0091\5\f\7")
        buf.write("\2\u0090\u008d\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\5\20\t\2\u0093\13\3\2\2\2\u0094\u0099")
        buf.write("\5\16\b\2\u0095\u0096\7\67\2\2\u0096\u0098\5\16\b\2\u0097")
        buf.write("\u0095\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\r\3\2\2\2\u009b\u0099\3\2\2")
        buf.write("\2\u009c\u00a2\7\3\2\2\u009d\u009e\7\62\2\2\u009e\u009f")
        buf.write("\7<\2\2\u009f\u00a1\7\63\2\2\u00a0\u009d\3\2\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\17\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\7\4")
        buf.write("\2\2\u00a6\u00a7\7\64\2\2\u00a7\u00a8\5\22\n\2\u00a8\u00a9")
        buf.write("\7\20\2\2\u00a9\u00aa\7\65\2\2\u00aa\21\3\2\2\2\u00ab")
        buf.write("\u00ad\5\4\3\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b4\3")
        buf.write("\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b3\5\24\13\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\23\3\2\2\2\u00b6\u00b4\3\2")
        buf.write("\2\2\u00b7\u00be\5\26\f\2\u00b8\u00be\5\36\20\2\u00b9")
        buf.write("\u00be\5.\30\2\u00ba\u00be\5\64\33\2\u00bb\u00be\5:\36")
        buf.write("\2\u00bc\u00be\5\32\16\2\u00bd\u00b7\3\2\2\2\u00bd\u00b8")
        buf.write("\3\2\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\25\3\2\2\2\u00bf")
        buf.write("\u00c0\5\30\r\2\u00c0\u00c1\7;\2\2\u00c1\u00c2\5<\37\2")
        buf.write("\u00c2\u00c3\78\2\2\u00c3\27\3\2\2\2\u00c4\u00c7\7\3\2")
        buf.write("\2\u00c5\u00c7\5\66\34\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00cb\3\2\2\2\u00c8\u00ca\5T+\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\31\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\u00cf\7\7\2\2\u00cf\u00d0\5<\37\2\u00d0\u00d1\7\27\2")
        buf.write("\2\u00d1\u00d5\5\22\n\2\u00d2\u00d4\5\34\17\2\u00d3\u00d2")
        buf.write("\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00da\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8\u00d9\7\5\2\2\u00d9\u00db\5\22\n\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00dd\7\25\2\2\u00dd\u00de\7\65\2\2\u00de\33\3\2\2\2")
        buf.write("\u00df\u00e0\7\13\2\2\u00e0\u00e1\5<\37\2\u00e1\u00e2")
        buf.write("\7\27\2\2\u00e2\u00e3\5\22\n\2\u00e3\35\3\2\2\2\u00e4")
        buf.write("\u00e8\5 \21\2\u00e5\u00e8\5*\26\2\u00e6\u00e8\5,\27\2")
        buf.write("\u00e7\u00e4\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3")
        buf.write("\2\2\2\u00e8\37\3\2\2\2\u00e9\u00ea\7\21\2\2\u00ea\u00eb")
        buf.write("\7\60\2\2\u00eb\u00ec\5\"\22\2\u00ec\u00ed\7\61\2\2\u00ed")
        buf.write("\u00ee\7\24\2\2\u00ee\u00ef\5\22\n\2\u00ef\u00f0\7\6\2")
        buf.write("\2\u00f0\u00f1\7\65\2\2\u00f1!\3\2\2\2\u00f2\u00f3\5$")
        buf.write("\23\2\u00f3\u00f5\7\67\2\2\u00f4\u00f6\5&\24\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00f9\7\67\2\2\u00f8\u00fa\5(\25\2\u00f9\u00f8\3\2\2")
        buf.write("\2\u00f9\u00fa\3\2\2\2\u00fa#\3\2\2\2\u00fb\u00fc\7\3")
        buf.write("\2\2\u00fc\u00fd\7;\2\2\u00fd\u00fe\5<\37\2\u00fe%\3\2")
        buf.write("\2\2\u00ff\u0100\5<\37\2\u0100\'\3\2\2\2\u0101\u0102\5")
        buf.write("<\37\2\u0102)\3\2\2\2\u0103\u0104\7\16\2\2\u0104\u0105")
        buf.write("\5<\37\2\u0105\u0106\7\24\2\2\u0106\u0107\5\22\n\2\u0107")
        buf.write("\u0108\7\f\2\2\u0108\u0109\7\65\2\2\u0109+\3\2\2\2\u010a")
        buf.write("\u010b\7\24\2\2\u010b\u010c\5\22\n\2\u010c\u010d\7\16")
        buf.write("\2\2\u010d\u010e\5<\37\2\u010e\u010f\7\t\2\2\u010f\u0110")
        buf.write("\7\65\2\2\u0110-\3\2\2\2\u0111\u0114\5\60\31\2\u0112\u0114")
        buf.write("\5\62\32\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("/\3\2\2\2\u0115\u0116\7\n\2\2\u0116\u0117\78\2\2\u0117")
        buf.write("\61\3\2\2\2\u0118\u0119\7\17\2\2\u0119\u011a\78\2\2\u011a")
        buf.write("\63\3\2\2\2\u011b\u011c\5\66\34\2\u011c\u011d\78\2\2\u011d")
        buf.write("\65\3\2\2\2\u011e\u011f\7\3\2\2\u011f\u0121\7\60\2\2\u0120")
        buf.write("\u0122\58\35\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123\u0124\7\61\2\2\u0124\67\3\2")
        buf.write("\2\2\u0125\u0126\b\35\1\2\u0126\u0127\5<\37\2\u0127\u012d")
        buf.write("\3\2\2\2\u0128\u0129\f\4\2\2\u0129\u012a\7\67\2\2\u012a")
        buf.write("\u012c\5<\37\2\u012b\u0128\3\2\2\2\u012c\u012f\3\2\2\2")
        buf.write("\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e9\3\2\2")
        buf.write("\2\u012f\u012d\3\2\2\2\u0130\u0132\7\22\2\2\u0131\u0133")
        buf.write("\5<\37\2\u0132\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0135\78\2\2\u0135;\3\2\2\2\u0136")
        buf.write("\u0137\5@!\2\u0137\u0138\5> \2\u0138\u0139\5@!\2\u0139")
        buf.write("\u013c\3\2\2\2\u013a\u013c\5@!\2\u013b\u0136\3\2\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c=\3\2\2\2\u013d\u013e\t\2\2\2\u013e")
        buf.write("?\3\2\2\2\u013f\u0140\b!\1\2\u0140\u0141\5D#\2\u0141\u0148")
        buf.write("\3\2\2\2\u0142\u0143\f\4\2\2\u0143\u0144\5B\"\2\u0144")
        buf.write("\u0145\5D#\2\u0145\u0147\3\2\2\2\u0146\u0142\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149A\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\t\3\2")
        buf.write("\2\u014cC\3\2\2\2\u014d\u014e\b#\1\2\u014e\u014f\5H%\2")
        buf.write("\u014f\u0156\3\2\2\2\u0150\u0151\f\4\2\2\u0151\u0152\5")
        buf.write("F$\2\u0152\u0153\5H%\2\u0153\u0155\3\2\2\2\u0154\u0150")
        buf.write("\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157E\3\2\2\2\u0158\u0156\3\2\2\2\u0159")
        buf.write("\u015a\t\4\2\2\u015aG\3\2\2\2\u015b\u015c\b%\1\2\u015c")
        buf.write("\u015d\5L\'\2\u015d\u0164\3\2\2\2\u015e\u015f\f\4\2\2")
        buf.write("\u015f\u0160\5J&\2\u0160\u0161\5L\'\2\u0161\u0163\3\2")
        buf.write("\2\2\u0162\u015e\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165I\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0167\u0168\t\5\2\2\u0168K\3\2\2\2\u0169\u016a")
        buf.write("\7\"\2\2\u016a\u016d\5L\'\2\u016b\u016d\5N(\2\u016c\u0169")
        buf.write("\3\2\2\2\u016c\u016b\3\2\2\2\u016dM\3\2\2\2\u016e\u016f")
        buf.write("\5P)\2\u016f\u0170\5N(\2\u0170\u0173\3\2\2\2\u0171\u0173")
        buf.write("\5R*\2\u0172\u016e\3\2\2\2\u0172\u0171\3\2\2\2\u0173O")
        buf.write("\3\2\2\2\u0174\u0175\t\6\2\2\u0175Q\3\2\2\2\u0176\u0177")
        buf.write("\b*\1\2\u0177\u0178\5V,\2\u0178\u017d\3\2\2\2\u0179\u017a")
        buf.write("\f\4\2\2\u017a\u017c\5T+\2\u017b\u0179\3\2\2\2\u017c\u017f")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("S\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\7\62\2\2\u0181")
        buf.write("\u0182\5<\37\2\u0182\u0183\7\63\2\2\u0183U\3\2\2\2\u0184")
        buf.write("\u0185\5X-\2\u0185\u0186\7\62\2\2\u0186\u0187\5<\37\2")
        buf.write("\u0187\u0188\7\63\2\2\u0188\u018b\3\2\2\2\u0189\u018b")
        buf.write("\5X-\2\u018a\u0184\3\2\2\2\u018a\u0189\3\2\2\2\u018bW")
        buf.write("\3\2\2\2\u018c\u0194\7\3\2\2\u018d\u0194\5Z.\2\u018e\u0194")
        buf.write("\5\66\34\2\u018f\u0190\7\60\2\2\u0190\u0191\5<\37\2\u0191")
        buf.write("\u0192\7\61\2\2\u0192\u0194\3\2\2\2\u0193\u018c\3\2\2")
        buf.write("\2\u0193\u018d\3\2\2\2\u0193\u018e\3\2\2\2\u0193\u018f")
        buf.write("\3\2\2\2\u0194Y\3\2\2\2\u0195\u019b\7<\2\2\u0196\u019b")
        buf.write("\7=\2\2\u0197\u019b\7>\2\2\u0198\u019b\5\\/\2\u0199\u019b")
        buf.write("\5^\60\2\u019a\u0195\3\2\2\2\u019a\u0196\3\2\2\2\u019a")
        buf.write("\u0197\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019b[\3\2\2\2\u019c\u019d\t\7\2\2\u019d]\3\2\2\2\u019e")
        buf.write("\u019f\79\2\2\u019f\u01a4\5Z.\2\u01a0\u01a1\7\67\2\2\u01a1")
        buf.write("\u01a3\5Z.\2\u01a2\u01a0\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a7\u01a8\7:\2\2\u01a8_\3\2\2\2")
        buf.write("\u01a9\u01aa\7;\2\2\u01aaa\3\2\2\2#ekz\u0083\u0088\u0090")
        buf.write("\u0099\u00a2\u00ae\u00b4\u00bd\u00c6\u00cb\u00d5\u00da")
        buf.write("\u00e7\u00f5\u00f9\u0113\u0121\u012d\u0132\u013b\u0148")
        buf.write("\u0156\u0164\u016c\u0172\u017d\u018a\u0193\u019a\u01a4")
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
    RULE_elseIfStatement = 13
    RULE_iterationStatement = 14
    RULE_forStatement = 15
    RULE_forCondition = 16
    RULE_forDeclaration = 17
    RULE_conditionExpr = 18
    RULE_updateExpr = 19
    RULE_whileStatement = 20
    RULE_doWhileStatement = 21
    RULE_jumpStatement = 22
    RULE_breakStatement = 23
    RULE_continueStatement = 24
    RULE_callStatement = 25
    RULE_functionCall = 26
    RULE_argumentList = 27
    RULE_returnStatement = 28
    RULE_expression = 29
    RULE_relationalOperator = 30
    RULE_logicalOrAndExpression = 31
    RULE_logicalOrAndOperator = 32
    RULE_additiveExpression = 33
    RULE_additiveOperator = 34
    RULE_multiplicativeExpression = 35
    RULE_multiplicativeOperator = 36
    RULE_logicalNotExpression = 37
    RULE_signExpression = 38
    RULE_signOperator = 39
    RULE_indexExpression = 40
    RULE_indexOperator = 41
    RULE_funcExpression = 42
    RULE_primaryExpression = 43
    RULE_literals = 44
    RULE_boolean = 45
    RULE_array = 46
    RULE_assignmentOperator = 47

    ruleNames =  [ "program", "variableStatement", "varList", "varDeclaration", 
                   "funcDeclaration", "paraList", "parameters", "funcBody", 
                   "statementList", "statement", "assignmentStatement", 
                   "assignDeclaration", "ifStatement", "elseIfStatement", 
                   "iterationStatement", "forStatement", "forCondition", 
                   "forDeclaration", "conditionExpr", "updateExpr", "whileStatement", 
                   "doWhileStatement", "jumpStatement", "breakStatement", 
                   "continueStatement", "callStatement", "functionCall", 
                   "argumentList", "returnStatement", "expression", "relationalOperator", 
                   "logicalOrAndExpression", "logicalOrAndOperator", "additiveExpression", 
                   "additiveOperator", "multiplicativeExpression", "multiplicativeOperator", 
                   "logicalNotExpression", "signExpression", "signOperator", 
                   "indexExpression", "indexOperator", "funcExpression", 
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 96
                self.variableStatement()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 102
                self.funcDeclaration()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableStatement" ):
                return visitor.visitVariableStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableStatement(self):

        localctx = BKITParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BKITParser.VAR)
            self.state = 111
            self.match(BKITParser.COLON)
            self.state = 112
            self.varList()
            self.state = 113
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarList" ):
                return visitor.visitVarList(self)
            else:
                return visitor.visitChildren(self)




    def varList(self):

        localctx = BKITParser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.varDeclaration()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 116
                self.match(BKITParser.COMMA)
                self.state = 117
                self.varDeclaration()
                self.state = 122
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = BKITParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BKITParser.Identifier)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 124
                self.match(BKITParser.LSB)
                self.state = 125
                self.match(BKITParser.IntegerConstant)
                self.state = 126
                self.match(BKITParser.RSB)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 132
                self.match(BKITParser.ASSIGN)
                self.state = 133
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclaration" ):
                return visitor.visitFuncDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclaration(self):

        localctx = BKITParser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BKITParser.FUNCTION)
            self.state = 137
            self.match(BKITParser.COLON)
            self.state = 138
            self.match(BKITParser.Identifier)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 139
                self.match(BKITParser.PARAMETER)
                self.state = 140
                self.match(BKITParser.COLON)
                self.state = 141
                self.paraList()


            self.state = 144
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaList" ):
                return visitor.visitParaList(self)
            else:
                return visitor.visitChildren(self)




    def paraList(self):

        localctx = BKITParser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.parameters()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 147
                self.match(BKITParser.COMMA)
                self.state = 148
                self.parameters()
                self.state = 153
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = BKITParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKITParser.Identifier)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 155
                self.match(BKITParser.LSB)
                self.state = 156
                self.match(BKITParser.IntegerConstant)
                self.state = 157
                self.match(BKITParser.RSB)
                self.state = 162
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncBody" ):
                return visitor.visitFuncBody(self)
            else:
                return visitor.visitChildren(self)




    def funcBody(self):

        localctx = BKITParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(BKITParser.BODY)
            self.state = 164
            self.match(BKITParser.COLON)
            self.state = 165
            self.statementList()
            self.state = 166
            self.match(BKITParser.ENDBODY)
            self.state = 167
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = BKITParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 169
                self.variableStatement()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self.statement() 
                self.state = 180
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.iterationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.jumpStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.callStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = BKITParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.assignDeclaration()
            self.state = 190
            self.match(BKITParser.ASSIGN)
            self.state = 191
            self.expression()
            self.state = 192
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignDeclaration" ):
                return visitor.visitAssignDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def assignDeclaration(self):

        localctx = BKITParser.AssignDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 194
                self.match(BKITParser.Identifier)
                pass

            elif la_ == 2:
                self.state = 195
                self.functionCall()
                pass


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 198
                self.indexOperator()
                self.state = 203
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

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementListContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementListContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def elseIfStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ElseIfStatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.ElseIfStatementContext,i)


        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = BKITParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BKITParser.IF)
            self.state = 205
            self.expression()
            self.state = 206
            self.match(BKITParser.THEN)
            self.state = 207
            self.statementList()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 208
                self.elseIfStatement()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 214
                self.match(BKITParser.ELSE)
                self.state = 215
                self.statementList()


            self.state = 218
            self.match(BKITParser.ENDIF)
            self.state = 219
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statementList(self):
            return self.getTypedRuleContext(BKITParser.StatementListContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseIfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStatement" ):
                return visitor.visitElseIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStatement(self):

        localctx = BKITParser.ElseIfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(BKITParser.ELSEIF)
            self.state = 222
            self.expression()
            self.state = 223
            self.match(BKITParser.THEN)
            self.state = 224
            self.statementList()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterationStatement" ):
                return visitor.visitIterationStatement(self)
            else:
                return visitor.visitChildren(self)




    def iterationStatement(self):

        localctx = BKITParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_iterationStatement)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.forStatement()
                pass
            elif token in [BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.whileStatement()
                pass
            elif token in [BKITParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = BKITParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BKITParser.FOR)
            self.state = 232
            self.match(BKITParser.LB)
            self.state = 233
            self.forCondition()
            self.state = 234
            self.match(BKITParser.RB)
            self.state = 235
            self.match(BKITParser.DO)
            self.state = 236
            self.statementList()
            self.state = 237
            self.match(BKITParser.ENDFOR)
            self.state = 238
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = BKITParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.forDeclaration()
            self.state = 241
            self.match(BKITParser.COMMA)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 242
                self.conditionExpr()


            self.state = 245
            self.match(BKITParser.COMMA)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 246
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForDeclaration" ):
                return visitor.visitForDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def forDeclaration(self):

        localctx = BKITParser.ForDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(BKITParser.Identifier)
            self.state = 250
            self.match(BKITParser.ASSIGN)
            self.state = 251
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpr" ):
                return visitor.visitConditionExpr(self)
            else:
                return visitor.visitChildren(self)




    def conditionExpr(self):

        localctx = BKITParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateExpr" ):
                return visitor.visitUpdateExpr(self)
            else:
                return visitor.visitChildren(self)




    def updateExpr(self):

        localctx = BKITParser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = BKITParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(BKITParser.WHILE)
            self.state = 258
            self.expression()
            self.state = 259
            self.match(BKITParser.DO)
            self.state = 260
            self.statementList()
            self.state = 261
            self.match(BKITParser.ENDWHILE)
            self.state = 262
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def doWhileStatement(self):

        localctx = BKITParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(BKITParser.DO)
            self.state = 265
            self.statementList()
            self.state = 266
            self.match(BKITParser.WHILE)
            self.state = 267
            self.expression()
            self.state = 268
            self.match(BKITParser.ENDDO)
            self.state = 269
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpStatement" ):
                return visitor.visitJumpStatement(self)
            else:
                return visitor.visitChildren(self)




    def jumpStatement(self):

        localctx = BKITParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_jumpStatement)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.breakStatement()
                pass
            elif token in [BKITParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = BKITParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKITParser.BREAK)
            self.state = 276
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = BKITParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BKITParser.CONTINUE)
            self.state = 279
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = BKITParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.functionCall()
            self.state = 282
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = BKITParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.Identifier)
            self.state = 285
            self.match(BKITParser.LB)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 286
                self.argumentList(0)


            self.state = 289
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)



    def argumentList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ArgumentListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_argumentList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.ArgumentListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argumentList)
                    self.state = 294
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 295
                    self.match(BKITParser.COMMA)
                    self.state = 296
                    self.expression() 
                self.state = 301
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = BKITParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKITParser.RETURN)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Identifier) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.IntegerConstant) | (1 << BKITParser.FloatingConstant) | (1 << BKITParser.String))) != 0):
                self.state = 303
                self.expression()


            self.state = 306
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.logicalOrAndExpression(0)
                self.state = 309
                self.relationalOperator()
                self.state = 310
                self.logicalOrAndExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOperator" ):
                return visitor.visitRelationalOperator(self)
            else:
                return visitor.visitChildren(self)




    def relationalOperator(self):

        localctx = BKITParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrAndExpression" ):
                return visitor.visitLogicalOrAndExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalOrAndExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.LogicalOrAndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_logicalOrAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.LogicalOrAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrAndExpression)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    self.logicalOrAndOperator()
                    self.state = 322
                    self.additiveExpression(0) 
                self.state = 328
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrAndOperator" ):
                return visitor.visitLogicalOrAndOperator(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrAndOperator(self):

        localctx = BKITParser.LogicalOrAndOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_logicalOrAndOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 334
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 335
                    self.additiveOperator()
                    self.state = 336
                    self.multiplicativeExpression(0) 
                self.state = 342
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveOperator" ):
                return visitor.visitAdditiveOperator(self)
            else:
                return visitor.visitChildren(self)




    def additiveOperator(self):

        localctx = BKITParser.AdditiveOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_additiveOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.logicalNotExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    self.multiplicativeOperator()
                    self.state = 350
                    self.logicalNotExpression() 
                self.state = 356
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeOperator" ):
                return visitor.visitMultiplicativeOperator(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeOperator(self):

        localctx = BKITParser.MultiplicativeOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_multiplicativeOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNotExpression" ):
                return visitor.visitLogicalNotExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalNotExpression(self):

        localctx = BKITParser.LogicalNotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_logicalNotExpression)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(BKITParser.NOT)
                self.state = 360
                self.logicalNotExpression()
                pass
            elif token in [BKITParser.Identifier, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBF, BKITParser.LB, BKITParser.LP, BKITParser.IntegerConstant, BKITParser.FloatingConstant, BKITParser.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignExpression" ):
                return visitor.visitSignExpression(self)
            else:
                return visitor.visitChildren(self)




    def signExpression(self):

        localctx = BKITParser.SignExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_signExpression)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.signOperator()
                self.state = 365
                self.signExpression()
                pass
            elif token in [BKITParser.Identifier, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.LP, BKITParser.IntegerConstant, BKITParser.FloatingConstant, BKITParser.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignOperator" ):
                return visitor.visitSignOperator(self)
            else:
                return visitor.visitChildren(self)




    def signOperator(self):

        localctx = BKITParser.SignOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_signOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpression" ):
                return visitor.visitIndexExpression(self)
            else:
                return visitor.visitChildren(self)



    def indexExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.IndexExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_indexExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.funcExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.IndexExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexExpression)
                    self.state = 375
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 376
                    self.indexOperator() 
                self.state = 381
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOperator" ):
                return visitor.visitIndexOperator(self)
            else:
                return visitor.visitChildren(self)




    def indexOperator(self):

        localctx = BKITParser.IndexOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_indexOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(BKITParser.LSB)
            self.state = 383
            self.expression()
            self.state = 384
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncExpression" ):
                return visitor.visitFuncExpression(self)
            else:
                return visitor.visitChildren(self)




    def funcExpression(self):

        localctx = BKITParser.FuncExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_funcExpression)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.primaryExpression()
                self.state = 387
                self.match(BKITParser.LSB)
                self.state = 388
                self.expression()
                self.state = 389
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = BKITParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_primaryExpression)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(BKITParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.match(BKITParser.LB)
                self.state = 398
                self.expression()
                self.state = 399
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKITParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literals)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IntegerConstant]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(BKITParser.IntegerConstant)
                pass
            elif token in [BKITParser.FloatingConstant]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(BKITParser.FloatingConstant)
                pass
            elif token in [BKITParser.String]:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.match(BKITParser.String)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.boolean()
                pass
            elif token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = BKITParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(BKITParser.LP)
            self.state = 413
            self.literals()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 414
                self.match(BKITParser.COMMA)
                self.state = 415
                self.literals()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 421
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = BKITParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assignmentOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
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
        self._predicates[27] = self.argumentList_sempred
        self._predicates[31] = self.logicalOrAndExpression_sempred
        self._predicates[33] = self.additiveExpression_sempred
        self._predicates[35] = self.multiplicativeExpression_sempred
        self._predicates[40] = self.indexExpression_sempred
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
         




