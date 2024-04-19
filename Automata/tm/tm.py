
class TapeLanguageException(Exception):
    pass

class Tape():
    def __init__(self):
        self.tape = ['_']
        self.head = 0
        self.language = ['_']

    def left(self):
        if self.head == 0:
            return self.head
        
        self.head -= 1
        return self.head

    def right(self):
        self.head += 1
        return self.head
    
    def write(self, value):
        if value not in self.language:
            raise TapeLanguageException
        
        self.tape[self.head] = value
        if self.head == len(self.tape):
            self.tape.append('_')


class State():

    def __init__(self, final):
        self.final = final
        # of form {value(str): state(str)}
        self.connections = {}
        self.emptyStateConnection = False
        self.emptyConnections = []
        self.name = ""

    def addConnection(self, value, state, pop, push):
        if value == "@":
            self.emptyStateConnection = True
        self.connections[value] = state

class TuringMachine():
    ''' Cases:
        1, 0: read in 1 as input, and if 0 is top of stack
        @ means dont push or pop or take input from string
    '''
    def __init__(self):
        #of form {state(str): State(state)}
        self.states = {}
        self.currentState = None
        self.language = []
        self.tape = Tape()
        with open("tm.txt","r") as file:

            #read in states on line 1
            content = file.readline().strip()
            states = content.split(',')
            for state in states:
                self.states[state] = None

            #read in language on line 2
            content = file.readline().strip()
            self.language = content.split(',')
            self.language.append("@")

            #read in stack language on line 3
            content = file.readline().strip()
            self.stackLanguage = content.split(',')
            self.stackLanguage.append("@")

            #read in initial state on line 4
            content = file.readline().strip()
            self.initial = content

            #read in final states on line 5
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
                if connection[2] == "@":
                    self.states[connection[0]].emptyStackConnection = True
                self.states[connection[0]].addConnection(connection[1], connection[3], connection[2], connection[4])

    def run(self, string):
        safety = 0
        while True:

            if len(string) == 0 and self.currentState.final:
                return True
            
            if safety >= 50:
                return False
            
            value = -1

            if len(string) != 0:
                value = string[0]

            if self.currentState.emptyStateConnection and value not in self.currentState.connections:
                currentState = self.states[self.currentState.connections['@']]
                value = '@'
            elif value not in self.currentState.connections:
                return False
            else:
                currentState = self.states[self.currentState.connections[value]]

            pop, push = self.currentState.stackConnections[value]
            self.currentState = currentState
            if pop != '@':
                popped = self.stack.pop()
                if popped != pop:
                    return False
            if push != '@':
                self.stack.push(push)


            if len(string) != 0 and value != '@':
                string = string[1:]

            safety += 1
        
        

    def writeResult(self, result):
        with open("output.txt", "a") as file:
            file.write(f'{"accept" if result else "reject"}\n')
    
    def readInput(self):
        with open("input.txt","r") as file:
            content = file.readlines()
            for line in content:
                line = line.strip()
                self.currentState = self.states[self.initial]
                result = self.run(line)
                self.writeResult(result)
        

if __name__ == "__main__":
    myTM = TuringMachine()
    myTM.readInput()