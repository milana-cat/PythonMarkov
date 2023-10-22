def start(rule_list, changed_string):
    result = ""
    rules = rule_list.split(";")
    for n in range(0, len(rules)):
        rules[n] = rules[n].split("-")
    while True:
        change_mark = False
        for i in range(0, len(rules)):
            if changed_string.find(rules[i][0]) > -1:
                result = changed_string.replace(rules[i][0], rules[i][1], 1)
                change_mark = True
                break
            else:
                continue
        changed_string = result
        if change_mark is True:
            print(changed_string)
        else:
            break


def check_rules(rule_list, void_char):
    rules = rule_list.split("\n")
    for n in range(0, len(rules)):
        rules[n] = rules[n].split("-")
    for s in rules:
        if s[0].find(void_char) != -1 or s[1].finds(s[0]) != -1:
            return False
