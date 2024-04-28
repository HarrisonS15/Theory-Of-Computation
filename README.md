## Deterministic Finite Automata:
1. In whichever approach you wish, have your program read in a text file called `dfa.txt`, and construct a DFA from this information. This file will contain data that describes a DFA.

2. The structure of `dfa.txt` will be as follows:
    - Line 1: the states of the DFA (separated by commas, if there is more than one state)
    - Line 2: the alphabet of the DFA (separated by commas, if there is more than one symbol)
    - Line 3: the starting state of the DFA
    - Line 4: the final/accept states of the DFA (separated by commas, if there is more than one accept state)
    - Line 5 and onward: the transition rules, where each rule takes the form `a,b,c` (where being in state ‘a’ and reading symbol ‘b’ transitions to new state ‘c’)

3. After your program constructs a DFA, read in another file called `input.txt`, where each line in the file is a string that will run on your DFA.

4. Both `dfa.txt` and `input.txt` should be assumed to be in the same directory as your Python program. Do not ask for the names of these; just hardcode them in.

5. Simulate each string in `input.txt` using your DFA, and write the output (`accept` or `reject`) into a new file called `output.txt` (also in the same directory as your Python program, and each result on a separate line).

6. There is one special input string ‘@’, which represents the empty string (a string of no characters).


## Nondeterministic Finite Automata:
1. In whichever approach you wish, have your program read in a text file called `nfa.txt`, and construct an NFA from this information. This file will contain data that describes an NFA.

2. The structure of `nfa.txt` will be as follows:
    - Line 1: the states of the NFA (separated by commas, if there is more than one state)
    - Line 2: the alphabet of the NFA (separated by commas, if there is more than one symbol)
    - Line 3: the starting state of the NFA
    - Line 4: the final/accept states of the NFA (separated by commas, if there is more than one accept state)
    - Line 5 and onward: the transition rules, where each rule takes the form `a,b,c` (where being in state ‘a’ and reading symbol ‘b’ transitions to new state ‘c’)

3. In addition to the given alphabet, all NFAs may also contain empty-string transitions (we will use `@` to represent an empty string transition).

4. After your program constructs an NFA, read in another file called `input.txt`, where each line in the file is a string that will run on your NFA.

5. Both `nfa.txt` and `input.txt` should be assumed to be in the same directory as your Python program. Do not ask for the names of these; just hardcode them in.

6. Simulate each string in `input.txt` using your NFA, and write the output (`accept` or `reject`) into a new file called `output.txt` (also in the same directory as your Python program, and each result on a separate line).

7. There is one special input string ‘@’, which represents the empty string (a string of no characters).


## Deterministic Pushdown Automata:
1. Read in a text file called `dpda.txt` and construct a DPDA. This file will contain data that describes a DPDA.

2. The structure of `dpda.txt` will be as follows:
- Line 1: the states of the DPDA (separated by commas, if there is more than one state)
- Line 2: the alphabet of the DPDA (separated by commas, if there is more than one symbol)
- Line 3: the alphabet of the stack
- Line 4: the starting state of the DPDA
- Line 5: the final/accept states of the DPDA (separated by commas, if there is more than one accept state)
- Line 6 and onward: the transition rules, where each rule takes the form `a,b,c,d,e` (where being in state ‘a’ and reading symbol ‘b’ while popping ‘c’ from the     top of the stack transitions to new state ‘d’ and pushes ‘e’ on the top of the stack)

3. In addition to the given alphabet, all DPDAs may also contain empty-string transitions for either the input character, the symbol at the top of the stack, or both (we will use ‘@’ to represent this). You can use any symbol for the bottom of the stack, but the provided examples I will give you use a ‘$’.

4. After your program constructs a DPDA, read in another file called `input.txt`, where each line in the file is a string that will run on your DPDA. Both `dpda.txt` and `input.txt` should be assumed to be in the same directory as your Python program. Simulate each string in `input.txt` using your DPDA, and write the output (accept or reject) into a new file called `output.txt` (also in the same directory as your Python program, and each result on a new line).


## Turing Machine:
1. Read in a text file called `tm.txt` and construct a Turing machine. This file will contain data that encodes a Turing machine.

2. The structure of `tm.txt` will be as follows:
    - Line 1: the states of the Turing machine (separated by commas, and ‘accept’ and ‘reject’ will always be states)
    - Line 2: the input alphabet (separated by commas, if there is more than one symbol)
    - Line 3: the tape alphabet (separated by commas, if there is more than one symbol, and assume that ‘_’ represents a blank space on the tape)
    - Line 4: the starting state of the Turing machine
    - Line 5 and onward: the transition rules, where each rule takes the form `a,b,c,d,e` (where being in state ‘a’ and reading symbol ‘b’ on the tape will write a       'c' to that location, move to new state ‘d’, and move the read/write head in direction ‘e’)

3. After your program constructs a Turing machine, read in another file called `input.txt`, where each line in the file is a string that will be loaded onto the Turing machine tape.

4. Both `tm.txt` and `input.txt` should be assumed to be in the same directory as your Python program.

5. Simulate each string inside of `input.txt` within your Turing machine, and write the output (`accept` or `reject`) into a new file called `output.txt` (also in the same directory as your Python program, and each result on a new line).

6. Technically, Turing Machines can get stuck looping. You can assume that every Turing Machines I give you will always halt.
