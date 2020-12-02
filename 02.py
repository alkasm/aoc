from sly import Lexer, Parser
from aocd import get_data
from collections import namedtuple


class PasswordLexer(Lexer):
    tokens = {NUMBER, CHAR}
    literals = {"-", ":"}
    ignore = " "

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # number has precedence
    CHAR = r"[a-zA-Z0-9_]"

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


ParseResult = namedtuple("ParseResult", "min, max, char, string")


class PasswordParser(Parser):
    """
    statement   : NUMBER - NUMBER CHAR : string
    string      : CHAR string
                | CHAR
    """

    tokens = PasswordLexer.tokens

    @_(r'NUMBER "-" NUMBER CHAR ":" string')
    def statement(self, p):
        return ParseResult(p.NUMBER0, p.NUMBER1, p.CHAR, p.string)

    @_("CHAR")
    def string(self, p):
        return p.CHAR

    @_("CHAR string")
    def string(self, p):
        return p.CHAR + p.string


def parse_and_validate(lines, validator):
    lexer = PasswordLexer()
    parser = PasswordParser()
    n_valid = 0
    for line in lines:
        n_valid += validator(parser.parse(lexer.tokenize(line)))
    return n_valid


def validate_one(p):
    return p.min <= p.string.count(p.char) <= p.max


def validate_two(p):
    return (p.string[p.min - 1] == p.char) ^ (p.string[p.max - 1] == p.char)


lines = get_data(day=2).splitlines()
print("Part one:", parse_and_validate(lines, validate_one))
print("Part two:", parse_and_validate(lines, validate_two))
