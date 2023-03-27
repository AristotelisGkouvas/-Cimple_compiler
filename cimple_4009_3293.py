import sys
import string

#############################################################################
#	LEKTIKOS ANALYTHS:														#
#############################################################################
line = 1

family = ''
lexical = ''
tokenType = ''
programName = ''

def lexicalAnalyzer():

    # counting variables
    global line             #Current line
    global family
    global lexical
    global tokenType

    family = ''
    tokenType = ''
    lexical = ''
    character = 0  #counting number of letter

    token_char = file.read(1)

    # TAB or SPACE or newline
    while token_char == '\t' or token_char == ' ' or token_char == '\r':
        token_char = file.read(1)

    if token_char == '\n':
        line += 1
        return lexicalAnalyzer()

    # Letter
    elif token_char.isalpha():
        lexical = token_char
        token_char = file.read(1)
        character += 1
        while token_char.isalpha() or token_char.isdigit():
            if character > 30:
                print(('Error in line %d: Word lenght surpassed limit of 30.', line))
            lexical = lexical + token_char
            character += 1
            token_char = file.read(1)
            #print('\t( %s )' % (token_char))
        file.seek(file.tell() - 1)
        family = 'Keyword'

        if lexical == 'program':
            tokenType = 'program_token'

        elif lexical == 'declare':
            tokenType = 'declare_token'

        elif lexical == 'if':
            tokenType = 'if_token'

        elif lexical == 'else':
            tokenType = 'else_token'

        elif lexical == 'while':
            tokenType = 'while_token'

        elif lexical == 'switchcase':
            tokenType = 'switchcase_token'

        elif lexical == 'forcase':
            tokenType = 'forcase_token'

        elif lexical == 'incase':
            tokenType = 'incase_token'

        elif lexical == 'case':
            tokenType = 'case_token'

        elif lexical == 'default':
            tokenType = 'default_token'

        elif lexical == 'not':
            tokenType = 'not_token'

        elif lexical == 'and':
            tokenType = 'and_token'

        elif lexical == 'or':
            tokenType = 'or_token'

        elif lexical == 'function':
            tokenType = 'function_token'

        elif lexical == 'procedure':
            tokenType = 'procedure_token'

        elif lexical == 'call':
            tokenType = 'call_token'

        elif lexical == 'return':
            tokenType = 'return_token'

        elif lexical == 'in':
            tokenType = 'in_token'

        elif lexical == 'inout':
            tokenType = 'inout_token'

        elif lexical == 'input':
            tokenType = 'input_token'

        elif lexical == 'print':
            tokenType = 'print_token'
        else:
            tokenType = 'id_token'
            family = 'Identifier'

    # Digit
    elif token_char.isdigit():
        lexical = token_char
        token_char = file.read(1)

        while token_char.isdigit():
            lexical = lexical + token_char
            token_char = file.read(1)
            num = int(lexical)
            if (num < -4294967297 or num > 4294967295):
                print('Error in line %d: Invalid range of number %s ( -2^32+1 > number > 2^32-1).' % (line, lexical))
                sys.exit(0)
        file.seek(file.tell() - 1)
        tokenType = 'INTEGER_token'

        family = 'Number'

    # '+' or '-'
    elif token_char == '+' or token_char == '-':
        lexical = token_char
        if lexical == '+':
            tokenType = 'plus_token'
        elif lexical == '-':
            tokenType = 'minus_token'

        family = 'Add_Operator'

    # '*' or '/'
    elif token_char == '*' or token_char == '/':
        lexical = token_char
        if lexical == '*':
            tokenType = 'multiply_token'
        elif lexical == '/':
            tokenType = 'division_token'

        family = 'Mul_Operator'

    # ':='
    elif token_char == ':':
        lexical = lexical + token_char
        token_char = file.read(1)
        if token_char == '=':
            tokenType = 'assign_token'
            lexical = lexical + token_char
            token_char = file.read(1)
        file.seek(file.tell() - 1)

        family = 'Assignment'

    # ',' or ';'
    elif token_char == ',' or token_char == ';':
        lexical = token_char
        if lexical == ',':
            tokenType = 'comma_token'
        elif lexical == ';':
            tokenType = 'semicolon_token'

        family = 'Delimiter'

    # '=' or '<>' or '<=' or '<' or '>=' or '>'
    elif token_char == '='  or token_char == '<' or token_char == '>':
        lexical = token_char
        if lexical == '=':
            token_char = file.read(1)
            tokenType = 'equals_token'
            lexical = lexical + token_char
        elif lexical == '<':
            token_char = file.read(1)
            if token_char == '>':
                tokenType = 'notequal_token'
                lexical = lexical + token_char

            elif token_char == '=':
                tokenType = 'lessorequals_token'
                lexical = lexical + token_char
            else:
                tokenType = 'less_token'
                file.seek(file.tell() - 1)
        elif lexical == '>':
            token_char = file.read(1)
            if token_char == '=':
                tokenType = 'greaterorequals_token'
                lexical = lexical + token_char
            else:
                tokenType = 'greater_token'
                file.seek(file.tell() - 1)

        family = 'Rel_Operator'
    # '(' or ')' or '{' or '}' or '[' or ']'
    elif token_char == '(' or token_char == ')' or token_char == '{' or token_char == '}' or token_char == '[' or token_char == ']':
        lexical = token_char
        if lexical == '(':
            tokenType = 'leftbracket_token'

        elif lexical == ')':
            tokenType = 'rightbracket_token'

        elif lexical == '{':
            tokenType = 'begin_token'

        elif lexical == '}':
            tokenType = 'end_token'

        elif lexical == ']':
            tokenType = 'rightsquarebracket_token'

        elif lexical == '[':
            tokenType = 'leftsquarebracket_token'

        family = 'Group_Symbol'

    # End program
    elif token_char == '.':
        lexical = token_char
        tokenType = 'endprogram_token'

        family = 'Delimiter'

    # Comments
    elif token_char == '#':
        lexical = token_char
        token_char = file.read(1)
        flag = False
        while token_char != '':
            token_char = file.read(1)
            if token_char == '#':
                flag= True
                break
        if flag == True:
            lexicalAnalyzer()
        else:
            print('Error in line %d: "#" is missing. The comment was supposed to be closed.' % (line))
            sys.exit(0)

    elif token_char == '':
        lexical = ''
        tokenType = 'eof_token'

    else:
        print('Error in line %d : character is not recognised as a language character/symbol ' % (line))
        sys.exit(0)

    ##### If it finds a comment, it prints the next lexical twice #####
    print('Line: %d \t%s\t\t\tfamily: %s ' % (line,lexical,family))

    return tokenType


