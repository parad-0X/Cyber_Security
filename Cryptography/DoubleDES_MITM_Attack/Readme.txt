2DESk1, k2(x) = DESk2(DESk1(x)), where k1 and k2 are two random keys of length 56-bit each and x is the input plaintext of 64-bit.

Your task is to break 2DES using the meet-in-the-middle attack pattern. Demonstrate that you can identify both k1 and k2 by using two random plaintext-ciphertext pairs <x1, y1> and <x2, y2>, where yi = 2DESk1, k2(xi).

Develop a computer program which takes <x1, y1> and <x2, y2> as the input and produces k1 and k2 as outputs. For simplicity and scalability reasons, assume that the first 32-bit of k1 and k2 are the same and given to you (you may “hardcode” any 32-bit you prefer). 
