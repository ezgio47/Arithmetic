from dataclasses import dataclass
from typing import List, Union
import re

# Token definieren
@dataclass
class Token:
    type: str
    value: str

class Lexer:
    def __init__(self, tet: str):
        self.text = text
        self.pos = 0

    def tokenize(self) -> List[Token]:
        tokens = []
        while self.pos < len(self.text):
            current_char = self.text[self.pos]

            # Whitespace ignorieren
            if current_char.isdigit():
                num = ""
                while self.pos < len(self.text) and self.text[self.pos].isdigit():
                    num += self.text[self.pos]
                    self.pos += 1
                tokens.append(Token("INT", num))
                continue

            # Operator und Klammern
            if current_char in "+-*/()":
                token_type = {
                    '+': 'PLUS',
                    '-': 'MINUS',
                    '*': 'MUL',
                    '/': 'DIV',
                    '(': 'LPAREN',
                    ')': 'RPAREN'
                }[current_char]
                tokens.append(Token(token_type, current_char))
                self.pos += 1
                continue

            raise ValueErro(f"Ungültiges Zeichen: {current_char}")

        return tokens

class Parser: 
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def current_token(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type: str):
        if self.current_token().type == token_type:
            self.pos += 1
        else:
            raise ValueError(f"Erwarteter Token-Typ: {token_type}, Gefunden: {self.current_token().type}")

    def factor(self) -> int:
        token = self.current_token()
        if token.type == "INT":
            self.eat("INT")
            return int(token.value)
        elif token.type == "LPAREN":
            self.eat("LPAREN")
            result = self.expr()
            self.eat("RPAREN")
            return result
        raise ValueError(f"Unerwarteter Token: {token}")

    def term(self) -> int:
        result = self.factor()

        while self.pos < len(self.tokens) and self.current_token().type in ["MUL", "DIV"]:
            token = self.current_token()
            if token.type == "MUL":
                self.eat("MUL")
                result *= self.factor()
            elif token.type == "DIV":
                self.eat("DIV")
                result /= self.factor()
            
        return result

    def expr(self) -> int:
        result = self.term()

        while self.pos < len(self.tokens) and self.current_token().type in ["PLUS", "MINUS"]:
            token = self.current_token()
            if token.type == "PLUS":
                self.eat("PLUS")
                result += self.term()
            elif token.type == "MINUS":
                self.eat("MINUS")
                result -= self.term()

        return result

def evaluate(expression: str) -> int:
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.expr()