#############################################################################
#	SYNTAKTIKOS ANALYTHS  &  ENDIAMESOS KWDIKAS				                #
#############################################################################

global listOfQuads
global listOfTemps
global listOfScopes

global scopes
global nestingLevel

global int_file
global c_file
global scopes_file

listOfQuads = []
listOfTemps = []
listOfScopes = []

numQuad = 0
numTemp = 1


class Token():
    def __init__(self,lexical,family,line):
        self.lexical, self.family, self.line = lexical, family, line

class Quad():
    def __init__(self,label,op1,op2,op3,op4):
        self.label, self.op1, self.op2, self.op3, self.op4 = label, op1, op2, op3, op4

class Scope():
    def __init__(self, name, entities, level):
        self.name, self.entities, self.level = name, list(), level

class Entity():
    def __init__(self, name, offset=None, en_type=None, label=None, arguments=0, framelength=None, parmode=None ):
        self.name, self.offset, self.en_type, self.label, self.arguments, self.framelength, self.parmode = name, offset, en_type, label, list(), framelength, parmode


def findFrameLength(i):
    for x in range(i,len(listOfQuads)):# Psa3e sthn quadlist
        if listOfQuads[x].op1 == 'CALL': # Otan breis to prwto "call"
            for scope in scope_array:
                for entity in scope.entities:# Gia ka8e entity
                    if entity.name == listOfQuads[x].op2:
                        return entity.framelength # Epestrespe to framelength


def calculateOffset(var):
    prev_offset = 0
    # for entities in current scope
    for entity in scope_array[current_level].entities:
        # for entities in current scope
        if entity.en_type == None and entity.name != var and entity.offset != None:
            prev_offset = entity.offset
    # find the var-entity
    for entity in scope_array[current_level].entities:
        if entity.name == var:
            if prev_offset == 0:
                entity.offset = 12
            else:
                entity.offset = prev_offset+4


def calculateFramelengths():
    global mainFrame
    maxoffset=0
    # if it has entities,calculate the maxoffset because maxoffset(+4)=framelength
    if len(scope_array[current_level].entities)>0:
        # find the first entity that has offset, and set it as a start point to find the maxoffset
        for entity in scope_array[current_level].entities:
            if entity.offset != None:
                maxoffset=entity.offset
                break
        # find the maxoffset
        for entity in scope_array[current_level].entities:
            if entity.offset>maxoffset:
                maxoffset=entity.offset

    if current_level-1>=0:
        n=scope_array[current_level-1]
        for entity in n.entities:
            # if entity is proc or func and framelength is empty, calculate it
            if entity.en_type != None and entity.framelength == None:
                # if maxoffset is 0, it means it has no vars, so the framelength must not be maxoffset+4=4
                if maxoffset==0:
                    entity.framelength=0
                else:
                    entity.framelength=maxoffset+4
    else:
        if maxoffset==0:
                mainFrame=0
        else:
            mainFrame=maxoffset+4


