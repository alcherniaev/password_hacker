'''def what_to_do(instructions):
    say = "Simon says"
    if instructions.startswith(say) or instructions.endswith(say):
        do = instructions.replace(say, '').strip()
        return f"I {do}"
    else:
        return "I won't do it!"'''

empty_l = []
empty_l.append(empty_l)

print(empty_l)    # [[...]]
print(empty_l.copy().copy)
