from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List


class AST(ABC):
    pass


class Type(AST):
    pass


@dataclass
class VarDecl(AST):
    variable: Id
    varType: Type


@dataclass
class Program(AST):
    decls: List[VarDecl]


@dataclass
class Id(AST):
    name: str


class IntType(Type):
    pass


class FloatType(Type):
    pass
