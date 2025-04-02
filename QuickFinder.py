def extended_gcd(a, b):
    """Returns gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(b, a):
    """Finds modular inverse of b modulo a (only works if gcd(b, a) = 1)."""
    gcd, x, _ = extended_gcd(b, a)
    if gcd != 1:
        return None  # No inverse exists
    return x % a  # Ensure positive value

def find_n_z(A, B, c):
    """Finds integers n and z satisfying A*z + c = n*B."""
    if c%A==0:
        return 0,0
    B_inv = mod_inverse(B, A)  # Compute B^(-1) mod A
    
    if B_inv is None:
        return None  # Should never happen because A and B are coprime

    n = (c * B_inv) % A  # Compute n in integer scope
    z = (n * B - c) // A  # Compute z

    # Ensure that n and z are positive (mod A or A for z)
    n = (n + A) % A  # Make sure n is positive
    z = (z + A) % A  # Make sure z is positive

    return n, z

# Ex