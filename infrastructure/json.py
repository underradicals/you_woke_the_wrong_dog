from pathlib import Path


def process(char: str, state: dict):
    if char == "{":
        state["level"] += 1
        return f"{{\n{'\t'*state['level']}"

    if char == ",":
        return f',\n{'\t'*state['level']}'

    if char == "}":
        state["level"] -= 1
        return f"\n{'\t'*state['level']}}}"

    if char == "[":
        state["level"] += 1
        return f"[\n{'\t'*state['level']}"

    if char == "]":
        state["level"] -= 1
        return f"\n{'\t'*state['level']}]"

    return char


def write_manifest_pretty(input_file: str | Path, output_file: str | Path):

    state = {'level': 0}

    with open(output_file, "w", encoding="utf-8") as file2:
        with open(input_file, "r") as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                file2.write(process(char, state))
