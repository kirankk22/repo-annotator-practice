def chunk_text(text, chunk_size):

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]