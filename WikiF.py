def interpret(code: str) -> None:
    instructions = {
        "</code>": "<",
        "</nowiki>": ">",
        "{{WIP}}": ",",
        "}}": "+",
        "{| class=\"wikitable\"": "-",
        "*": ".",
        "===": "[",
        "<s>": "]",
    }

    prg = code

    for k, v in reversed(sorted(list(instructions.items()))): # Make sure that {{WIP}} does not turn into {{WIP+ and then try to be replaced
        prg = prg.replace(k, v)

    array = [0]
    negarray = [0]

    pointerLocation = 0

    i = 0
    c = 0

    while i < len(prg):
        if prg[i] == "<":
            pointerLocation -= 1

            if pointerLocation < 0 and len(negarray) <= (abs(pointerLocation) - 1):
                negarray.append(0)
        elif prg[i] == ">":
            pointerLocation += 1

            if pointerLocation >= 0 and len(array) <= abs(pointerLocation):
                array.append(0)
        elif prg[i] == "+":
            if pointerLocation < 0:
                negarray[abs(pointerLocation) - 1] += 1
                negarray[abs(pointerLocation) - 1] %= 1114112
            else:
                array[pointerLocation] += 1
                array[pointerLocation] %= 1114112
        elif prg[i] == "-":
            if pointerLocation < 0:
                negarray[abs(pointerLocation) - 1] -= 1
                negarray[abs(pointerLocation) - 1] %= 1114112
            else:
                array[pointerLocation] -= 1
                array[pointerLocation] %= 1114112
        elif prg[i] == ".":
            if pointerLocation < 0:
                print(end=chr(negarray[abs(pointerLocation) - 1]))
            else:
                print(end=chr(array[pointerLocation]))
        elif prg[i] == ",":
            x = input("> ")

            try:
                y = int(x)
            except ValueError:
                y = ord(x)

            if pointerLocation < 0:
                negarray[abs(pointerLocation) - 1] = y
            else:
                array[pointerLocation] = y
        elif prg[i] == "[":
            if pointerLocation < 0:
                if negarray[abs(pointerLocation) - 1] == 0:
                    open_braces = 1

                    while open_braces > 0:
                        i += 1

                        if prg[i] == "[":
                            open_braces += 1
                        elif prg[i] == "]":
                            open_braces -= 1
            elif array[pointerLocation] == 0:
                open_braces = 1

                while open_braces > 0:
                    i += 1

                    if prg[i] == "[":
                        open_braces += 1
                    elif prg[i] == "]":
                        open_braces -= 1
        elif prg[i] == "]":
            open_braces = 1

            while open_braces > 0:

                i -= 1

                if prg[i] == "[":
                    open_braces -= 1
                elif prg[i] == "]":
                    open_braces += 1

            i -= 1
        i += 1

interpret("}}}}}}}}===</nowiki>}}}}===</nowiki>}}</nowiki>}}}</nowiki>}}}</nowiki>}</code></code></code></code>{| class=\"wikitable\"<s></nowiki>}</nowiki>}</nowiki>{| class=\"wikitable\"</nowiki></nowiki>}===</code><s></code>{| class=\"wikitable\"<s></nowiki></nowiki>*</nowiki>{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"*}}}}}}}**}}}*</nowiki></nowiki>*</code>{| class=\"wikitable\"*</code>*}}}*{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"*{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"{| class=\"wikitable\"*</nowiki></nowiki>}*</nowiki>}}*")