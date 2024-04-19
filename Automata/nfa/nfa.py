class State():

    def __init__(self, final):
        self.final = final
        # of form {value(str): state(str)}
        self.connections = {}
        self.emptyStateConnection = False
        self.emptyConnections = []
        self.name = ""

    def addConnection(self, value, state):
        if value == "@":
            self.emptyConnections.append(state)
        if value in self.connections.keys():
            self.connections[value].append(state)
        else:
            self.connections[value] = [state]

class NFA():

    def __init__(self):
        #of form {state(str): State(state)}
        self.states = {}
        self.currentState = None
        self.language = []
        with open("nfa.txt","r") as file:

            #read in states on line 1
            content = file.readline().strip()
            states = content.split(',')
            for state in states:
                self.states[state] = None

            #read in language on line 2
            content = file.readline().strip()
            self.language = content.split(',')
            self.language.append("@")

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
                self.states[name].name = name

            #set initial state
            self.currentState = self.states[self.initial]

            #add all connections
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                connection = line.split(',')
                if connection[1] == "@":
                    self.states[connection[0]].emptyStateConnection = True
                self.states[connection[0]].addConnection(connection[1],connection[2])
    
    def run(self, string, currentState, loopSafety):
        result = False
        #base case, if the string is empty and the current state is final, it passes
        if len(string) == 0 and currentState.final:
            return currentState.final
        
        #fail safe for infinite loops through empty strings
        if loopSafety >=50:
            return False

        #check all the empty string connections
        if currentState.emptyStateConnection:
            for i in range(len(currentState.emptyConnections)):
                result = self.run(string, self.states[currentState.emptyConnections[i]], loopSafety+1)

        #base case
        if len(string) == 0:
            return currentState.final or result
        
        #if this specific path of the nfa doesnt work, then return the result of the empty string paths
        
        if string[0] not in currentState.connections.keys():
            return result
        
        #check each connection for the current value (there can be multiple for a single value)
        
        for i in range(len(currentState.connections[string[0]])):
            result = result or self.run(string[1:], self.states[currentState.connections[string[0]][i]], 0)

        return result

    
    def writeResult(self, result):
        with open("output.txt", "a") as file:
            file.write(f'{"accept" if result else "reject"}\n')
    
    def readInput(self):
        with open("input.txt","r") as file:
            content = file.readlines()
            for line in content:
                line = line.strip()
                self.currentState = self.states[self.initial]
                result = self.run(line, self.currentState, 0)
                self.writeResult(result)
        

if __name__ == "__main__":
    myNFA = NFA()
    myNFA.readInput()


