# Monte-carlo-decryption
This uses the Metropolis-Hastings algorithm to decode a text created with a substitution cipher. I.e. each symbol, comprising letters and a limited number of other symbols, are substituted uniquely with another one of the symbols

# Description 
- The method requires the creation of a transition matrix. A demo and code is used for producing a transition matrix from War and Peace. The version of War and Peace is taken from Project Gutenberg. 
- A demo for the deciphering using Metropolis-Hasting is included.
- I will later upload a function for obtaining enciphered texts suitable for use with the algorithm. For now, a specific enciphered text is included in encrypted_message.txt

# Packages
Works with:
- Python 3.9.7
- Numpy 1.20.3
