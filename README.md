# Monte-carlo-decryption
This uses the Metropolis-Hastings algorithm to decode a text created with a substitution cipher. I.e. each symbol, the symbols comprising letters and a limited number of other symbols, is substituted uniquely with another one of the symbols

# Description 
- The method requires the creation of a transition matrix. A demo and code is used for producing a transition matrix from War and Peace. The version of War and Peace is taken from Project Gutenberg. 
- A demo for the deciphering using Metropolis-Hasting is included.
- The function scramble is included to take a text and scramble it with a substitution cipher. The text must be provided as a txt file. Therefore, various texts may be tested with the decryption algorithm. 

# Packages
Works with:
- Python 3.9.7
- Numpy 1.20.3