def createScope(name):
    #create a scope for main program and each function/proc
    global current_level
    current_level=current_level+1
    scope=Scope(name,[],current_level)
    scope_array.append(scope)
    return scope


def printCurrentScope():
    scopes_file.write('[Scope '+str(current_level)+' : ('+scope_array[current_level].name+')]')
    for entity in scope_array[current_level].entities:
        if entity.offset==None:
            scopes_file.write('--->('+entity.name+',FL:'+str(entity.framelength)+',SQ:'+str(entity.label )+')')
        else:
            if entity.parmode!=None:
                scopes_file.write('--->('+entity.name+':'+str(entity.offset)+',%s)'%(entity.parmode))
            else:
                scopes_file.write('--->('+entity.name+':'+str(entity.offset)+')')


def deleteCurrentScope():
    global current_level
    current_level=current_level-1
    del scope_array[-1]


def searchPars(name,parList):
    for scope in scope_array:
        for entity in scope.entities:
            if entity.name==name and (entity.en_type=='function' or entity.en_type=='procedure'):
                if len(parList) == len(entity.arguments):#check general number of parameters
                    for x in range(0,len(parList)):
                        if parList[x]==entity.arguments[x].parmode:
                            pass
                        else:
                            print('Error in line %s: Wrong passing in parameter "%s". Expected "%s" but is "%s".'%(line,str(x+1),entity.arguments[x].parmode,parList[x]))
                            sys.exit(0)
                else:
                    print('Error in line %s: Wrong number of parameters in procedure/function "%s". '%line)
                    sys.exit(0)


def nextQuad():
    # Epistrefei ton aritho ths epomenhs tetradas
    global numQuad
    return numQuad

def genQuad(op1, op2, op3, op4):
    # Dhmiourgei thn epomenh 4ada
    global numQuad
    global listOfQuads

    quad = Quad(numQuad,op1,op2, op3, op4)
    numQuad += 1
    listOfQuads.append(quad)

def newTemp():
    # Dhmiourgei kai epistrefei mia nea proswrinh metablhth
    global numTemp
    global listOfTemps

    list = ['T_']
    list.append(str(numTemp))
    temps = "".join(list)
    numTemp += 1
    listOfTemps += [temps]
    return temps

def emptyList():
    # Dhmiourgei mia kenh lista etiketwn 4dwn
    return list()

def makeList(x):
    # Dhmiourgei mia lista etiketwn tetradwn pou periexei mono to x
    return [x]

def merge(list_1,list_2):
    # Dhmiourgei mia lista etiketwn 4dwn apo th synenwsh listwn list1, list2
    return list_1+list_2

def backPatch(list, z):
    # Sarwnw thn listOfQuads kai gia kathe 4ada pou to 4o teloumeno den einai symplhrwmeno ("_") to symbplhrwnw me thn etiketa "z"
    global listOfQuads
    for i in listOfQuads:
        if i.label in list:
            i.op4 = z
    return

