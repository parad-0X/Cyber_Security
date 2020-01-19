Alice and Bob are communicating with the help of Merkle’s puzzles to establish a common secret key. In this problem, we (slightly) modified the Merkle’s puzzle set-up for learning and automation purposes.

All the puzzles are encrypted using the same AES-128 key (in the ctr mode), but the first 14 bytes of the key are just zero. Alice has to figure out the remaining two bytes of the key, of course. The encrypted message inside each puzzle has this format:”Puzzle is  x:k” (without quotes), where both x and k are  128-bit random numbers. Note that P is upper case in “Puzzle”.

Bob sends 65,000 puzzles to Alice who picks one of the random puzzles and return x (in cleartext) to Bob. You can download all 65,000 puzzles from my google drive site. Each row of this puzzle file is a ciphertext (a.k.a., puzzle) from Bob to Alice. The IV is 16 bytes, the prefix of each ciphertext.

 Eve who wants to find out the secret key k which corresponds to x =740AC607E4F3A32193DA750FACF38D87.
Develop an algorithm and a program to find k from x using the 65,000 puzzles.
