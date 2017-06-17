# Hashnator
A very basic Python hash system with 3 levels of hashing

# This python module is not for real cases like security stuffs, only for study.

To use is very simple:

Test = Hashnator.Hashnator ()
print Test.Hash

# Level two of hash with 24 characters
Test = Hashnator.Hashnator (HashLevel = 2, HashSize = 24)
print Test.Hash

# Level tree of hash with 32 characters
Test = Hashnator.Hashnator (HashLevel = 3, HashSize = 32)
print Test.Hash
