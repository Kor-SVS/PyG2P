from typing import List, Union

from rule import Rule
from util import is_empty_string


class G2P:
    def __init__(self, rulebook_filepath: Union[str, None] = None) -> None:
        self.rulebook_filepath = rulebook_filepath
        self.load_rulebook(self.rulebook_filepath)

    def load_rulebook(self, rulebook_filepath: Union[str, None] = None):
        if is_empty_string(rulebook_filepath):
            self.rules = []
            return

        try:
            with open(rulebook_filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            rules: List[Rule] = []
            for line in lines:
                line: str = line.strip()

                line = line.split("#")[0]  # comment filter

                if is_empty_string(line):
                    continue

                tokens = line.split("|||")

                assert len(tokens) == 3, f"len(tokens) == 3, ({len(tokens)=})"

                rule_title = tokens[0].strip()
                in_regex = tokens[1].strip()
                out_repl = tokens[2].strip()

                assert len(rule_title) > 0, f"len(rule_title) > 0, ({len(rule_title)=})"
                assert len(in_regex) > 0, f"len(in_regex) > 0, ({len(in_regex)=})"
                assert len(out_repl) > 0, f"len(out_repl) > 0, ({len(out_repl)=})"

                rule = Rule(rule_title, in_regex, out_repl)
                rules.append(rule)

            self.rules = rules
        except Exception as ex:
            print(f"Rulebook load error: {ex=}")
            self.rules = []

    def __call__(self, text: str, verbose: bool = False):
        for rule in self.rules:
            text = rule.process(text, verbose)

        print(f"RESULT: {text}")
