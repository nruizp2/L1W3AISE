import secrets

def generate_uuid():
    return '{:08x}-{:04x}-{:04x}-{:04x}-{:012x}'.format(
        secrets.randbits(32),
        secrets.randbits(16),
        secrets.randbits(16),
        secrets.randbits(16),
        secrets.randbits(48),
    )

# Example usage:
print(generate_uuid())
