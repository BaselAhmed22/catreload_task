def short_word(strings):
    if not strings:
        return None

    shortest = strings[0]

    for word in strings:
        if len(word) < len(shortest):
            shortest = word
    return shortest

words = ["code", "backend", "ai", "circle"]
result = short_word(words)
print(result)
