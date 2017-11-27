# Hidden-Markov-Model
An example of the common Hidden Markov Models implemented with the Forward algorithm and Viterbi algorithm. 

These programs discover:
How likely an HMM is to have generated a give sequence  -Forward Algorithm
What is the most likely "path" for a gernating a sequence of observations - Viterbi

Given:
The tranistion probabilities
The emission probabilities
The sequence


Forward Algorithm results:
  The X axis of the console printout is the state "l"
  The Y axis of the consol printout is the nucleotide of a sequence
  The final line contains the probability of the final state given "l" states and the transmission ("a") and emission ("e") probabilities

  Table "f" that is the probability of the nucleotide occuring at state "l" using a dynamic programming-esque approach that generates the entire table instead of asking for the probability at a precise point and generating backwards from there.

  
