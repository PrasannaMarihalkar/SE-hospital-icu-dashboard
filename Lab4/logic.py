def feedback(code, guess):
    exact = 0
    used_code = [False] * len(code)
    used_guess = [False] * len(guess)

    # First resolve exact matches.
    for i, (code_ch, guess_ch) in enumerate(zip(code, guess)):
        if code_ch == guess_ch:
            exact += 1
            used_code[i] = True
            used_guess[i] = True

    # Then resolve partial matches using only unmatched positions.
    partial = 0
    for i, guess_ch in enumerate(guess):
        if used_guess[i]:
            continue

        for j, code_ch in enumerate(code):
            if used_code[j]:
                continue

            if guess_ch == code_ch:
                partial += 1
                used_code[j] = True
                break

    return exact, partial
