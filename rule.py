import regex


class Rule:
    def __init__(self, rule_title: str, in_regex: str, out_repl: str) -> None:
        self.rule_title = rule_title
        self.in_regex = regex.compile(in_regex)
        self.out_repl = out_repl

    def process(self, text: str, verbose: bool = False):
        result = self.in_regex.sub(self.out_repl, text)

        if verbose:
            print(f"RULE TITLE : {self.rule_title}")
            print(f"IN TEXT    : {text}")
            print(f"IN PATTERN : {self.in_regex.pattern}")
            print(f"OUT REPLACE: {self.out_repl}")
            print(f"OUT TEXT   : {result}")
            print()

        return result