def syntaxAnalyzer(c_file):

    global tokenType
    global lexical
    global programName

    global scopes
    global listOfScopes
    global nestingLevel


    def program():
        # program ID block .

        # "program" is the starting symbol
        # followed by its name and a block
        # every program ends with a fullstop
        global tokenType
        global lexical
        global programName

        tokenType = lexicalAnalyzer()

        if tokenType == 'program_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                programName = lexical
                tokenType = lexicalAnalyzer()
                genQuad('BEGIN_PROGRAM_BLOCK', programName, '_', '_')
                block(programName, 1)
                if tokenType == 'endprogram_token':
                    tokenType = lexicalAnalyzer()
                    if tokenType == 'eof_token':
                        genQuad('BEGIN_PROGRAM_BLOCK', programName, '_', '_')
                        print("\nCompilation successfully completed without errors.\n")
                        nextQuad()
                        return
                    else:
                        print('Error in line %d: No characters are allowed after the fullstop indicating the end of the program.' % (line))
                        sys.exit(0)
                else:
                    print('Error in line %d: A fullstop expected, the program should end with a fullstop.' % (line))
                    sys.exit(0)
            else:
                print('Error in line %d: The program name expected after the keyword "program" but found "%s" .' % (line, lexical))
                sys.exit(0)
        else:
            print('Error in line %d: The program must start with the keyword "program" but instead it starts with the word "%s".' % (line, lexical))
            sys.exit(0)


    def block(programName, mainProgram):
        # { declarationsprogramName subprograms blockStatements }

        # a block consists of declarations, subprograms and blockStatements
        global tokenType

        if tokenType == 'begin_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'declare_token':
                declarations()
            subprograms()
            if mainProgram == 0:
                genQuad('BEGIN_BLOCK', programName, '_', '_')
            blockStatements()
            if tokenType == 'end_token':
                if mainProgram == 1:
                    genQuad('HALT', '_', '_', '_')
                if mainProgram == 0:
                    genQuad('END_BLOCK', programName, '_', '_')
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: The "}" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "{" was expected .' % line)
            sys.exit(0)
        return


    def declarations():
        # ( declare varlist ; ) *

        # declaration of variables
        # kleene star implies zero or more "declare" statements
        global tokenType

        while tokenType == 'declare_token':
            tokenType = lexicalAnalyzer()
            varlist()
            if tokenType == 'semicolon_token':
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: The keyword ";" was expected\n' % line)
                sys.exit(0)
        return


    def varlist():
        # ID ( , ID ) *
        # | e

        # a list of variables following the declaration keyword
        global tokenType

        if tokenType == "id_token":
            tokenType = lexicalAnalyzer()
            while tokenType == 'comma_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'id_token':
                    tokenType = lexicalAnalyzer()
                else:
                    print('Error in line %d: A variable is expected after comma (,). ' % line)
                    sys.exit(0)
        return


    def subprograms():
        # ( subprogram ) *

        # zero or more subprograms
        global tokenType

        while tokenType == 'procedure_token' or tokenType == 'function_token':
            subprogram()
        return


    def subprogram():
        # a subprogram is a function or a procedure
        # followed by parameters and block
        global tokenType
        global lexical

        # function ID ( formalparlist ) block
        if tokenType == 'function_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                idName = lexical
                tokenType = lexicalAnalyzer()
                if tokenType == "leftbracket_token":
                    tokenType = lexicalAnalyzer()
                    formalparlist()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        block(idName,0)
                    else:
                        print('Error in line %d: The ")" was expected .' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected .' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: A variable is expected after the keyword "function".' % line)
                sys.exit(0)

        # procedure ID ( formalparlist ) block
        elif tokenType == 'procedure_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                idName = lexical
                tokenType = lexicalAnalyzer()
                if tokenType == "leftbracket_token":
                    tokenType = lexicalAnalyzer()
                    formalparlist()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        block(idName,0)
                    else:
                        print('Error in line %d: The ")" was expected .' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected .' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: A variable is expected after the keyword "procedure".' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The keyword "function" or "procedure" was expected.' % line)
            sys.exit(0)
        return


    def formalparlist():
        # formalparitem ( , formalparitem ) *

        # list of formal parameters
        # one or more parameters are allowed
        global tokenType

        formalparitem()
        while tokenType == 'comma_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'in_token' or tokenType == 'inout_token':
                formalparitem()
            else:
                print('Error in line %d: Expected "in" or "inout" after the comma.' %  line)
                sys.exit()
        return


    def formalparitem():
        # a formal parameters
        # "in": by value, "inout": by reference
        global tokenType

        # in ID
        if tokenType == 'in_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: A variable is expected after the keyword "in".' % line)
                sys.exit(0)

        # inout ID
        elif tokenType == 'inout_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: A variable is expected after the keyword "inout".' % line)
                sys.exit(0)


    def statements():
        # statement  ;
        # | { statement ( ; statement ) * }

        # one or more statements
        # more than one statements should be grouped with brackets
        global tokenType

        if tokenType == 'begin_token':
            tokenType = lexicalAnalyzer()
            blockStatements()
            if tokenType == 'end_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: The "}" was expected .' % line)
                sys.exit(0)
        else:
            statement()
            if tokenType == 'semicolon_token':
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: The keyword ";" was expected\n' % line)
                sys.exit(0)
        return


    def blockStatements():
        # statement ( ; statement ) *

        # statements cosidered as block (used in program and subprogram)

        global tokenType

        statement()
        while tokenType == 'semicolon_token':
            tokenType = lexicalAnalyzer()
            statement()
        return


    def statement():
        # one statement

        global tokenType

        # assignStat
        if tokenType == 'id_token':
            assignStat()
        # ifStat
        elif tokenType == 'if_token':
            ifStat()
        # whileStat
        elif tokenType == 'while_token':
            whileStat()
        # switchcaseStat
        elif tokenType == 'switchcase_token':
            switchcaseStat()
        # forcaseStat
        elif tokenType == 'forcase_token':
            forcaseStat()
        # incaseStat
        elif tokenType == 'incase_token':
            incaseStat()
        # callStat
        elif tokenType == 'call_token':
            callStat()
        # returnStat
        elif tokenType == 'return_token':
            returnStat()
        # inputStat
        elif tokenType == 'input_token':
            inputStat()
        # printStat
        elif tokenType == 'print_token':
            printStat()
        return


    def assignStat():
        # ID := expression

        # assignment statement
        global tokenType
        global lexical

        if tokenType == 'id_token':
            id_name = lexical
            tokenType = lexicalAnalyzer()
            if tokenType == 'assign_token':
                tokenType = lexicalAnalyzer()
                e_place = expression()
                # Start P1
                genQuad(":=", e_place, '_', id_name)
                # End P1
            else:
                print('Error in line %d: The assignment symbol ":=" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "id" was expected.' % line)
            sys.exit(0)
        return


    def ifStat():
        # if ( condition ) statements
        # elsepart

        # if statement
        global tokenType

        if tokenType == 'if_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                cond = condition()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                    # Start P1 #
                    backPatch(cond[0], nextQuad())
                    # End P1 #
                    statements()
                    # Start P2 #
                    ifList = makeList(nextQuad())
                    genQuad('JUMP', '_', '_', '_' )
                    backPatch(cond[1], nextQuad())
                    # End P2 #
                    elsePart()
                    # Start P3 #
                    backPatch(ifList, nextQuad())
                    # End P3 #
                else:
                    print('Error in line %d: The ")" was expected .' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected .' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "if" was expected.' % line)
            sys.exit(0)
        condition_true = cond[0]
        condition_false = cond[1]
        return condition_true, condition_false


    def elsePart():
        # else statements
        # | e

        # else part is optional
        global tokenType

        if tokenType == 'else_token':
            tokenType = lexicalAnalyzer()
            statements()
        return


    def whileStat():
        # while ( condition ) statements

        # while statement
        global tokenType

        if tokenType == 'while_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                # Start P0
                condQuad = nextQuad()
                # End P0
                cond = condition()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                    # Start P1
                    backPatch(cond[0], nextQuad())
                    # End P1
                    statements()
                    # Start P2
                    genQuad('JUMP', '_', '_', condQuad)
                    backPatch(cond[1], nextQuad())
                    # End P2
                else:
                    print('Error in line %d: The ")" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "while" was expected.' % line)
            sys.exit(0)
        condition_true = cond[0]
        condition_false = cond[1]
        return condition_true, condition_false


    def switchcaseStat():
        # switchcase
        #   ( case ( condition ) statements ) *
        #   default statements

        # switch statement
        global tokenType

        if tokenType == 'switchcase_token':
            tokenType = lexicalAnalyzer()
            # Start P0
            exitList = emptyList()
            # End P0
            if tokenType == 'case_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    cond = condition()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        # Start P1
                        backPatch(cond[0], nextQuad())
                        # End P1
                        statements()
                        # Start P2
                        t = makeList(nextQuad())
                        genQuad('JUMP', '_', '_', '_')
                        exitList = merge(exitList,t)
                        backPatch(cond[1], nextQuad())
                        # End P2
                        while tokenType == 'case_token':
                            tokenType = lexicalAnalyzer()
                            if tokenType == 'leftbracket_token':
                                tokenType = lexicalAnalyzer()
                                cond = condition()
                                if tokenType == 'rightbracket_token':
                                    tokenType = lexicalAnalyzer()
                                    # Start P1
                                    backPatch(cond[0], nextQuad())
                                    # End P1
                                    statements()
                                    # Start P2
                                    t = makeList(nextQuad())
                                    genQuad('JUMP', '_', '_', '_')
                                    exitList = merge(exitList, t)
                                    backPatch(cond[1], nextQuad())
                                    # End P2
                        while tokenType == 'default_token':
                            tokenType = lexicalAnalyzer()
                            statements()
                            # Start P3
                            backPatch(exitList, nextQuad())
                            # End P3
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "case" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "switchcase" was expected.' % line)
            sys.exit(0)
        condition_true = cond[0]
        condition_false = cond[1]
        return condition_true, condition_false


    def forcaseStat():
        # forcase
        #   ( case ( condition ) statements ) *
        #   default statements

        # forcase statement
        global tokenType

        if tokenType == 'forcase_token':
            tokenType = lexicalAnalyzer()
            # Start P1
            firstCondQuad = nextQuad()
            # End P1
            if tokenType == 'case_token':
                tokenType = lexicalAnalyzer()
                print(tokenType)
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    cond = condition()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        # Start P2
                        backPatch(cond[0], nextQuad())
                        # End P2
                        statements()
                        # Start P3
                        genQuad('JUMP', '_', '_', firstCondQuad)
                        backPatch(cond[1], nextQuad())
                        # End P3
                        while tokenType == 'case_token':
                            tokenType = lexicalAnalyzer()
                            print(tokenType)
                            if tokenType == 'leftbracket_token':
                                tokenType = lexicalAnalyzer()
                                cond = condition()
                                if tokenType == 'rightbracket_token':
                                    tokenType = lexicalAnalyzer()
                                    # Start P2
                                    backPatch(cond[0], nextQuad())
                                    # End P2
                                    statements()
                                    # Start P3
                                    genQuad('JUMP', '_', '_', firstCondQuad)
                                    backPatch(cond[1], nextQuad())
                                    # End P3
                        while tokenType == 'default_token':
                            tokenType = lexicalAnalyzer()
                            statements()
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "case" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "forcase" was expected.' % line)
            sys.exit(0)
        condition_true = cond[0]
        condition_false = cond[1]
        return condition_true, condition_false
        return

    def incaseStat():
        # incase
        #   ( case ( condition ) statements )*

        # incase statement
        global tokenType

        if tokenType == 'incase_token':
            tokenType = lexicalAnalyzer()
            # Start P1
            flag = newTemp()
            firstCondQuad = nextQuad()
            genQuad(':=', '0', '_', flag)
            # End P1
            if tokenType == 'case_token':
                tokenType = lexicalAnalyzer()
                print(tokenType)
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    cond = condition()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        # Start P2
                        backPatch(cond[0], nextQuad())
                        # End P2
                        statements()
                        # Start P3
                        genQuad(':=', '1', '_', flag)
                        backPatch(cond[1], nextQuad())
                        # End P3
                        while tokenType == 'case_token':
                            tokenType = lexicalAnalyzer()
                            print(tokenType)
                            if tokenType == 'leftbracket_token':
                                tokenType = lexicalAnalyzer()
                                cond = condition()
                                if tokenType == 'rightbracket_token':
                                    tokenType = lexicalAnalyzer()
                                    # Start P2
                                    backPatch(cond[0], nextQuad())
                                    # End P2
                                    statements()
                                    # Start P3
                                    genQuad(':=', '1', '_', flag)
                                    backPatch(cond[1], nextQuad())
                                    # End P3
                        while tokenType == 'default_token':
                            tokenType = lexicalAnalyzer()
                            statements()
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "case" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "incase" was expected.' % line)
            sys.exit(0)
        # Start P4
        genQuad('=', '1', flag, firstCondQuad)
        # End P4
        condition_true = cond[0]
        condition_false = cond[1]
        return condition_true, condition_false


    def returnStat():
        # return ( expression )

        # return statement
        global tokenType

        if tokenType == 'return_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                e_place = expression()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                    # Start P1
                    genQuad('RET', e_place, '_', '_')
                    # End P1
                else:
                    print('Error in line %d: The ")" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "return" was expected.' % line)
            sys.exit(0)
        return


    def callStat():
        # call ID ( actualparlist )

        # call statement
        global tokenType
        global lexical

        if tokenType == 'call_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                idName = lexical
                tokenType = lexicalAnalyzer()
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    actualparlist()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        if tokenType == 'procedure_token':
                            genQuad('CALL', idName, '_', '_')
                            tokenType = lexicalAnalyzer()         
                        elif tokenType == 'function_token':
                            w = newTemp()
                            genQuad('PAR', w, 'RET', '_')
                            genQuad('CALL', idName, '_', '_')
                            tokenType = lexicalAnalyzer()
                            return w
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "id" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "call" was expected.' % line)
            sys.exit(0)


    def printStat():
        # print ( expression )

        # print statement
        global tokenType

        if tokenType == 'print_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                e_place = expression()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                    # Start P1
                    genQuad('OUT', e_place, '_', '_')
                    # End P1
                else:
                    print('Error in line %d: The ")" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "print" was expected.' % line)
            sys.exit(0)
        return


    def inputStat():
        # input ( ID )

        # input statement
        global tokenType
        global lexical

        if tokenType == 'input_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'id_token':
                    idName = lexical
                    tokenType = lexicalAnalyzer()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        genQuad('INP', idName, '_', '_')
                        return
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "id" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "input" was expected.' % line)
            sys.exit(0)


    def actualparlist():
        # actualparitem ( , actualparitem ) *
        # | e

        # list of actual parameters
        global tokenType

        actualparitem()
        while tokenType == 'comma_token':
            tokenType = lexicalAnalyzer()
            actualparitem()
        return


    def actualparitem():
        #   in expression
        # | inout ID

        # an actual parameter
        # "in": value, "inout": reference
        global tokenType

        if tokenType == 'in_token':
            tokenType = lexicalAnalyzer()
            e = expression()
            genQuad('PAR', e, 'CV', '_')
        elif tokenType == 'inout_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                idName = lexical
                tokenType = lexicalAnalyzer()
                genQuad('PAR', idName, 'REF', '_')
            else:
                print('Error in line %d: A parameter was expected after the keyword "inout".\n' % line)
                sys.exit(0)
        return


    def condition():
        # boolterm ( or boolterm ) *

        # boolean expression
        global tokenType
        B1 = emptyList()

        # Start P1
        B1 = boolTerm()
        # End P1
        while tokenType == 'or_token':
            # Start P2
            backPatch(B1[1], nextQuad())
            # End P2
            tokenType = lexicalAnalyzer()
            B2 = boolTerm()

            # Start P3
            B1[0] = merge(B1[0], B2[0])
            B1[1] = B2[1]
            # End P3
        return [B1[0],B1[1]]


    def boolTerm():
        # boolfactor ( and boolfactor )*

        # term in boolean expression
        global tokenType
        Q1 = emptyList()
        # Start P1
        Q1 = boolfactor()
        # End P1
        while tokenType == 'and_token':
            tokenType = lexicalAnalyzer()
            # Start P2
            backPatch(Q1[0], nextQuad())
            # End P2

            Q2 = boolfactor()

            # Start P3
            Q1[1] = merge(Q1[1], Q2[1])
            Q1[0]= Q2[0]
            # End P3
        return [Q1[0],Q1[1]]


    def boolfactor():
        # factor in boolean expression

        global tokenType
        # not [ condition ]
        if tokenType == 'not_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftsquarebracket_token':
                tokenType = lexicalAnalyzer()
                R = condition()
                if tokenType == 'rightsquarebracket_token':
                    tokenType = lexicalAnalyzer()
                    return [R[0], R[1]]
                else:
                    print('Error in line %d: The right square bracket symbol "]" was expected here.\n' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The left square bracket symbol "[" was expected here.\n' % line)
                sys.exit(0)
        # [ condition ]
        elif tokenType == 'leftsquarebracket_token':
            tokenType = lexicalAnalyzer()
            R = condition()
            if tokenType == 'rightsquarebracket_token':
                tokenType = lexicalAnalyzer()
                return [R[0], R[1]]
            else:
                print('Error in line %d: The right square bracket symbol "]" was expected here.\n' % line)
                sys.exit(0)

        # expression REL_OP expression
        else:
            e1 = expression()
            relop = REL_OP()
            e2 = expression()

            # Start P1
            R_true = makeList(nextQuad())
            genQuad(relop, e1, e2, '_')
            R_false = makeList(nextQuad())
            genQuad('JUMP', '_', '_', '_')
            # End P1
        return [R_true,R_false]


    def expression():
        # optionalSign term ( ADD_OP term ) *

        # arithmetic expression
        global tokenType

        optionalSign()
        t1_place = term()
        while tokenType == 'plus_token' or tokenType == 'minus_token':
            op = ADD_OP()
            t2_place = term()
            # Start P1
            w = newTemp()
            genQuad(op, t1_place, t2_place, w)
            t1_place = w
            # End P1
        # Start P2
        e_place = t1_place
        # End P2
        return e_place



    def term():
        # factor ( MUL_OP factor ) *

        # term in arithmetic expression
        global tokenType

        f1_place = factor()
        while tokenType == 'multiply_token' or tokenType == 'division_token':
            op = MUL_OP()
            f2_place = factor()
            # Start P1
            w = newTemp()
            genQuad(op, f1_place, f2_place, w)
            f1_place = w
            # End P1
        # Start P2
        t_place = f1_place
        # End P2
        return t_place


    def factor():
        # factor in arithmetic expression
        global tokenType

        #   INTEGER
        if tokenType == 'INTEGER_token':
            fact = lexical
            tokenType = lexicalAnalyzer()
            return fact

        # | ( expression )
        elif tokenType == 'leftbracket_token':
            tokenType = lexicalAnalyzer()
            e = expression()
            if tokenType == 'rightbracket_token':
                fact = e
                tokenType = lexicalAnalyzer()
                return fact
            else:
                print('Error in line %d: The right bracket symbol ")" was expected here\n' % line)
                sys.exit(0)
        # | ID idTail
        elif tokenType == 'id_token':
            fact = lexical
            tokenType = lexicalAnalyzer()
            tail = idTail()
            if tail == 'par' :
                w = newTemp()
                genQuad('PAR',w ,'RET', '_')
                genQuad('CALL',fact ,'_', '_')
            return fact


    def idTail():
        # ( actualparlist )
        # | e

        # follows a function or procedure
        # describes parethneses and parameters
        global tokenType

        if tokenType == 'leftbracket_token':
            tokenType = lexicalAnalyzer()
            actualparlist()
            if tokenType == 'rightbracket_token':
                tokenType = lexicalAnalyzer()
                return 'par'
        return

    def optionalSign():
        # ADD_OP
        # | e

        # symbols "+" and "-" (are optional)
        global tokenType
        if tokenType == 'plus_token' or tokenType == 'minus_token':
            opSign = ADD_OP()
            tokenType = lexicalAnalyzer()
            return opSign
        return

    ########################################
    # lexer rules: relational, arithentic operations, integer values and ids
    ########################################

    def REL_OP():
        # = | <= | >= | > | < | <>
        global tokenType
        global lexical

        if (tokenType == 'equals_token' or tokenType == 'lessorequals_token' or tokenType == 'greaterorequals_token'
                or tokenType == 'less_token' or tokenType == 'greater_token' or tokenType == 'notequal_token'):
            relOp = lexical
            tokenType = lexicalAnalyzer()
        else:
            print('Error in line %d: A comparison sign was expected here.' % line)
            sys.exit(0)
        return relOp


    def ADD_OP():
        # + | -
        global tokenType
        global lexical

        if tokenType == 'plus_token' or tokenType == 'minus_token':
            addOp = lexical
            tokenType = lexicalAnalyzer()
        else:
            print('Error in line %d: A plus sign(+) or a minus sign(-) was expected here.' % (line))
            sys.exit(0)
        return addOp


    def MUL_OP():
        # * | /
        global tokenType
        global lexical

        if tokenType == 'multiply_token' or tokenType == 'division_token':
            mulOp = lexical
            tokenType = lexicalAnalyzer()
        else:
            print('Error in line %d: A multiplication sign(*) or a division sign(/) was expected here.' % (line))
            sys.exit(0)
        return mulOp
    program()


def intFile(int_file):
    global listOfQuads
    for quad in listOfQuads:
        int_file.write('%s: %s , %s , %s , %s\n' % (quad.label, quad.op1, quad.op2, quad.op3, quad.op4))


def cFile(c_file):

    c_file.write('#include <stdio.h>\n')
    c_file.write('#include <stdlib.h>\n\n')
    c_file.write('int main(){\n')
    c_file.write('{\t')

    global listOfTemps
    varlist = list()
    variables = ''

    for quad in listOfQuads:
        op1, op2, op3, op4 = str(quad.op1), str(quad.op2), str(quad.op3), str(quad.op4)
        if op1 != 'BEGIN_BLOCK' and op1 != 'END_BLOCK':
            if op2 not in varlist and not (op2.isdigit()):  # if its not already in list, append it
                if op2 != '_' and op2[0] != '-' and op2[0] != '+':  # check if number has + or - (eg. -1000)
                    varlist.append(op2)

            if op3 not in varlist and not (op3.isdigit()):
                if op3 != '_' and op3[0] != '-' and op3[0] != '+':
                    varlist.append(op3)

            if op4 not in varlist and not (op4.isdigit()):
                if op4 != '_' and op4[0] != '-' and op4[0] != '+':
                    varlist.append(op4)

    c_file.write('\n   int ')  # for variable declaration in C file. (Eg. int a,b,c;)

    for x in varlist:
        variables = variables + (x + ',')  # separate each variable declaration with comma

    c_file.write(variables[:-1] + ';\n')  # trim the last comma

    for quad in listOfQuads:
        label, op1, op2, op3, op4 = str(quad.label), str(quad.op1), str(quad.op2), str(quad.op3), str(quad.op4)
        print(op1, op2, op3, op4)
        
        if op1 == '+' or op1 == '-' or op1 == '*' or op1 == '/':
            c_file.write('\n   L_' + label + ': ' + op4 + ' = ' + op2 + op1 + op3 +';//('+op1 +', '+ op2 +', '+ op3 +', '+op4+')')
        elif op1 == '<' or op1 == '>' or op1 == '=' or op1 == '>=' or op1 == '<=' or op1 == '<>':
            if op1 == '=':
                c_file.write('\n   L_' + label + ': ' + 'if(' + op2 + ' == ' + op3 + ') goto L_' + op4 + ';//('+op1 +', '+ op2 +', '+ op3 +', '+op4+')')
            elif op1 == '<>':
                c_file.write('\n   L_' + label + ': ' + 'if(' + op2 + ' != ' + op3 + ') goto L_' + op4 + ';//('+op1 +', '+ op2 +', '+ op3 +', '+op4+')')
            else:
                c_file.write('\n   L_' + label + ': ' + 'if(' + op2 + op1 + op3 + ') goto L_' + op4 + ';//('+op1 +', '+ op2 +', '+ op3 +', '+op4+')')
        elif op1 == ':=':
            c_file.write('\n   L_' + label + ': '+ op4 + ' = ' + op2 + ';//(:=,' + op2 + ',_,' + op4 + ')')
        elif op1 == 'JUMP':
            c_file.write('\n   L_' + label + ': ' + 'goto L_' + op4 + ';//(Jump,_,_,' + op4 + ')')
        elif op1 == 'OUT':
            c_file.write('\n   L_' + label + ': ' + 'Printf("%d",' + op2 + ');')
        elif op1 == 'INP':
            c_file.write('\n   L_' + label + ': ' + 'Scanf("%d",&' + op2 + ');')
        elif op1 == 'RET':
            c_file.write('\n   L_' + label + ': ' + 'Return("%d",&' + op2 + ');')
        elif op1 == 'HALT':
            c_file.write('\n   L_' + label + ':  {}')
    c_file.write('\n}')  # close the main block


def exportFiles():

    # create test.int file
    int_file = open('test.int', 'a+')

    # create test.c file
    c_file = open('test.c', 'w+')

    syntaxAnalyzer(c_file)

    intFile(int_file)
    cFile(c_file)

    int_file.close()
    c_file.close()


# Opening file, as arguement in command line:
file = open(sys.argv[1], 'r')

exportFiles()
# create scopes.txt file
scopes_file = open('scopes.txt', 'a+')
