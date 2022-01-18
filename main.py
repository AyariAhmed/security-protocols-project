from cryptographic_tools.hashing import Hash



Hash.hash('ahmed','md5',True)

t = Hash.hash('admin', 'sha256', True)
Hash.crack_hash(t,'sha256',True)


