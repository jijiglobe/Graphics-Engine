import mdl
print "mdl imported"
from display import *
print "display imported"
from matrix import *
print "matrix imported"
from draw import *
print "draw imported"

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    print "colors initialized"
    tmp = new_matrix()
    print "matrix created"
    ident( tmp )
    print "setup complete"
    p = mdl.parseFile(filename)
    
    if p:
        print "file lexing complete"
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stackFunctions = ["push","pop"]
    modFunctions = ["move","rotate","scale"]
    drawFunctions = ["box","sphere","torus","line"]
    otherFunctions = ["display","save"]
    stack = [ tmp ]
    screen = new_screen()
    
    print stack
    
    print "commands parsing..."
    for command in commands:
        print command
        if command[0] in stackFunctions:
            if command[0] == "push":
                copy = []
                for x in stack[0]:
                    empty = []
                    copy.append(empty)
                    for y in x:
                        copy[-1].append(y)
                stack.append(copy)
            elif command[0] == "pop":
                stack.pop()
            #print stack[0] == stack[1]
            print "stack function\ncurrent stack: "+str(stack)+"\n"
 
        elif command[0] in modFunctions:
            if command[0] == "move":
                matrix_mult(make_translate(command[1],command[2],command[3]),stack[-1])
            elif command[0] =="rotate":
                if command[1] == "x": 
                    matrix_mult(make_rotX(command[2]),stack[-1])
                elif command[1] == "y":
                    matrix_mult(make_rotY(command[2]),stack[-1])
                elif command[1] == "z":
                    matrix_mult(make_rotZ(command[2]),stack[-1])
            elif command[0] == "scale":
                matrix_mult(make_scale(command[1],command[2],command[3]),stack[-1])
            print "modifying function\ncurrent top: "+str(stack[-1])+"\n"
        elif command[0] in drawFunctions:
            print "draw function\n"
        elif command[0] in otherFunctions:
            print "other function\n"
        else:
            print "command not recognized...\n"
       
    
