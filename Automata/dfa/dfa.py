class State(object):

    def __init__(self, final):
        self.final = final
        # of form {value: state}
        self.connections = {}

    def addConnection(self, value, state):
        self.connections[value] = state


class DFA(object):

    def __init__(self):
        #of form {state name: state}
        self.states = {}
        self.currentState = None
        self.language = []
        with open("dfa.txt","r") as file:

            #read in states on line 1
            content = file.readline().strip()
            states = content.split(',')
            for state in states:
                self.states[state] = None

            #read in language on line 2
            content = file.readline().strip()
            self.language = content.split(',')

            #read in initial state on line 3
            content = file.readline().strip()
            self.initial = content

            #read in final states on line 4
            content = file.readline().strip()
            finalStates = content.split(',')

            #initialize all states
            for name in self.states.keys():
                final = False
                if name in finalStates:
                    final = True
                self.states[name] = State(final)

            #set initial state
            self.currentState = self.states[self.initial]

            #add all connections
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                connection = line.split(',')
                self.states[connection[0]].addConnection(connection[1],connection[2])

    def nextState(self, value):
         self.currentState = self.states[self.currentState.connections[value]]
         return self.currentState
    
    def getResult(self):
        return self.currentState.final
    
    def run(self, string):
        for char in string:
            if char == "@": break
            self.nextState(char)
        return self.getResult()

    #use getResult to write result on a new line of file
    def writeResult(self):
        with open("output.txt", "a") as file:
            file.write(f'{"accept" if self.getResult() else "reject"}\n')
    
    def readInput(self):
        with open("input.txt","r") as file:
            content = file.readlines()
            for line in content:
                line = line.strip()
                self.currentState = self.states[self.initial]
                self.run(line)
                self.writeResult()
        

if __name__ == "__main__":
    myDFA = DFA()
    myDFA.readInput()



""" Test dfa
a,b,c,d,e
1,0
a
b,c,d
a,1,e
a,0,b
b,1,e
b,0,c
c,0,e
c,1,d
d,1,e
d,0,e
e,1,e
e,0,e
"""

            
            

            