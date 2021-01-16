def what_to_do(instructions):
    say = "Simon says"
    if instructions.startswith(say) or instructions.endswith(say):
        do = instructions.replace(say, '').strip()
        return f"I {do}"
    else:
        return "I won't do it!"
